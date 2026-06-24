import random

from sonicstv.pic_manip.line_process_algo.type import PictureMonocolourLine
from sonicstv.sstv_spec import SSTVSpec, ColourValue


def coverRandomly(
    pic_line: PictureMonocolourLine, colour_value: ColourValue | list[ColourValue], _: type[SSTVSpec],
    *, strength: float = 0.6
) -> PictureMonocolourLine:
    """
    Replace the existing value randomly.

    ### Parameters:
    * `strength`: How hard will the colour being written to original data. 1 means completely overwrite.
    """

    if isinstance(colour_value, list):
        return [
            colour_value[i] if random.random() < strength else pic_line[i]
            for i in range(len(pic_line))
        ]
    else:
        return [
            colour_value if random.random() < strength else x
            for x in pic_line
        ]
