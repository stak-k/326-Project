# calculate price score, commute score, future crime score, etc

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
        return calculate_flexibilty_score(str(lease_term))
    
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
    
    # Covenience Score

    # Crime Score


    # Overall Score
    def overall_score(self, price: float, lease_term: int, distances: dict) -> float:
        """ Calculate overall score as weighted average of individual scores
        Args:
            price (float): Actual rent price.
            lease_term (int): Lease term in months.
            distances (dict): Dictionary of commute for targeted destination.
        Returns:
            float: Overall score between 0 and 10.
        """
        price_s = self.price_score(price)
        flex_s = self.flexibility_score(lease_term)
        commute_s = self.commute_score(distances)

        # Weights for each score component
        weights = {
            'price': 0.5,
            'flexibility': 0.2,
            'commute': 0.3
        }

        overall = (price_s * weights['price'] +
                   flex_s * weights['flexibility'] +
                   commute_s * weights['commute'])
        
        return overall




