from sonicstv.pic_manip.line_process_algo.type import PictureMonocolourLine
from sonicstv.sstv_spec import SSTVSpec, ColourValue


def coverAll(
    pic_line: PictureMonocolourLine, colour_value: ColourValue | list[ColourValue], _: type[SSTVSpec],
) -> PictureMonocolourLine:
    """
    Cover the whole channel/component with given value.
    """

    if isinstance(colour_value, list):
        return colour_value
    else:
        return [colour_value] * len(pic_line)
