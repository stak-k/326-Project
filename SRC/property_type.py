from property import Property

class Studio(Property):
    """Represents a studio rental unit.
    Studio rentals typically offer a single-room layout, 
    and therefore receive a higher property type score.
    """
    def rental_type(self) -> str:
        """Return the type of rental."""
        return "Studio"
    
    def __init__(self, address, price, lease_term):
        """Initialize a Studio rental unit."""
        super().__init__(address, price, lease_term)
    
    def type_score(self) -> float:
        """Return type score for a studio layout."""
        return 9.0

class OneByOne(Property):
    """Represents a One bed, One Bath (Single Apartemnt)
    Typically Offers a One bed room, one bath, with a full kitchen and living room
    and is not shared. Therefore receive the Best property type score.
    """
    def rental_type(self) -> str:
        return "One Bed + One Bath"
    
    def __init__(self, address, price, lease_term):
        """Initialize a One Bed + One Bath"""
        super().__init__(address, price, lease_term)
    
    def type_score(self) -> float:
        """Return type score for a One Bed + One Bath"""
        return 10.0
    

class TwoByOne(Property):
    """Represents a Two bed, One Bath (Shared Apartment)
    Typically Offers a Two bed room, one bath, with a full kitchen and living room
    and is shared. Decrease few points for shared bathroom.
    """
    def rental_type(self) -> str:
        return "Two Bed + One Bath"
    
    def __init__(self, address, price, lease_term):
        """Initialize a Two Bed + One Bath"""
        super().__init__(address, price, lease_term)
    
    def type_score(self) -> float:
        """Return type score for a Two Bed + One Bath"""
        return 7.0
    
class TwoByTwo(Property):
    """Represents a Two bed, Two Bath (Shared Apartment)
    Typically Offers a Two bed room, Two bath, with a full kitchen and living room
    and is shared. Increase 1 point compared to Two by One for additional bathroom.
    """
    def rental_type(self) -> str:
        return "Two Bed + Two Bath"
    
    def __init__(self, address, price, lease_term):
        """Initialize a Two Bed + Two Bath"""
        super().__init__(address, price, lease_term)
    
    def type_score(self) -> float:
        """Return type score for a Two Bed + Two Bath"""
        return 8.0
    
class ThreeByTwo(Property):
    """3 Bed + 2 Bath (Shared Apartment)
    More roommates, but extra bathroom helps.
    Slightly lower overall desirability for students.
    """
    def rental_type(self) -> str:
        return "Three Bed + Two Bath"
    
    def __init__(self, address, price, lease_term):
        super().__init__(address, price, lease_term)
    
    def type_score(self) -> float:
        return 6.0


class ThreeByThree(Property):
    """3 Bed + 3 Bath (Shared Apartment)
    Every bedroom has its own bathroom. More privacy.
    Higher score than 3x2.
    """
    def rental_type(self) -> str:
        return "Three Bed + Three Bath"
    
    def __init__(self, address, price, lease_term):
        super().__init__(address, price, lease_term)
    
    def type_score(self) -> float:
        return 7.0


class FourByTwo(Property):
    """4 Bed + 2 Bath (Shared Apartment)
    High roommate count + shared bathrooms = lower score.
    """
    def rental_type(self) -> str:
        return "Four Bed + Two Bath"
    
    def __init__(self, address, price, lease_term):
        super().__init__(address, price, lease_term)
    
    def type_score(self) -> float:
        return 4.0


class FourByThree(Property):
    """4 Bed + 3 Bath
    Slightly better than 4x2 due to reduced bathroom sharing.
    """
    def rental_type(self) -> str:
        return "Four Bed + Three Bath"
    
    def __init__(self, address, price, lease_term):
        super().__init__(address, price, lease_term)
    
    def type_score(self) -> float:
        return 5.5


class FourByFour(Property):
    """4 Bed + 4 Bath (Popular UMD student layout)
    Every person gets their own bathroom.
    Better privacy but still lots of roommates.
    """
    def rental_type(self) -> str:
        return "Four Bed + Four Bath"
    
    def __init__(self, address, price, lease_term):
        super().__init__(address, price, lease_term)
    
    def type_score(self) -> float:
        return 6.0



class SharedHouse(Property):
    def rental_type(self) -> str:
        return "Shared House"
    
    def type_score(self) -> float:
        return 7.0

class Basement(Property):
    def rental_type(self) -> str:
        return "Basement"
    
    def type_score(self) -> float:
        return 8.5
    

class SingleApartment(Property):
    def rental_type(self) -> str:
        return "Single Apartment"
    
    def __init__(self, address, price, lease_term):
        """Initialize a Single Apartment"""
        super().__init__(address, price, lease_term)
    
    def type_score(self) -> float:
        return 10.0