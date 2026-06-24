from sonicstv.pic_manip.line_process_algo.type import PictureMonocolourLine
from sonicstv.sstv_spec import SSTVSpec, ColourValue


def nudgeAll(
    pic_line: PictureMonocolourLine, colour_value: ColourValue | list[ColourValue], _: type[SSTVSpec],
    *, strength: float = 0.25
) -> PictureMonocolourLine:
    """
    Nudge the whole channel/component toward given value.

    ### Parameters:
    * `strength`: How hard will the original colour being pushed to target colour.
      0 means nothing modified. 1 means completely overwrite.
    """

    strength = max(0, min(strength, 1))

    if isinstance(colour_value, list):
        result_line = pic_line.copy()
        for i in range(min(len(pic_line), len(colour_value))):
            result_line[i] = max(0, min(
                round(pic_line[i] + (colour_value[i] - pic_line[i]) * strength),
                255
            ))
        return result_line
    else:
        return [
            max(0, min(
                round(x + (colour_value - x) * strength),
                255
            ))
            for x in pic_line
        ]
