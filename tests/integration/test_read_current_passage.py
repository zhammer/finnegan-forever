"""Integration test module for the read_current_passage use case."""

import pytest
from finnegan_forever.read_current_passage import read_current_passage


@pytest.mark.parametrize('text', [
    pytest.lazy_fixture('a_field_of_cotton'),
    pytest.lazy_fixture('i_hear_an_army')
])
class TestReadCurrentPassage:
    """Test suite for read_current_passage."""

    @pytest.mark.parametrize('size', [
        10,
        20,
        30,
        1000
    ])
    def test_passage_size(self, text, size):
        # Given
        scroll = InMemoryScrollGateway(text)
        passage_size = size
        reading_every = 4
        seconds = 0

        # When
        passage = read_current_passage(scroll, passage_size, reading_every, seconds)

        # Then
        expected = text[0:passage_size]
        assert passage == expected

# Mocks

class InMemoryScrollGateway:
    """Mock scroll gateway class. Uses an in-memory text block rather """

    def __init__(self, text):
        """C'tor"""
        self.text = text


    def __len__(self):
        """Get the length of self.text."""
        return len(self.text)


    def read_passage(self, offset, passage_size):
        """Read a passage of `passage_size` bytes starting at `offset`."""
        return self.text[offset: offset + passage_size]
