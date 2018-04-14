"""Module for the time gateway.

Available classes:
- TimeGateway: Get information about the current time.
"""

import time


class TimeGateway:
    """Gateway class for getting the current time.

    Available functions:
    - seconds: Get the number of seconds elapsed since the epoch.
    """

    @staticmethod
    def seconds():
        """Get the number of seconds elapsed since the epoch."""
        return int(time.time())
