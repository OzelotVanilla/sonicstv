import random
import numpy

from sonicstv.pic_manip.line_process_algo.type import PictureMonocolourLine
from sonicstv.sstv_spec import SSTVSpec, ColourValue, TimeInSecond, SSTVRGBSeriesSpec


def stampWindowed(
    pic_line: PictureMonocolourLine, colour_value: ColourValue | list[ColourValue], sstv_spec: type[SSTVSpec],
    * ,
    window_duration: TimeInSecond = 0.0732, strength: float = 0.8,
    window_offset: int | str = "random", window_jitter: int = -1
) -> PictureMonocolourLine:
    """
    Write the sound data only to part of the line, with fixed length.

    ### Parameters:
    * `window_duration`: How long will the note be played. Must be greater than 0.
    * `strength`: How hard will the colour being written to original data. 1 means completely overwrite.
    * `window_offset`: A fixed offset calculated from the center of original line to the center of windowed.
      Auto-clamped if the line goes out-of-range.
      Could be defined as `random` to let algorithm randomly decides its position.
    * `window_jitter`: A further random offset added to the windowed.
      Meaningful if only `window_offset` is defined, and `window_jitter` is bigger than 0.
      For example, if `window_offset = 20, window_jitter = 5`, `window_offset` will be range from 15 to 25, randomly.
    """

    # # First calculate how many pixel will be used.
    one_line_duration: TimeInSecond  # How many time is `sstv_spec` used to play one channel/component in one line.
    match sstv_spec:
        case _ if issubclass(sstv_spec, SSTVRGBSeriesSpec):
            one_line_duration = sstv_spec.duration__per_channel_scan

        case _:
            raise RuntimeError(
                f"[ERR ] Unsupported SSTV Specification `{sstv_spec.name}` for `PictureMonocolourLine`. "
                + "Nothing modified."
            )
    window_duration = max(0, min(window_duration, one_line_duration))
    pixel_needed = round(sstv_spec.image_width * window_duration / one_line_duration)

    # # Decide where it should be placed.
    calculated_left_offset: int
    match window_offset:
        case _ if isinstance(window_offset, int) and 0 <= window_offset:
            jitter_this_time = 0 if window_jitter <= 0 else random.randint(-window_jitter, window_jitter)
            calculated_left_offset = window_offset + jitter_this_time

        case "random":
            max_left_offset = sstv_spec.image_width - pixel_needed
            calculated_left_offset = random.randint(0, max_left_offset)

        case _:
            raise RuntimeError(f"[ERR ] Invalid value `{window_offset}` for `stampWindowed::window_offset`.")

    # # Calculate final result of colour values.
    colour_values_to_write = pic_line.copy()
    if isinstance(colour_value, list):  # Series of value.
        # Shrink/Grow colour_value if necessary (upsampling/downsampling).
        homogen_colour_value: list[ColourValue] = colour_value.copy()
        if len(colour_value) != pixel_needed:
            old_indexes = numpy.linspace(0, len(colour_value) - 1, len(colour_value))
            new_indexes = numpy.linspace(0, len(colour_value) - 1, pixel_needed)
            homogen_colour_value = numpy.interp(new_indexes, old_indexes, colour_value).tolist()
        colour_values_to_write = [
            homogen_colour_value[i] if random.random() < strength else pic_line[i]
            for i in range(calculated_left_offset, min(sstv_spec.image_width, pixel_needed + calculated_left_offset))
        ]
    else:  # Only one value
        for i in range(calculated_left_offset, min(sstv_spec.image_width, pixel_needed + calculated_left_offset)):
            colour_values_to_write[i] = colour_value if random.random() < strength else pic_line[i]

    return colour_values_to_write
