"""Integration test module for finnegan_forever.gateways.unicode_scroll."""

import pytest
from finnegan_forever.gateways.unicode_scroll import UnicodeScrollGateway


def test_scroll_gateway_read(finnegans_wake_unicode_chars):
    """Read the entire Finnegan's Wake text using the UnicodeScrollGateway and check that all
    unicode characters are included in the read text.
    """
    scroll = UnicodeScrollGateway('finnegans-wake-scroll.txt')

    length = len(scroll)
    finnegans_wake = scroll.read_passage(0, length)

    words = finnegans_wake.split()
    assert 'riverrun,' == words[0]
    assert 'the' == words[-1]

    assert all(char in finnegans_wake for char in finnegans_wake_unicode_chars)


@pytest.fixture()
def finnegans_wake_unicode_chars():
    """Data fixture that returns a string of all unicode characters in Finnegan's Wake."""
    return '¤·àáãéìóôþŒŠŸˆ–—‘’‚“”‡…‹'
