from abc import ABC, abstractmethod
from formatter import format_address


class Property(ABC):
    """
    Abstract base class representing a generic rental property.

    This class defines the shared structure and behavior for all
    property types (e.g., Studio, 2x2, 4x4, etc.).

    It enforces a common interface using abstract methods so that
    all subclasses must implement:
        - rental_type()
        - type_score()

    This design supports inheritance and polymorphism.
    
    """
    def __init__(self, address: str, price: float, lease_term: int):
        """
        Initialize common attributes for all rental properties.

        Args:
            address (str): Property address
            price (float): Monthly rent
            lease_term (int): Lease duration in months

        Notes:
            - Address is formatted for consistency.
            - Price and lease term are cast to numeric types
              to prevent invalid data.
        """
        self.address = format_address(address)
        self.price = float(price)
        self.lease_term = int(lease_term)

    @abstractmethod
    def rental_type(self) -> str:
        """Return property type name( 'Studio', 'Two Bed + Two Bath', etc.)"""
        pass

    @abstractmethod
    def type_score(self) -> float:
        """Return a numeric score representing how desirable
        this property type is (0–10 scale).

        Each subclass defines its own scoring logic."""
        pass

    # -------------------
    # Shared Utility Methods
    # -------------------

    def to_dict(self) -> dict:
        """
        Convert the property details into a dictionary format.

        Returns:
            dict: Property attributes as key-value pairs.

        used for:
            - CSV export
            - Data persistence
            - Integration with PropertyManager
        """
        return {
            "Address": self.address,
            "Rent": self.price,
            "Lease Term": self.lease_term,
            "Property Type": self.rental_type(),
            "Type Score": self.type_score()
        }

    def __str__(self):
        return (
            f"{self.rental_type()} - {self.address} | "
            f"{self.price} | Lease: {self.lease_term}"
        )