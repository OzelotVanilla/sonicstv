from sonicstv.sstv_spec.base import (
    SSTVSpec, SSTVColourSpace, SSTVChannelName,
    TimeInSecond,
)

from typing import ClassVar


class SSTVRGBSeriesSpec(SSTVSpec):
    duration__per_channel_scan: ClassVar[TimeInSecond]
    """
    How much time is taken to transmit one colour component's pixel data.

    Unit: second.
    This does not include sync, porch, or separator gap.
    """

    @classmethod
    def getPixelDuration(cls) -> TimeInSecond:
        return cls.duration__per_channel_scan / cls.image_width

    @classmethod
    def getNoteSlotCount(cls) -> int:
        return cls.image_height * len(cls.line_scan_sequence)


class MartinM1(SSTVRGBSeriesSpec):
    name: ClassVar[str] = "Martin M1"

    image_width: ClassVar[int] = 320
    image_height: ClassVar[int] = 256

    duration: ClassVar[TimeInSecond] = 114

    colour_space: ClassVar[SSTVColourSpace] = "RGB"

    line_scan_sequence: ClassVar[tuple[SSTVChannelName, ...]] = ("G", "B", "R")

    duration__per_channel_scan: ClassVar[TimeInSecond] = 0.146432


class MartinM2(MartinM1):
    name: ClassVar[str] = "Martin M2"

    image_width: ClassVar[int] = 160
    image_height: ClassVar[int] = 256

    duration: ClassVar[TimeInSecond] = 58
    duration__per_channel_scan: ClassVar[TimeInSecond] = 0.073216


class ScottieS1(SSTVRGBSeriesSpec):
    name: ClassVar[str] = "Scottie S1"

    image_width: ClassVar[int] = 320
    image_height: ClassVar[int] = 256

    duration: ClassVar[TimeInSecond] = 110

    colour_space: ClassVar[SSTVColourSpace] = "RGB"

    line_scan_sequence: ClassVar[tuple[SSTVChannelName, ...]] = ("G", "B", "R")

    duration__per_channel_scan: ClassVar[TimeInSecond] = 0.13824
    """
    For general SSTV: 138.24 ms

    For PySSTV: SCAN = 138.24 ms - 1.5 ms = 136.74 ms
    """


class ScottieS2(ScottieS1):
    name: ClassVar[str] = "Scottie S2"

    image_width: ClassVar[int] = 320
    """
    PySSTV uses 160.
    """
    image_height: ClassVar[int] = 256

    duration: ClassVar[TimeInSecond] = 71
    duration__per_channel_scan: ClassVar[TimeInSecond] = 0.086564


class ScottieDX(ScottieS1):
    name: ClassVar[str] = "Scottie DX"

    image_width: ClassVar[int] = 320
    image_height: ClassVar[int] = 256

    duration: ClassVar[TimeInSecond] = 269
    duration__per_channel_scan: ClassVar[TimeInSecond] = 0.3441


class WraaseSC2120(SSTVRGBSeriesSpec):
    name: ClassVar[str] = "Wraase SC2-120"

    image_width: ClassVar[int] = 320
    image_height: ClassVar[int] = 256

    duration: ClassVar[TimeInSecond] = 120

    colour_space: ClassVar[SSTVColourSpace] = "RGB"

    line_scan_sequence: ClassVar[tuple[SSTVChannelName, ...]] = ("R", "G", "B")

    duration__per_channel_scan: ClassVar[TimeInSecond] = 0.156


class WraaseSC2180(WraaseSC2120):
    name: ClassVar[str] = "Wraase SC2-180"

    duration: ClassVar[TimeInSecond] = 180
    duration__per_channel_scan: ClassVar[TimeInSecond] = 0.235
