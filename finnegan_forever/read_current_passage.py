"""Module for the read_current_passage use case."""

from finnegan_forever.entities import passage


def read_current_passage(scroll, passage_size, reading_every, seconds):
    """Read the current passage of size `passage_size` from the given `scroll` based on the current
    time in seconds. For more information on how the current passage is selected, see the
    documentation for `finnegan_forever.entities.passage.current_passage_offset`. Return the text of
    the read passage.
    """
    scroll_size = len(scroll)
    passage_offset = passage.current_passage_offset(scroll_size, passage_size, reading_every, seconds)
    return scroll.read_passage(passage_offset, passage_size)
