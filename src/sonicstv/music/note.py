from abc import ABC as AbstractClass, abstractmethod

from sonicstv.sstv_spec import FrequencyValue, ColourValue, SSTVSpec


type NoteDuration = int


class Note(AbstractClass):
    """
    Abstract class for all sonicstv notes.
    """

    duration_frame: NoteDuration = 1

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def getFreq(self) -> FrequencyValue | list[FrequencyValue]: ...

    @abstractmethod
    def getColourValue(self, sstv_spec: type[SSTVSpec]) -> ColourValue | list[ColourValue]: ...


class SingleFreqNote(Note):
    """
    Note that only
    """

    freq: float

    def __init__(self, freq: FrequencyValue, duration_frame: NoteDuration = 1) -> None:
        """
        Arguments:
        frame_start: 
        """
        super().__init__()
        self.freq = freq
        self.duration_frame = duration_frame

    def getFreq(self) -> FrequencyValue:
        return self.freq

    def getColourValue(self, sstv_spec: type[SSTVSpec]) -> ColourValue | list[int]:
        return sstv_spec.convertFreqToColourValue(self.freq)
