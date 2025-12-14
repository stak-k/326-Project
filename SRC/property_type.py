from property import Property

# ------------------
# Studio Apartment
# ------------------
class Studio(Property):
    """Represents a studio rental unit.
    
    Studio apartments usually consist of a single open space combining bedroom, 
    living area, and kitchen. Because they
    are private and not shared, they receive a relatively high
    property type score.
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

# -------------------
# One Bed + One Bath 
# -------------------
class OneByOne(Property):
    """Represents a One bed, One Bath (Single Apartemnt)
    Typically Offers a One bed room, one bath, with a full kitchen and living room
    and is not shared. Therefore receive the Best property type score.
    """
    def rental_type(self) -> str:
        """Return the type of rental as a descriptive string."""
        return "One Bed + One Bath"
    
    def __init__(self, address, price, lease_term):
        """Initialize a One Bed + One Bath"""
        super().__init__(address, price, lease_term)
    
    def type_score(self) -> float:
        """Return type score for a One Bed + One Bath"""
        return 10.0
    

# -------------------
# Two Bed + One Bath 
# -------------------
class TwoByOne(Property):
    """Represents a Two bed, One Bath (Shared Apartment)
    Typically Offers a Two bed room, one bath, with a full kitchen and living room
    and is shared. Decrease few points for shared bathroom.
    """
    def rental_type(self) -> str:
        """Return the type of rental as a descriptive string."""
        return "Two Bed + One Bath"
    
    def __init__(self, address, price, lease_term):
        """Initialize a Two Bed + One Bath"""
        super().__init__(address, price, lease_term)
    
    def type_score(self) -> float:
        """Return type score for a Two Bed + One Bath"""
        return 7.0

# -------------------
# Two Bed + Two Bath 
# -------------------   
class TwoByTwo(Property):
    """Represents a Two bed, Two Bath (Shared Apartment)
    Typically Offers a Two bed room, Two bath, with a full kitchen and living room
    and is shared. Increase 1 point compared to Two by One for additional bathroom.
    """
    def rental_type(self) -> str:
        """Return the type of rental as a descriptive string."""
        return "Two Bed + Two Bath"
    
    def __init__(self, address, price, lease_term):
        """Initialize a Two Bed + Two Bath"""
        super().__init__(address, price, lease_term)
    
    def type_score(self) -> float:
        """Return type score for a Two Bed + Two Bath"""
        return 8.0

# -------------------
# Three Bed + Two Bath 
# -------------------  
class ThreeByTwo(Property):
    """3 Bed + 2 Bath (Shared Apartment)
    More roommates, but extra bathroom helps.
    Slightly lower overall desirability for students.
    """
    def rental_type(self) -> str:
        """Return the type of rental as a descriptive string."""
        return "Three Bed + Two Bath"
    
    def __init__(self, address, price, lease_term):
        """Initialize the subclass by calling the parent class constructor with address, price, and lease term."""
        super().__init__(address, price, lease_term)
    
    def type_score(self) -> float:
        return 6.0

# -------------------
# Three Bed + Three Bath 
# -------------------
class ThreeByThree(Property):
    """3 Bed + 3 Bath (Shared Apartment)
    Every bedroom has its own bathroom. More privacy.
    Higher score than 3x2.
    """
    def rental_type(self) -> str:
        """Return the specific rental type label for this unit."""
        return "Three Bed + Three Bath"
    
    def __init__(self, address, price, lease_term):
        """Initialize with address, monthly price, and lease duration."""
        super().__init__(address, price, lease_term)
    
    def type_score(self) -> float:
        return 7.0

# -------------------
# Four Bed + Two Bath
# -------------------
class FourByTwo(Property):
    """4 Bed + 2 Bath (Shared Apartment)
    High roommate count + shared bathrooms = lower score.
    """
    def rental_type(self) -> str:
        """Return the rentals type label."""
        return "Four Bed + Two Bath"
    
    def __init__(self, address, price, lease_term):
        """Initialize the rental by forwarding core attributes to the base class."""
        super().__init__(address, price, lease_term)
    
    def type_score(self) -> float:
        return 4.0

# -------------------
# Four Bed + Three Bath
# -------------------
class FourByThree(Property):
    """4 Bed + 3 Bath
    Slightly better than 4x2 due to reduced bathroom sharing.
    """
    def rental_type(self) -> str:
        """Return the rentals type description."""
        return "Four Bed + Three Bath"
    
    def __init__(self, address, price, lease_term):
        """Initialize the rental with its address, price, and lease term."""
        super().__init__(address, price, lease_term)
    
    def type_score(self) -> float:
        """Return the numeric score representing this rental type."""
        return 5.5

# -------------------
# Four Bed + Four Bath
# -------------------
class FourByFour(Property):
    """4 Bed + 4 Bath (Popular UMD student layout)
    Every person gets their own bathroom.
    Better privacy but still lots of roommates.
    """
    def rental_type(self) -> str:
        """Return the descriptive label for this rental type."""
        return "Four Bed + Four Bath"
    
    def __init__(self, address, price, lease_term):
        """Initialize the rental by forwarding core attributes to the base class."""
        super().__init__(address, price, lease_term)
    
    def type_score(self) -> float:
        return 6.0

# -------------------
# Shared House
# -------------------
class SharedHouse(Property):
    def rental_type(self) -> str:
        """Returns the string label for this rental type ('Shared House')."""
        return "Shared House"
    
    def type_score(self) -> float:
        """Returns the numerical score representing this rental type (7.0)."""
        return 7.0

# ------------------- 
# Basement Apartment
# -------------------
class Basement(Property):
    def rental_type(self) -> str:
        """Returns the rental type label 'Basement'."""
        return "Basement"
    
    def type_score(self) -> float:
        """Returns an 8.5 desirability score for this rental type."""
        return 8.5
    
# -------------------
# Single Apartment
# -------------------
class SingleApartment(Property):
    def rental_type(self) -> str:
        return "Single Apartment"
    
    def __init__(self, address, price, lease_term):
        """Initialize a Single Apartment"""
        super().__init__(address, price, lease_term)
    
    def type_score(self) -> float:
        return 10.0
