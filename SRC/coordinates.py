
from function_library import get_property_coordinates

class Coordinates:
    """ Gets coordinates for a given rental property"""

    def __init__(self, address: str):
        """ Initialize with address and fetch coordinates"""
        self.address = address
        self.latitude, self.longitude = get_property_coordinates(address)


        