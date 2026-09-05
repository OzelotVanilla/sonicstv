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
    Note that only has one frequency to play.
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


class RestNote(Note):
    """
    Note that plays no frequency, and add no overlays to the original pic.
    """

    def __init__(self, duration_frame: NoteDuration = 1) -> None:
        super().__init__()
        self.duration_frame = duration_frame

    def getFreq(self) -> FrequencyValue | list[FrequencyValue]:
        return []

    def getColourValue(self, sstv_spec: type[SSTVSpec]) -> ColourValue | list[ColourValue]:
        return []
