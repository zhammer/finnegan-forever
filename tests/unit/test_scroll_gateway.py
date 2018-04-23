"""Test module for the scroll gateway."""

import tempfile
from unittest.mock import patch
import pytest
from finnegan_forever.gateways.ascii_scroll import AsciiScrollGateway

class TestAsciiScrollGateway:
    """Test suite for the AsciiScrollGateway."""

    def test_init_file_doesnt_exist(self):
        """AsciiScrollGateway should raise a FileNotFound error if the scroll file doesnt exist."""
        # Given
        with patch('finnegan_forever.gateways.ascii_scroll.os.path') as mock_os_path:
            mock_os_path.isfile.return_value = False

            # When / Then
            with pytest.raises(FileNotFoundError):
                scroll = AsciiScrollGateway('filename.txt')

    def test_init_file_exists(self):
        """AsciiScrollGateway should raise a FileNotFound error if the scroll file doesnt exist."""
        # Given
        with patch('finnegan_forever.gateways.ascii_scroll.os.path') as mock_os_path:
            mock_os_path.isfile.return_value = True

            # When / Then
            scroll = AsciiScrollGateway('filename.txt')


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
            scroll = AsciiScrollGateway(temp.name)

            # Then
            assert len(scroll) == len(text)

    @pytest.mark.parametrize('text,block_size', [
        (pytest.lazy_fixture('a_field_of_cotton'), 10),
        (pytest.lazy_fixture('i_hear_an_army'), 10),
        (pytest.lazy_fixture('a_field_of_cotton'), 50),
        (pytest.lazy_fixture('i_hear_an_army'), 50)
    ])
    def test_read_passage(self, text, block_size):
        """Test the AsciiScrollGateway.read_passage function."""

        # Given
        with tempfile.NamedTemporaryFile(buffering=0) as temp:
            temp.write(text)

            # When
            scroll = AsciiScrollGateway(temp.name)

            # Then
            offset = 0
            while offset < len(text):
                expected = text[offset: offset + block_size]
                scroll_passage = scroll.read_passage(offset, block_size)
                assert scroll_passage.encode('utf-8') == expected

                offset += block_size
