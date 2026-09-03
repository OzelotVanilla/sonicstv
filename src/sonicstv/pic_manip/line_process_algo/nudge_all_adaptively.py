import numpy

from sonicstv.pic_manip.line_process_algo.type import PictureMonocolourLine
from sonicstv.sstv_spec import SSTVSpec, ColourValue
from sonicstv.pic_manip.line_process_algo.util import clampColourValue


def nudgeAllAdaptively(
    pic_line: PictureMonocolourLine, colour_value: ColourValue | list[ColourValue], _: type[SSTVSpec],
    *, max_strength: float = 1, min_strength: float = 0.03, strength_reference: float = -1
) -> PictureMonocolourLine:
    """
    Nudge the pixels in the whole channel/component toward given value,
     while the strength is auto-calculated from the local complexity of neighbour pixels.
    If the neighbour shows a complex colour change, modify the pixel harder.

    In this version, standard deviation (SD) is used for calculating the complexity.

    **Notice**: Unlike `biasAll`, which calculates the average of each line (all pixel gets same move),
     `nudgeAll` checks/moves pixel by pixel (farther pixel value got bigger move).

    ### Parameters:
    * `max_strength`: How hard will the original colour being pushed to target colour at maximum.
      0 means nothing modified. 1 means completely overwrite at most complex area.
      Should not be bigger than `min_strength`.
    * `min_strength`: How hard will the original colour being pushed to target colour at minimum.
          0 means nothing modified. 1 means completely overwrite at most complex area.
      Should not be smaller than `max_strength`.
    * `strength_reference`: The threshold of complexity that makes strength to 1.
      In current version that is, if SD is bigger than this value, it will makes strength to 1.
      If this value is not set-ed, it will be auto calculated in runtime.
    """
    # # Check if param is correct.
    if max_strength < min_strength:
        raise RuntimeError(
            f"[ERR ] `max_strength` ({max_strength}) should be bigger than `min_strength` ({min_strength})"
            + " for `nudgeAllAdaptively`."
        )

    # # Get the local complexity.
    complexity_array = [
        getLocalComplexityOfStandardDeviation(pic_line, i)
        for i in range(0, len(pic_line))
    ]

    # # Calculate a `strength_reference` if not set-ed.
    if strength_reference < 0:
        strength_reference = max(
            20,
            calculateStrengthReference(complexity_array)
        )

    # # Calculate pixel-specific strength for nudge.
    multiplier_array = [
        max(0, min(1, complexity_array[i] / strength_reference))
        for i in range(0, len(pic_line))
    ]
    raw_strength_array = [
        min_strength + multiplier_array[i] * (max_strength - min_strength)
        for i in range(0, len(pic_line))
    ]

    # # Smooth the strength array by get their mean.
    strength_array = [
        numpy.mean(getNearbyElements(raw_strength_array, i, 5))
        for i in range(0, len(pic_line))
    ]

    # # Nudge all pixels with given strength.
    if isinstance(colour_value, list):
        result_line = pic_line.copy()
        for i in range(0, len(pic_line)):
            result_line[i] = clampColourValue(round(
                pic_line[i] + (colour_value[i] - pic_line[i]) * strength_array[i]
            ))
        return result_line
    else:
        return [
            clampColourValue(round(pic_line[i] + (colour_value - pic_line[i]) * strength_array[i]))
            for i in range(0, len(pic_line))
        ]


def getLocalComplexityOfStandardDeviation(pic_line: PictureMonocolourLine, index: int, count: int = 5) -> float:
    """
    `count` is the number of elements to take for the SD, including the `index`-pointed one,
     so must be odd number.
    """

    return numpy.std(getNearbyElements(pic_line, index, count))  # standard deviation of local pixels


def calculateStrengthReference(complexity_array: list[float]) -> float:
    """
    Use percentile-90 value for now.
    """

    return numpy.percentile(complexity_array, 90)


def getNearbyElements[ElementType](arr: list[ElementType], i: int, n: int) -> list[ElementType]:
    length_of_arr = len(arr)
    number_of_neighbour_to_take = round((n - 1) / 2)

    result = []
    for i in range(i - number_of_neighbour_to_take, i + number_of_neighbour_to_take + 1):
        if i in range(0, length_of_arr):
            result.append(arr[i])

    return result
