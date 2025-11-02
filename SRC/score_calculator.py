# calculate price score, commute score, future crime score, etc

from function_library import (
    calculate_price_score,
    calculate_commute_score,
    calculate_flexibilty_score
)

class ScoreCalculator:
    """ Calculates different category scores and combines them into and overall score"""

    def __init__(self, average_price: float = 1500.0):
        """ Initialize with default average rent score """
        self._average_price = float(average_price)

    # Price Score
    def price_score(self, price: float) -> float:
        """ Calculate price score based on rent and average price """
        return calculate_price_score(price, self._average_price)
    
    # Lease Flexibility Score
    def flexibility_score(self, lease_term: int) -> float:
        """ Calculate lease flexibility score based on lease type """
        return calculate_flexibilty_score(lease_term)
    
    # Commute Score
    def commute_score(self, distances: dict) -> float:
        """ Calculate commute score based on commute time in minutes """
        return calculate_commute_score(distances)
    
    # Covenience Score

    # Crime Score


    # Overall Score
    def overall_score(self, price: float, lease_term: int, distances: dict) -> float:
        """ Calculate overall score as weighted average of individual scores """
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




