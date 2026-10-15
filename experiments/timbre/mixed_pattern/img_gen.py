# Adopt from ChatGPT.

import os
import cv2
import numpy
import numpy.typing

pic_width: int = 320
pic_height: int = 256
output_dir: str = "experiments/timbre/mixed_pattern"

# Pattern: 2D brightness values, shape (256, 320).
# Image:   3D RGB pixels, shape (256, 320, 3).
type Pattern = numpy.typing.NDArray[numpy.float32]
type Image = numpy.typing.NDArray[numpy.uint8]


def toUInt8(pattern: Pattern) -> numpy.typing.NDArray[numpy.uint8]:
    """
    Round brightness values and limit them to 0..255.
    """
    return numpy.clip(numpy.rint(pattern), 0, 255).astype(numpy.uint8)


def createRGBImage(red: Pattern, green: Pattern, blue: Pattern) -> Image:
    """
    Combine three brightness patterns into one RGB image.
    """
    for channel in (red, green, blue):
        if channel.shape != (pic_height, pic_width):
            raise ValueError("Each channel must be 256 x 320.")

    return numpy.stack(
        (toUInt8(red), toUInt8(green), toUInt8(blue)), axis=2
    )


def createGreyscaleImage(pattern: Pattern) -> Image:
    """
    Make an RGB image with identical R, G, and B values.
    """
    return createRGBImage(pattern, pattern, pattern)


def saveImage(file_name: str, image: Image) -> None:
    """
    Save a complete RGB image to output_dir as PNG.
    """
    if image.shape != (pic_height, pic_width, 3):
        raise ValueError("Image must have shape (256, 320, 3).")
    if image.dtype != numpy.uint8:
        raise TypeError("Image dtype must be numpy.uint8.")
    if not file_name.lower().endswith(".png"):
        raise ValueError("File name must end with .png.")

    file_path = os.path.join(output_dir, file_name)
    bgr_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if not cv2.imwrite(file_path, bgr_image):
        raise OSError(f"Failed to save image: {file_path}")


def createSquarePattern(stripe_width: int, low: float, high: float) -> Pattern:
    """
    Alternate low and high brightness every stripe_width pixels.
    """
    if stripe_width <= 0:
        raise ValueError("stripe_width must be positive.")

    x = numpy.arange(pic_width)
    high_stripe = (x // stripe_width) % 2 == 1
    row = numpy.where(high_stripe, high, low).astype(numpy.float32)
    return numpy.tile(row, (pic_height, 1))


def createSinePattern(period_px: float, mean: float, amplitude: float) -> Pattern:
    """
    Repeat a smooth sine-wave brightness pattern along each row.
    """
    if period_px <= 0:
        raise ValueError("period_px must be positive.")

    x = numpy.arange(pic_width, dtype=numpy.float32)
    row = mean + amplitude * numpy.sin(2 * numpy.pi * x / period_px)
    return numpy.tile(row.astype(numpy.float32), (pic_height, 1))


def createTrianglePattern(period_px: float, mean: float, amplitude: float) -> Pattern:
    """
    Repeat a triangle-wave brightness pattern along each row.
    """
    if period_px <= 0:
        raise ValueError("period_px must be positive.")

    x = numpy.arange(pic_width, dtype=numpy.float32)
    phase = (x / period_px) % 1.0
    row = mean + amplitude * (4 * numpy.abs(phase - 0.5) - 1)
    return numpy.tile(row.astype(numpy.float32), (pic_height, 1))


def createSawPattern(period_px: float, mean: float, amplitude: float) -> Pattern:
    """
    Repeat a rising brightness ramp with a sudden reset.
    """
    if period_px <= 0:
        raise ValueError("period_px must be positive.")

    x = numpy.arange(pic_width, dtype=numpy.float32)
    phase = (x / period_px) % 1.0
    row = mean + amplitude * (2 * phase - 1)
    return numpy.tile(row.astype(numpy.float32), (pic_height, 1))


def createDualSinePattern(
    period1: float, amplitude1: float,
    period2: float, amplitude2: float,
    mean: float = 128.0,
) -> Pattern:
    """
    Combine two horizontal sine modulations.
    """
    if period1 <= 0 or period2 <= 0:
        raise ValueError("Periods must be positive.")

    x = numpy.arange(pic_width, dtype=numpy.float32)
    row = (
        mean
        + amplitude1 * numpy.sin(2 * numpy.pi * x / period1)
        + amplitude2 * numpy.sin(2 * numpy.pi * x / period2)
    )
    return numpy.tile(row.astype(numpy.float32), (pic_height, 1))


def createYSweepPattern(
    period_top: float, period_bottom: float,
    mean: float = 128.0, amplitude: float = 32.0,
) -> Pattern:
    """
    Change the horizontal sine period from top to bottom.
    """
    if period_top <= 0 or period_bottom <= 0:
        raise ValueError("Periods must be positive.")

    x = numpy.arange(pic_width, dtype=numpy.float32)
    pattern = numpy.empty((pic_height, pic_width), dtype=numpy.float32)

    for y in range(pic_height):
        fraction = y / (pic_height - 1)
        period = period_top + (period_bottom - period_top) * fraction
        pattern[y] = mean + amplitude * numpy.sin(2 * numpy.pi * x / period)

    return pattern


def createSmoothNoisePattern(
    seed: int, mean: float = 128.0,
    amplitude: float = 40.0, blur_sigma: float = 6.0,
) -> Pattern:
    """
    Create one smoothed random row and repeat it vertically.
    """
    if blur_sigma <= 0:
        raise ValueError("blur_sigma must be positive.")

    rng = numpy.random.default_rng(seed)
    noise = rng.standard_normal((1, pic_width)).astype(numpy.float32)
    noise = cv2.GaussianBlur(noise, (0, 0), sigmaX=blur_sigma)
    peak = float(numpy.max(numpy.abs(noise)))
    row = mean + amplitude * noise[0] / max(peak, 1e-8)
    return numpy.tile(row.astype(numpy.float32), (pic_height, 1))


if __name__ == "__main__":
    os.makedirs(output_dir, exist_ok=True)

    square = createSquarePattern(stripe_width=16, low=112, high=144)
    sine = createSinePattern(period_px=32, mean=128, amplitude=32)
    triangle = createTrianglePattern(period_px=32, mean=128, amplitude=32)
    saw = createSawPattern(period_px=32, mean=128, amplitude=32)
    dual_sine = createDualSinePattern(16, 24, 64, 12)
    sweep = createYSweepPattern(period_top=64, period_bottom=16)
    noise = createSmoothNoisePattern(seed=42)

    saveImage("square_wave.png", createGreyscaleImage(square))
    saveImage("sine_wave.png", createGreyscaleImage(sine))
    saveImage("triangle_wave.png", createGreyscaleImage(triangle))
    saveImage("sawtooth_wave.png", createGreyscaleImage(saw))
    saveImage("dual_sine.png", createGreyscaleImage(dual_sine))
    saveImage("y_sweep.png", createGreyscaleImage(sweep))
    saveImage("smooth_noise.png", createGreyscaleImage(noise))
    saveImage("rgb_combo.png", createRGBImage(square, sine, noise))
