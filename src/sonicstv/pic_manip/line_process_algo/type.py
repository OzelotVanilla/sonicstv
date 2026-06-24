from typing import Callable, Concatenate

from sonicstv.sstv_spec import SSTVSpec, ColourValue


type PictureMonocolourLine = list[ColourValue]

type LineProcessor = Callable[
    [PictureMonocolourLine, ColourValue | list[ColourValue], type[SSTVSpec]],
    PictureMonocolourLine
]

type ConfigurableLineProcessor[**Args] = Callable[
    Concatenate[PictureMonocolourLine, ColourValue | list[ColourValue], Args],
    PictureMonocolourLine,
]
