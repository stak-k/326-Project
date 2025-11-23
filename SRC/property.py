from abc import ABC, abstractmethod
from formatter import format_address


class Property(ABC):
    def __init__(self, address: str, price: float, lease_term: str):
        self.address = format_address(address)
        self.price = float(price)
        self.lease_term = lease_term

    @abstractmethod
    def rental_type(self) -> str:
        """Return property type name( 'Studio', 'Room')"""
        pass

    @abstractmethod
    def type_score(self) -> float:
        """Return score based on property type"""
        pass

    def to_dict(self) -> dict:
        return{
            "Address": self.address,
            "Rent": self.price,
            "Lease Term": self.lease_term,
            "Property Type": self.rental_type(),
            "Type Score": self.type_score()
        }

    def __str__(self):
        return (f"{self.rental_type()} - {self.address} | {self.price} | Lease: {self.lease_term} ")