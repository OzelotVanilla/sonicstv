from sonicstv.pic_manip.line_process_algo.type import PictureMonocolourLine
from sonicstv.sstv_spec import SSTVSpec, ColourValue
from sonicstv.pic_manip.line_process_algo.util import clampColourValue


def biasAll(
    pic_line: PictureMonocolourLine, colour_value: ColourValue | list[ColourValue], _: type[SSTVSpec],
    *, strength: float = 0.25
) -> PictureMonocolourLine:
    """
    Calculate the average of the whole channel/component,
     and moves the whole channel/component towards target value, with a fixed value.

    **Notice**: Unlike `nudgeAll`, which checks/moves pixel by pixel (farther pixel value got bigger move),
         `biasAll` calculates the average of each line and then moves toward target (all pixel gets same move).

    ### Parameters:
    * `strength`: How hard will the original colour being pushed to target colour.
      0 means nothing modified. 1 means trying to move the average completely to target.
    """

    strength = max(0, min(strength, 1))

    if isinstance(colour_value, list):
        result_line = pic_line.copy()
        bias_array = [colour_value[i] - pic_line[i] for i in range(len(pic_line))]
        bias = round(sum(bias_array) / len(bias_array) * strength)
        for i in range(min(len(pic_line), len(colour_value))):
            result_line[i] = clampColourValue(pic_line[i] + bias)

        return result_line
    else:
        average = sum(pic_line) / len(pic_line)
        bias = round((colour_value - average) * strength)

        return [
            clampColourValue(x + bias)
            for x in pic_line
        ]
