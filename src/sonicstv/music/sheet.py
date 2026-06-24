from sonicstv.music.note import Note


class Sheet:
    """
    Sheet to play, constructed 
    """

    notes: list[Note]

    offset_start: int = 0
    """
    Make how many silent frame until the notes start to play.
    """

    def __init__(
            self,
            notes: list[Note],
            *,
            offset_start: int = 0
    ) -> None:
        self.notes = notes
        self.offset_start = offset_start
