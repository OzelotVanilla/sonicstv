from sonicstv.pic_manip.line_process_algo.type import PictureMonocolourLine
from sonicstv.sstv_spec import SSTVSpec, ColourValue
from sonicstv.pic_manip.line_process_algo.util import clampColourValue


def nudgeAll(
    pic_line: PictureMonocolourLine, colour_value: ColourValue | list[ColourValue], _: type[SSTVSpec],
    *, strength: float = 0.25
) -> PictureMonocolourLine:
    """
    Nudge the pixels in the whole channel/component toward given value.

    **Notice**: Unlike `biasAll`, which calculates the average of each line (all pixel gets same move),
     `nudgeAll` checks/moves pixel by pixel (farther pixel value got bigger move).

    ### Parameters:
    * `strength`: How hard will the original colour being pushed to target colour.
      0 means nothing modified. 1 means completely overwrite.
    """

    strength = max(0, min(strength, 1))

    if isinstance(colour_value, list):
        result_line = pic_line.copy()
        for i in range(min(len(pic_line), len(colour_value))):
            result_line[i] = clampColourValue(round(pic_line[i] + (colour_value[i] - pic_line[i]) * strength))
        return result_line
    else:
        return [
            clampColourValue(round(x + (colour_value - x) * strength))
            for x in pic_line
        ]
