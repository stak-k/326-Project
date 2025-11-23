# class that stores the rental property data entered by the user

# Import Validator and Coordinates
from validator import Validator
from coordinates import Coordinates
# Import necessary formatters
from formatter import ( format_address, format_rent_display )

from property_type import *
from property import Property

class RentalProperty:
    """Stores validated data for single property.
    
    Attributes:
        _address (str): Formatted property address
        _rent (float): Validated rent amount
        _zipcode (int): 5 digit zipcode   
        _utilities_included (bool): Whether utilities are included in rent
        _coordinates (tuple): (latitude, longitude) of the property
        _validator (Validator): Validator instance for data validation
    """

    def __init__(self, address: str, rent: float, zipcode: int, utilities_included: bool):
        """Initialize a rental property with validation and formatting
        Args:
            address (str): Full rental address.
            rent (float): Monthly rent amount.
            zipcode (int): 5-digit ZIP code for the property.
            utilities_included (bool): Whether utilities are included.

        Raises:
            TypeError: If an argument has an incorrect data type.
            ValueError: If an argument fails validation rules.     
        """

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
        if self._validator.validate_zip(str(zipcode)):
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
        """Sets the rental property address after validation and formatting
        
        Args:
            new_address (str): The new address to set.
        """
        if self._validator.validate_address(new_address):
            self._address = format_address(new_address)
            # Update coordinates when address changes
            self._coordinates = Coordinates(self._address).coordinates

        
    # Rent Getter 
    @property 
    def rent(self): 
        """Returns the rent for the rental property"""
        return self._rent 

    # Rent Setter
    @rent.setter
    def rent(self, new_rent: float):
        """Sets the rent for the rental property after validation
         Args:
            new_rent (float): New rent value to set.
        """
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
        """Sets the zipcode for the rental property after validation
            Args:
                new_zipcode (int): New zipcode value to set.
        """
        if self._validator.validate_zip(str(new_zipcode)):
            self._zipcode = int(new_zipcode) 
            
    # Utilities Included Getter 
    @property 
    def utilities_included(self):
         """Returns whether utilities are included in the rent"""
         return self._utilities_included
    
    # Utilities Included Setter
    @utilities_included.setter
    def utilities_included(self, included: bool):
         """Sets whether utilities are included in the rent
         Args:
            included (bool): True if utilities are included, False otherwise.
         """
         self._utilities_included = bool(included)
         
    # Coordinates Getter
    @property 
    def coordinates(self):
        """Returns the (latitude, longitude) tuple for the rental property"""
        return self._coordinates
    
    # Summary Method for saving or exporting data 
    def summary(self):
         """Returns a summary representation of the property
         
         Returns:
            dict: A dictionary containing address, rent, ZIP, utilities, and coordinates.
         """
         return{ "address": self._address,
            "rent": format_rent_display(self._rent),
            "zipcode": self._zipcode,
            "utilities_included": self._utilities_included,
            "coordinates": self._coordinates
            }                 
    
    def __str__(self):
        """Readable string representation of the rental property
        
        Returns:
            str: A descriptive string representation of the property details.
        """
        included = "Yes" if self._utilities_included else "No"
        return f"{self._address} — {format_rent_display(self._rent)} | ZIP: {self._zipcode} | Utilities Included: {included}"
    

    def __init__(self, address, rent, zipcode, utilities_included, property_type_name, lease_term):

        type_map = {
            "Studio": Studio,
            "1x1": OneByOne,
            "2x1": TwoByOne,
            "2x2": TwoByTwo,
            "3x2": ThreeByTwo,
            "3x3": ThreeByThree,
            "4x2": FourByTwo,
            "4x3": FourByThree,
            "4x4": FourByFour,
            "Basement": Basement,
            "Shared House": SharedHouse
        }

        # Validate correct property type
        if property_type_name not in type_map:
            raise ValueError(f"Unknown property type: {property_type_name}")
        
        # Intiatlize the correct subclass
        self.property_type_obj = type_map[property_type_name](
            address,
            rent,
            lease_term
        )

        # Store other basic attributes
        self.zipcode = zipcode
        self.utilities_included = utilities_included