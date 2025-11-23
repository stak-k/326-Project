from property import Property

class Studio(Property):
    def rental_type(self):
        return "Studio"
    
    def type_score(self):
        return 9

class Room(Property):
    def rental_type(self):
        return "Room"
    
    def type_score(self):
        return 6.5

class SharedHouse(Property):
    def rental_type(self):
        return "Shared House"
    
    def type_score(self):
        return 7

class Basement(Property):
    def rental_type(self):
        return "Basemente"
    
    def type_score(self):
        return 8