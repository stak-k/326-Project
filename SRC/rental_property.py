# class that stores the rental property data entered by the user

# Import necessary formatters
from formatter import (
    format_address,
    format_rent_display
)

class RentalProperty:
    """Stores validated data for single property."""

    def __init__(self, address: str, rent: float, zipcode: int, utilities_included: bool):
        """Initialize a rental property with validation and formatting"""

        # Format each input
        self.address = format_address(address)