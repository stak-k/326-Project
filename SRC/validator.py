# validate all user input before scoring (addresses, rent, zipcode, etc)

from function_library import (
    validate_rental_address,
    validate_rent_input,
    validate_zipcode,
    validate_listing_title,
    validate_email_contact,
    validate_class_locations
)

class Validator:
    """ Validates all of the user inputs for rental listings"""


    def __init__(self):
        pass #No strored data, only methods
    
    # Address
    def validate_address(self, address: str) -> bool:
        """ Validates rental address"""
        return validate_rental_address(address)
    
    # Rent
    def validate_rent(self, rent) -> bool:
        """Validate monthly rent as positive numeric input."""
        return validate_rent_input(rent)

    # Zipcode
    def validate_zip(self, zipcode: int) -> bool:
        """Validate ZIP code format."""
        return validate_zipcode(zipcode)

    # Listing Title
    def validate_title(self, title: str) -> str:
        """Validate and clean the listing title."""
        return validate_listing_title(title)

    # Email
    def validate_email(self, email: str) -> bool:
        """Validate email contact format."""
        return validate_email_contact(email)
    
    # Class Locations
    def validate_locations(self, selected: list[str]) -> list[str]:
        """Validate selected class locations."""
        return validate_class_locations(selected)