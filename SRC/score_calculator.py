# calculate price score, commute score, etc

from rental_property import RentalProperty


from function_library import (
    calculate_price_score,
    calculate_commute_score,
    calculate_flexibilty_score
)

from property import Property

class ScoreCalculator:
    """ 
    Calculates different category scores and combines them into and overall score
    
    This class integrates price, commute, and lease flexibility scores
    to generate a final weighted overall score. Future extensions goingto include
    convenience and crime safety metrics.
    """

    def __init__(self, average_price: float = 1500.0):
        """ Initialize with default average rent score 
        Args:
            average_price (float): Average rent price for comparison actuall rent price.
            default is 1500.0
        """
        self._average_price = float(average_price)
    
    # Type score (polymorphic)
    def property_type_score(self, property_obj: Property) -> float:
        return property_obj.type_score()

    # Price Score
    def price_score(self, price: float) -> float:
        """ Calculate price score based on rent and average price 
        Args:
            price (float): Actual rent price.
        Returns:
            float: Price score between 0 and 10.
        """
        return calculate_price_score(price, self._average_price)
    
    # Lease Flexibility Score
    def flexibility_score(self, lease_term: int) -> float:
        """ Calculate lease flexibility score based on lease type 
        
        Args:
            lease_term (int): Lease term in months(6,12).
        Returns:
            float: Flexibility score between 0 and 10 based on how flexible or rigid.
        """
        # Convert 6 -> "6 Months", 12 -> "12 Months"
        if lease_term == 6:
            term_str = "6 Months"
        elif lease_term == 12:
            term_str = "12 Months"
        else:
            term_str = "Month-to-Month"  # fallback or future use

        return calculate_flexibilty_score(term_str)
    
    # Commute Score
    def commute_score(self, distances: dict) -> float:
        """ Calculate commute score based on commute time in minutes 
        
        Args:
            distances (dict): Dictionary of commute durations times in minutes
            for various modes or destinations.
        Returns:
            float: Commute score between 0 and 10.
        """
        return calculate_commute_score(distances)
    

    # NEW: clean, object-driven overall score uses composition + inheritance + polymorphism
    def overall_score(self, rental: RentalProperty) -> float:
        """Calculate weighted overall score using rental object attributes.
        Args:
            price (float): Actual rent price.
            lease_term (int): Lease term in months.
            distances (dict): Dictionary of commute for targeted destination.
            type (float): Score based on property type
        Returns:
            float: Overall score between 0 and 10."""

        price_s = self.price_score(rental.rent)
        flex_s = self.flexibility_score(rental.lease_term)
        commute_s = self.commute_score(rental.distances)
        type_s = rental.property_type_obj.type_score() # ploymorphic call

        weights = {
            'price': 0.5,
            'flexibility': 0.2,
            'commute': 0.3,
            'type': 0.1
        }


        overall = (
            price_s * weights['price'] +
            flex_s * weights['flexibility'] +
            commute_s * weights['commute'] +
            type_s * weights['type']
        )

        return round(overall, 2)






