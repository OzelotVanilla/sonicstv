from abc import ABC as AbstractClass, abstractmethod
from typing import ClassVar, Literal


type FrequencyValue = float
type ColourValue = int
type TimeInSecond = float

type SSTVColourSpace = Literal["RGB", "YCbCr"]
type SSTVChannelName = Literal[
    "R", "G", "B", "Y", "Cb", "Cr",
    "R-Y", "B-Y", "Y0", "Y1"
]


class SSTVSpec(AbstractClass):
    name: ClassVar[str]

    image_width: ClassVar[int]
    image_height: ClassVar[int]

    duration: ClassVar[TimeInSecond]
    """
    How much time is taken to transmit the full image.
    """

    freq_low_bound: ClassVar[FrequencyValue] = 1500
    freq_high_bound: ClassVar[FrequencyValue] = 2300

    colour_low_bound: ClassVar[ColourValue] = 0x00
    colour_high_bound: ClassVar[ColourValue] = 0xff

    colour_space: ClassVar[SSTVColourSpace]

    line_scan_sequence: ClassVar[tuple[SSTVChannelName, ...]]
    """
    This is the SSTV scan sequence of channel in one line.
    Not the actual picture data.
    """

    @classmethod
    def clampFreqWithWarning(cls, freq: FrequencyValue) -> FrequencyValue:
        if not cls.freq_low_bound <= freq <= cls.freq_high_bound:
            old_freq = freq
            freq = max(cls.freq_low_bound, min(freq, cls.freq_high_bound))
            print(
                f"[WARN] Frequency {old_freq:8.2f} is out of bound "
                + f"({cls.freq_low_bound} ~ {cls.freq_high_bound}) of Martin M1. "
                + f"Clamped to {freq}."
            )

        return freq

    @classmethod
    def clampColourValueWithWarning(cls, colour_value: ColourValue) -> ColourValue:
        if not 0 <= colour_value <= 255:
            old_colour_value = colour_value
            colour_value = max(0, min(colour_value, 255))
            print(
                f"[WARN] Frequency {old_colour_value:<3} is out of bound (`0..=255`) of Martin M1. "
                + f"Clamped to {colour_value}."
            )

        return colour_value

    @classmethod
    def convertFreqToColourValue(cls, freq: FrequencyValue) -> ColourValue:
        """
        Convert a frequency value to colour value (`0..=255`).
        """

        freq = cls.clampFreqWithWarning(freq)
        colour_value = round((freq - cls.freq_low_bound) / (cls.freq_high_bound - cls.freq_low_bound) * 255)
        return max(cls.colour_low_bound, min(colour_value, cls.colour_high_bound))

    @classmethod
    def convertColourValueToFreq(cls, colour_value: ColourValue) -> FrequencyValue:
        """
        Convert a colour value (`0..=255`) to frequency.
        """

        colour_value = cls.clampColourValueWithWarning(colour_value)
        freq = colour_value / 255 * (cls.freq_high_bound - cls.freq_low_bound) + cls.freq_low_bound
        return max(cls.freq_low_bound, min(freq, cls.freq_high_bound))

    @classmethod
    @abstractmethod
    def getNoteSlotCount(cls) -> int: ...
