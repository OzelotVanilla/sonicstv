def clampColourValue(colour_value: int) -> int:
    """
    Clamp given colour value to `0..=255`.
    """

    return max(min(colour_value, 255), 0)
