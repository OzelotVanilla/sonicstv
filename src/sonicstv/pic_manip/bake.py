import cv2
import numpy
import os
from returns.pipeline import is_successful
from returns.maybe import Maybe, Some, Nothing
from returns.result import Result, Success, Failure
from dataclasses import dataclass

from sonicstv.music.sheet import Sheet
from sonicstv.sstv_spec import SSTVSpec, MartinM1
from sonicstv.pic_manip.line_process_algo import coverRandomly, LineProcessor


type OpenCVImage = cv2.typing.MatLike
type PixelRedValue = numpy.uint8
type PixelGreenValue = numpy.uint8
type PixelBlueValue = numpy.uint8
type OpenCVColourPixel = tuple[PixelBlueValue, PixelGreenValue, PixelRedValue]


def bake(
    picture_path: str, sheet: Sheet,
    sstv_spec: type[SSTVSpec] = MartinM1,
    line_process_algo: LineProcessor = coverRandomly,
) -> BakedImage | None:
    """
    Argument:

    convertFreqToColourValue: Function that convert frequency (calculated from `Note`) to colour value (one of the channel).
    """

    # # Read and resize image.
    image_read_result = readAndResizePicture(picture_path, sstv_spec)
    if not is_successful(image_read_result):
        print(image_read_result.failure())
        return None
    image = image_read_result.unwrap()

    # # Check if all notes could be played.
    playable_note_slot_count = sstv_spec.getNoteSlotCount()
    if len(sheet.notes) + sheet.offset_start > playable_note_slot_count:
        print(
            f"[WARN] Too long sheet, {len(sheet.notes) + sheet.offset_start - playable_note_slot_count}"
            + " notes at tail could not be played."
        )

    # # Burn note to picture.
    burn_result = burnSheetIntoImage(image, sheet, sstv_spec, line_process_algo)
    if not is_successful(burn_result):
        print(burn_result.failure())
        return None
    result_image = burn_result.unwrap()
    return BakedImage(result_image)


def readAndResizePicture(path: str, sstv_spec: type[SSTVSpec]) -> Result[OpenCVImage, str]:
    """
    Read the picture and resize it to specified sstv encoder required size.
    """

    # # Test if file exists.
    path = os.path.abspath(path)
    if not os.path.exists(path):
        return Failure(f"[ERR ] Provided path not exist: {path}.")
    if not os.path.isfile(path):
        return Failure(f"[ERR ] Provided path is not file: {path}.")

    # # Read image.
    image = cv2.imread(path)
    if image is None:
        return Failure(f"[ERR ] Unsupported extension or corrupted image at: {path}.")

    # # Resize image.
    image = cv2.resize(image, (sstv_spec.image_width, sstv_spec.image_height))

    return Success(image)


def burnSheetIntoImage(
    image: OpenCVImage,
    sheet: Sheet,
    sstv_spec: type[SSTVSpec],
    line_process_algo: LineProcessor
) -> Result[OpenCVImage, str]:
    # # Create result image from original image.
    result_image = image.copy()

    # # Process lines.
    notes = iter(sheet.notes)
    slot_index = 0

    for i in range(sstv_spec.image_height):
        line = result_image[i].copy()

        for channel_index, channel_type in enumerate(sstv_spec.line_scan_sequence):
            if slot_index < sheet.offset_start:
                slot_index += 1
                continue

            note = next(notes, None)
            if note is None:
                return Success(result_image)

            colour_value = note.getColourValue(sstv_spec)
            line_result = line_process_algo(
                image[i, :, channel_index].tolist(),
                colour_value,
                sstv_spec
            )

            match channel_type:
                case "B":
                    line[:, 0] = line_result

                case "G":
                    line[:, 1] = line_result

                case "R":
                    line[:, 2] = line_result

                case _:
                    return Failure(
                        f"[ERR ] SSTV Specification {sstv_spec.name} uses unsupported scan component "
                        f"`{channel_type}` in `burnSheetIntoImage`."
                    )

            slot_index += 1

        result_image[i] = line

    return Success(result_image)


@dataclass(frozen=True)
class BakedImage:
    image: OpenCVImage

    def save(self, path: str):
        is_image_write_success = cv2.imwrite(path, self.image)
        if not is_image_write_success:
            raise OSError(f"[ERR ] Failed to write to path `{path}`.")
