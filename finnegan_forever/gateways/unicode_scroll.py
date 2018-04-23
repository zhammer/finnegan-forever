"""Module for the scroll gateway.

Available classes:
- UnicodeScrollGateway: Read passages from a file-based scroll with unicode encoding.
"""

import os.path

UTF32_BYTES_PER_CHAR = 4


class UnicodeScrollGateway:
    """Gateway class for interacting with a file-based utf-32-be-encoded scroll. The underlying
    scroll file should be created with scripts/create_unicode_scroll.py. Using a scroll file that
    is not utf-32-be encoded with no combining characters will lead to undefined behavior.

    Available function:
    - __len__: Get the length in chars of the file the scroll represents.
    - read_passage: Read a passage of a given length in chars at a given char offset into the scroll.
    """

    def __init__(self, filename):
        """C'tor"""
        if not os.path.isfile(filename):
            raise FileNotFoundError('Scroll file "%s" not found.', filename)
        self._filename = filename


    def __len__(self):
        """Get the length in chars of the file the scroll represents."""
        return os.path.getsize(self._filename) // UTF32_BYTES_PER_CHAR


    def read_passage(self, offset, passage_size):
        """Read a passage of length `passage_size` chars at `offset` chars into the scroll."""
        offset_bytes = offset * UTF32_BYTES_PER_CHAR
        passage_size_bytes = passage_size * UTF32_BYTES_PER_CHAR

        with open(self._filename, 'rb') as scroll_file:
            scroll_file.seek(offset_bytes)
            return scroll_file.read(passage_size_bytes).decode('utf-32-be')
