"""Module for the scroll gateway.

Available classes:
- ScrollGateway: Read passages from a file-based scroll.
"""

import os.path


class ScrollGateway:
    """Gateway class for interacting with a file-based scroll.

    Available function:
    - __len__: Get the length in bytes of the file the scroll represents.
    - read_passage: Read a passage of a given length at a given offset into the scroll.
    """

    def __init__(self, filename):
        """C'tor"""
        if not os.path.isfile(filename):
            raise FileNotFoundError('Scroll file "%s" not found.', filename)
        self._filename = filename


    def __len__(self):
        """Get the length in bytes of the file the scroll represents."""
        return os.path.getsize(self._filename)


    def read_passage(self, offset, passage_size):
        """Read a passage of length `passage_size` at `offset` chars into the scroll."""
        with open(self._filename, 'r') as scroll_file:
            scroll_file.seek(offset)
            return scroll_file.read(passage_size)
