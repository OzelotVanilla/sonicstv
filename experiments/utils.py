import os
from PIL import Image as PILImage
from pysstv.color import MartinM1 as PySSTVMartinM1


__all__ = [
    "convertImageToMartinM1Audio"
]


def convertImageToMartinM1Audio(
    image_path: str, output_path: str, *, should_overwrite_if_existed: bool = False
) -> None:
    """
    Convert an image into SSTV audio.
    """
    # # Check if given path is file, and make dir if necessary.
    if not should_overwrite_if_existed and os.path.isfile(output_path):
        raise RuntimeError(f"[ERR ] Cannot write to path `{output_path}` since it already existed.")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    pil_image = PILImage.open(image_path)
    sstv_sound = PySSTVMartinM1(pil_image, 48000, 16)
    sstv_sound.vox_enabled = True  # enable prefix sound
    sstv_sound.write_wav(output_path)
