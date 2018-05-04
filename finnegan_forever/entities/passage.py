"""Module for the passage entity.

Available functions:
- current_passage_offset: Get the offset of the current passage in a scroll based on the time in seconds.
"""

import math


def current_passage_offset(scroll_size, passage_size, reading_every, seconds):
    """Get the offset of the current passage in a scroll. We assume that the scroll has been being
    read since the beginning of time, where a new passage of `passage_size` characters is read every
    `reading_every` seconds. We assume that after final passage in the scroll is read, the scroll is
    started from the beginning, and so on. `seconds` represents the number of seconds since the
    beginning of time. `scroll_size` represents the total number of characters in the scroll.

    # From a 270-char scroll, we're reading 40-char passages every 4 seconds. Since we are at 0
    # seconds, our offset is 0 -- the offset of the first passage.
    >>> current_passage_offset(scroll_size=270, passage_size=40, reading_every=4, seconds=0)
    0

    # A second elapses. Since a full 4 second window has not yet elapsed, we are still at offset 0.
    >>> current_passage_offset(scroll_size=270, passage_size=40, reading_every=4, seconds=1)
    0

    # Four seconds have elapsed. We are now reading from the second passage, at character 40.
    >>> current_passage_offset(scroll_size=270, passage_size=40, reading_every=4, seconds=4)
    40

    # Five more windows (20 seconds) elapse. We are five passages (200 characters) further into the
    # text. Note that the final passage in this case would not be a full length passage.
    >>> current_passage_offset(scroll_size=270, passage_size=40, reading_every=4, seconds=24)
    240

    # Another four seconds elapse. We are back at the beginning of the scroll!
    >>> current_passage_offset(scroll_size=270, passage_size=40, reading_every=4, seconds=28)
    0
    """
    num_passages_in_scroll = math.ceil(scroll_size / passage_size)
    windows_elapsed = seconds // reading_every
    current_passage_number = int(windows_elapsed % num_passages_in_scroll)
    return current_passage_number * passage_size
