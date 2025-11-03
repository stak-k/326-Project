
from function_library import get_property_coordinates

class Coordinates:
    """ Gets coordinates for a given rental property"""

    def __init__(self, address: str):
        """ Initialize with address and fetch coordinates"""
        self.address = address
        self.latitude, self.longitude = get_property_coordinates(address)


    # Address Getter
    @property
    def address(self) -> str:
        """ Returns the rental property address"""
        return self._address

    # Address Setter
    # Every time the address changes, the coordinates refresh, keeping data consistent
    @address.setter
    def address(self, new_address: str):
        """ Sets the rental property address and refreshes coordinates"""
        self._address = new_address
        self._coordinates = get_property_coordinates(new_address)

    # Coordinates Getter
    # Reads data safely without directly accessing private variables
    @property
    def coordinates(self) -> tuple:
        """ Returns the (latitude, longitude) tuple for the rental property"""
        return self._coordinates
    
    # Manual Refresh Method
    # Manual override to force a coordinate update
    def refresh_coordinates(self) -> tuple:
        """ Manually refreshes and returns the latest coordinates for the current address"""
        self._coordinates = get_property_coordinates(self._address)
        return self._coordinates
    

    # String Representation
    # For easy debugging and display
    def __str__(self):
            """
    Returns a string representation of the object showing 
    the address and its latitude and longitude.
    """
        lat, lon = self._coordinates
        return f"Address: {self._address}, Latitude: {lat}, Longitude: {lon}"
