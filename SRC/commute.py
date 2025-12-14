
from function_library import (
    calculate_commute_time, 
    calculate_distance
)
from coordinates import Coordinates
from validator import Validator
from formatter import format_address

# #  This class is responsible for calculating the distance and estimated
# commute time between two addresses.
#
# It acts as a connector between:
# - Validator: to make sure addresses are valid
# - Formatter: to normalize address formatting
# - Function library: to calculate distance and travel time
#
# The goal of this class is to keep commute logic separate from
# rental data and scoring logic, making the system modular and easier
# to test and maintain.
#
# This class is used by RentalProperty and ScoreCalculator to include
# commute convenience as part of the overall rental score.
class Commute:
    """Handles distance and time calculations between 2 locations 
        
        Integrates:
        - Validator: for address validation
        - Formatter: for address formatting
        - Function library: for commute time and distance calculations

        Example:
        c = Commute("7303 Baltimore Ave", "Edward St. John Learning Center", "walk")
        print(c)
            Walk commute from '7303 Baltimore Ave' -> 'Edward St. John Learning Center': 
                  1.2 miles, 25.6 min
    """

## Distance is calculated once, time depends on transportation mode
    def __init__(self, start_address: str, end_address: str, mode: str = "walk"):
        """
        Initialize with start and end addresses, and transportation mode.

            Args:
             start_address(str): The starting address for the commute
             end_address (str): The destination address for the commute
             mode (str): Mode of transportation ("walk", "bike", "drive", "bus"). Default is "walk"

             Raises: 
                ValueError: If either address is invalid. 

        Example:
            Commute("7303 Baltimore Ave", "Edward St. John Learning Center", "walk")
        """

        self._validator = Validator()
        self._mode = mode.lower()

        # Validate and format both addresses

        if not self._validator.validate_address(start_address):
            raise ValueError("Invalid start address.")
        if not self._validator.validate_address(end_address):
            raise ValueError("Invalid destination address.")
    
        self._start_address = format_address(start_address)
        self._end_address = format_address(end_address)
        
        # Calculate distance and time
        self._distance_miles = calculate_distance(self._start_address, self._end_address)
        self._time_minutes = calculate_commute_time(self._distance_miles, self._mode)


    @property
    def start_address(self):
        """Return formatted starting address."""
        return self._start_address

    @property
    def end_address(self):
        """Return formatted destination address."""
        return self._end_address

    @property
    def mode(self):
        """Return mode of transportation (walk, bike, drive, bus)."""
        return self._mode

    @mode.setter
    def mode(self, new_mode: str):
        """Update travel mode and recalculate time.
        Args:
            new_mode (str): The new transportation mode (UI-controlled: walk, shuttle, metro, drive).
        """
        self._mode = new_mode.lower()
        self._time_minutes = calculate_commute_time(self._distance_miles, self._mode)

    @property
    def distance_miles(self):
        """Return calculated distance in miles."""
        return self._distance_miles

    @property
    def time_minutes(self):
        """Return calculated travel time in minutes."""
        return self._time_minutes
    

    def refresh_commute(self):
        """Recalculate distance and time (if addresses changed)."""
        self._distance_miles = calculate_distance(self._start_address, self._end_address)
        self._time_minutes = calculate_commute_time(self._distance_miles, self._mode)

    def summary(self) -> dict:
        """Return a full commute summary dictionary.
        
            Returns: dict: Contains start, end, mode, distance(miles), and time(minutes).

            Example:
               {
                "start" : "7303 Baltimore Ave",
                "end" : "Edward St. John Learning Center"
                "mode" : "walk"
                "distance_miles" : 1.2,
                "time_minutes": 25.6
                }
        """
        return {
            "start": self._start_address,
            "end": self._end_address,
            "mode": self._mode,
            "distance_miles": self._distance_miles,
            "time_minutes": self._time_minutes
        }

    def __str__(self):
        """Readable text summary for printing or debugging.
        
            Example:
                Walk commute from '7303 Baltimore Ave' 
                    -> 'Edward St. John Learning Center': 1.25 miles, 24.0 min
        """
        return (f"{self._mode.title()} commute from '{self._start_address}' -> "
                f"'{self._end_address}': {self._distance_miles} miles, "
                f"{self._time_minutes} min")
