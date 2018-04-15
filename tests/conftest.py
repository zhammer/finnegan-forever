import pytest

HAMMER_EMOJI = '\U0001f528 '

def pytest_addoption(parser):
    """Turn on hammertime pytest display with --hammertime."""
    group = parser.getgroup('hammertime')
    group.addoption('--hammertime', action='store_true',
                    help='display "{}" instead of "." for passed tests'.format(HAMMER_EMOJI))

def pytest_report_teststatus(report):
    """Turn '.' success char into hammer emoji."""
    if pytest.config.getoption('hammertime'):
        if report.when == 'call' and report.outcome == 'passed':
            return (report.outcome, HAMMER_EMOJI, 'PASSED')


# Fixtures

@pytest.fixture()
def a_field_of_cotton():
    """Data fixture for Matsuo Basho's haiku 'A Field of Cotton'."""
    return b"""A field of cotton--
as if the moon
  had blossomed."""

@pytest.fixture()
def i_hear_an_army():
    """Data fixture for Joyce's poem 'I Hear an Army'."""
    return b"""I hear an army charging upon the land,
  And the thunder of horses plunging, foam about their knees:
Arrogant, in black armour, behind them stand,
  Disdaining the reins, with fluttering whips, the charioteers.

They cry unto the night their battle-name:
  I moan in sleep when I hear afar their whirling laughter.
They cleave the gloom of dreams, a blinding flame,
  Clanging, clanging upon the heart as upon an anvil.

They come shaking in triumph their long, green hair:
  They come out of the sea and run shouting by the shore.
My heart, have you no wisdom thus to despair?
  My love, my love, my love, why have you left me alone?"""
