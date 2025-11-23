from property import Property

class Studio(Property):
    def rental_type(self) -> str:
        return "Studio"
    
    def type_score(self) -> float:
        return 9

class Room(Property):
    def rental_type(self) -> str:
        return "Room"
    
    def type_score(self) -> float:
        return 6.5

class SharedHouse(Property):
    def rental_type(self) -> str:
        return "Shared House"
    
    def type_score(self) -> float:
        return 7

class Basement(Property):
    def rental_type(self) -> str:
        return "Basement"
    
    def type_score(self) -> float:
        return 8