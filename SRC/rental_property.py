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
        self._validator = Validator()
        self._coordinates = None  # Will be set after address validation

        # Validate and set address
        if self._validator.validate_address(address):
            self._address = format_address(address)
            # Initialize Coordinates object after address is validated
            self._coordinates = Coordinates(self._address).coordinates

        
        # Validate and set rent
        if self._validator.validate_rent(rent):
            self._rent = float(rent)

        # Validate and set zipcode
        if self._validator.validate_zip(zipcode):
            self._zipcode = int(zipcode)

        # Set utilities included
        self._utilities_included = bool(utilities_included)




    # Address Getter
    @property
    def address(self):
        """Returns the rental property address"""
        return self._address
        
    # Adress Setter
    @address.setter
    def address(self, new_address: str):
        """Sets the rental property address after validation and formatting"""
        if self._validator.validate_address(new_address):
            self._address = format_address(new_address)
            # Update coordinates when address changes
            self.coordinates = Coordinates(self._address).coordinates

        
    # Rent Getter 
    @property 
    def rent(self): 
        """Returns the rent for the rental property"""
        return self._rent 

    # Rent Setter
    @rent.setter
    def rent(self, new_rent: float):
        """Sets the rent for the rental property after validation"""
        if self._validator.validate_rent(new_rent):
            self._rent = float(new_rent)
            
    # Zipcode Getter
    @property
    def zipcode(self):
        """Returns the zipcode for the rental property"""
        return self._zipcode
    
    # Zipcode Setter
    @zipcode.setter
    def zipcode(self, new_zipcode: int):
        """Sets the zipcode for the rental property after validation"""
        if self._validator.validate_zip(new_zipcode):
            self._zipcode = int(new_zipcode) 
            
    # Utilities Included Getter 
    @property 
    def utilities_included(self):
         """Returns whether utilities are included in the rent"""
         return self._utilities_included
    
    # Utilities Included Setter
    @utilities_included.setter
    def utilities_included(self, included: bool):
         """Sets whether utilities are included in the rent"""
         self._utilities_included = bool(included)
         
    # Coordinates Getter
    @property 
    def coordinates(self):
        """Returns the (latitude, longitude) tuple for the rental property"""
        return self._coordinates
    
    # Summary Method for saving or exporting data 
    def summary(self):
         """Returns a summary representation of the property"""
         return{ "address": self._address,
            "rent": self._rent,
            "zipcode": self._zipcode,
            "utilities_included": self._utilities_included,
            "coordinates": self._coordinates
            }                 