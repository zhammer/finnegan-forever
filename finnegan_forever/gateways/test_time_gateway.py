"""Test module for the time gateway."""

from unittest.mock import patch
import pytest
from finnegan_forever.gateways.time_gateway import TimeGateway


@pytest.mark.parametrize(
    "time_time,expected", [
        (0, 0),
        (4.4, 4),
        (1300.2, 1300),
        (1525.9, 1525)
    ])
def test_seconds(time_time, expected):
    """Test TimeGateway.seconds with a few simple cases."""
    # Given
    with patch('finnegan_forever.gateways.time_gateway.time') as mock_time:
        mock_time.time.return_value = time_time
        time_gateway = TimeGateway()

        # When
        seconds = time_gateway.seconds()

    # Then
    assert seconds == expected
