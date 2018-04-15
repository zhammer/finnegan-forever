"""Test module for the scroll gateway."""

import tempfile
import pytest
from finnegan_forever.gateways.scroll_gateway import ScrollGateway

class TestScrollGateway:
    """Test suite for the scroll gateway."""

    @pytest.mark.parametrize('text', [
        pytest.lazy_fixture('a_field_of_cotton'),
        pytest.lazy_fixture('i_hear_an_army')
    ])
    def test_len_builtin(self, text):
        """Test the builtin __len__ function for a scroll."""

        # Given
        with tempfile.NamedTemporaryFile(buffering=0) as temp:
            temp.write(text)

            # When
            scroll = ScrollGateway(temp.name)

            # Then
            assert len(scroll) == len(text)

    @pytest.mark.parametrize('text,block_size', [
        (pytest.lazy_fixture('a_field_of_cotton'), 10),
        (pytest.lazy_fixture('i_hear_an_army'), 10),
        (pytest.lazy_fixture('a_field_of_cotton'), 50),
        (pytest.lazy_fixture('i_hear_an_army'), 50)
    ])
    def test_read_passage(self, text, block_size):
        """Test the ScrollGateway.read_passage function."""

        # Given
        with tempfile.NamedTemporaryFile(buffering=0) as temp:
            temp.write(text)

            # When
            scroll = ScrollGateway(temp.name)

            # Then
            offset = 0
            while offset < len(text):
                expected = text[offset: offset + block_size]
                scroll_passage = scroll.read_passage(offset, block_size)
                assert scroll_passage.encode('utf-8') == expected

                offset += block_size
