from abc import ABC, abstractmethod
from formatter import format_address


class Property(ABC):
    def __init__(self, address: str, price: float, lease_term: str):
        self.address = address
        self.price = price
        self.lease_term = lease_term

    @abstractmethod
    def rental_type(self) -> str:
        """Return property type name( 'Studio', 'Room')"""
        pass

    @abstractmethod
    def type_score(self) -> float:
        """Return score based on property type"""
        pass

