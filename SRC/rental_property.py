# class that stores the rental property data entered by the user

# Import Validator and Coordinates
from validator import Validator
from coordinates import Coordinates
# Import necessary formatters
from formatter import (
    format_address,
    format_rent_display
)

class RentalProperty:
    """Stores validated data for single property."""

    def __init__(self, address: str, rent: float, zipcode: int, utilities_included: bool):
        """Initialize a rental property with validation and formatting"""

        # Create helper objects
        self.validator = Validator()
        self.coordinates = None  # Will be set after address validation

        # Validate and set address
        if self._validator.validate_address(address):
            self._address = format_address(address)
            # Initialize Coordinates object after address is validated
            self.coordinates = Coordinates(self._address).coordinates

        
        # Validate and set rent
        if self._validator.validate_rent(rent):
            self._rent = float(rent)

        # Validate and set zipcode
        if self._validator.validate_zip(zipcode):
            self._zipcode = int(zipcode)

        # Set utilities included
        self._utilities_included = bool(utilities_included)