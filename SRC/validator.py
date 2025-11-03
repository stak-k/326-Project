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
    """ Validates all of the user inputs for rental listings
    
        Example:
        v = Validator()
        v.validate_address("123 Main St, College Park, MD")
        True

    """

    def __init__(self):
        pass #No strored data, only methods
    
    # Address
    def validate_address(self, address: str) -> bool:
        """ Validates rental address
        
        Args:
            address (str): Full address entered by the user.

        Returns:
            bool: True if address is valid; raises ValueError otherwise.

        Example:
            v = Validator()
            v.validate_address("8500 Paint Branch Dr, College Park, MD")
            True
        """
        return validate_rental_address(address)
    
    # Rent
    def validate_rent(self, rent) -> bool:
        """Validate monthly rent as positive numeric input.
        
        Args:
            rent (float | int): Rental price entered by the user.

        Returns:
            bool: True if valid; raises ValueError for negative or non-numeric values.

        Example:
            v.validate_rent(1500)
            True

        """
        return validate_rent_input(rent)

    # Zipcode
    def validate_zip(self, zipcode: int) -> bool:
        """Validate ZIP code format.
        
        Args:
            zipcode (str | int): The ZIP code to validate.

        Returns:
            bool: True if valid; raises ValueError otherwise.

        Example:
            v.validate_zip("20740")
            True
        """
        return validate_zipcode(zipcode)

    # Listing Title
    def validate_title(self, title: str) -> str:
        """Validate and clean the listing title.
        
        Args:
            title (str): Property title input from user.

        Returns:
            str: Cleaned title string; raises ValueError for invalid input.

        Example:
            v.validate_title("spacious apartment near umd")
            'Spacious Apartment Near Umd'
        """
        return validate_listing_title(title)

    # Email
    def validate_email(self, email: str) -> bool:
        """Validate email contact format.
        
        Args:
            email (str): Email address provided by the user.

        Returns:
            bool: True if valid email; raises ValueError otherwise.

        Example:
            v.validate_email("user@example.com")
            True
        """
        return validate_email_contact(email)
    
    # Class Locations
    def validate_locations(self, selected: list[str]) -> list[str]:
        """Validate selected class locations.
        
        Args:
            selected (list[str]): List of class building codes (e.g., ['ESJ', 'HBK']).

        Returns:
            list[str]: Validated list of building codes.

        Example:
            v.validate_locations(["ESJ", "HBK", "KEY"])
            ['ESJ', 'HBK', 'KEY']
            
        """
        return validate_class_locations(selected)
    
    def __str__(self) -> str:
        """
        String representation for easy debugging and logging.

        Returns:
            str: Text summary of what the validator supports.

        Example:
            v = Validator()
            print(v)
            Validator(active: address, rent, zip, title, email, class locations)
        """
        return "Validator(active: address, rent, zip, title, email, class locations)"