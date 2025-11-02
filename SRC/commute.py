# Calculates distance (miles) and estimated commute time between two addresses

from function_library import (
    calculate_commute_time, 
    calculate_distance
)
from coordinates import Coordinates
from validator import Validator
from formatter import format_address


class Commute:
    """Handles distance and time calculations between 2 locations """

    def __init__(self, start_address: str, end_address: str, mode: str = "walk"):
        """
        Initialize with start and end addresses, and transportation mode.
        Example:
            Commute("7303 Baltimore Ave", "Edward St. John Learning Center", "walk")
        """

        self._validator = Validator()
        self._mode = mode.lower()

        # Validate and format both addresses

        if self._validator.validate_address(start_address):
            self._start_address = format_address(start_address)
        if self._validator.validate_address(end_address):
            self._end_address = format_address(end_address)

        # Calculate distance and time
        self._distance_miles = calculate_distance(self._start_address, self._end_address)
        self._time_minutes = calculate_commute_time(self._distance_miles, self._mode)


