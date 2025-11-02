#Import functions from the function_library file so this class can use them 
# handle text formattin and summary creation.
from function_library import(
     format_address,
     format_rent_display,
     format_listing_title,
     generate_listing_summary
)

class Formatter:
     """Handles text and display formating for rental listing"""
     
     def __init__(self, currency_symbol: str = "$", default_lease_term: str= "Month-to-month", ):
        """ 
            Sets up the basic settings for how the listing should look

            Args:
                currency_symbol(str): Default currency 
                default_lease_term (str): Lease term to use when none is provided
        """
        # Make sure both inputs are text and not empty.
        if not isinstance(currency_symbol, str) or not currency_symbol.strip():
            raise ValueError("Currency symbol must be a non-empty string.")
        if not isinstance(default_lease_term, str) or not default_lease_term.strip():
            raise ValueError("Default lease term must be non-empty string.")
            
        #Store the settings in private variables for later use 
        self._currency_symbol = currency_symbol.strip()
        self._default_lease_term = default_lease_term.strip()


    #Address Formating
     def format_address(self, address: str) -> str:
        """
        Use the function from function_library to clean and format an address.
        Makes sure spacing and capitalization look nice.
        """
        return format_address(address)

    #Listing Title Formatting (new)
     def format_listing_title(self,title: str) -> str:
         """ 
         Formats the rental title so 
         it looks clean and properly capitalized.
         """
         return format_listing_title(title)
             
    #Rent Display Formatting

     def format_rent_display(self, price: float, lease_term:str | None = None) -> str:
        """
        Formats the rent price so it looks professional.
        Example: turns 1500 into "$1,500 / month" or "$1,500 / year"
        depending on the lease term.

        """
        return format_rent_display(
            price,
            lease_term,
            currency_symbol = self._currency_symbol,  # Use the stored symbol 
            default_lease_term= self._default_lease_term # Use the stored default term
        )
     

    #Summary Listing
     def generate_listing_summary(self, title: str, price: float, address: str, score: float, lease_term: str | None = None,) -> str:
        """
        Creates a single summary line showing the most important info.
        Example:
        "🏠 Cozy Studio — $1,250 / month at 123 Main St, College Park, MD | Score: 9.1/10"
        """
        return generate_listing_summary(
            title,
            price,
            address,
            score, 
            lease_term
        )
     

     #Settings
     @property
     def settings(self) -> dict:
         """
            Shows the current formatting settings (like $ symbol and default lease term).
            Useful for checking what the class is using at the moment.
        """
         return {
            "currency_symbol": self._currency_symbol,
            "default_lease_term": self._default_lease_term
        }
     
     #String Representation
     def __str__(self) -> str:
        """
        When you print this object, it shows a short description
        of what settings are currently active.
        Example:
        Formatter(currency='$', default_lease_term='Month-to-month')
        """
        return (
            f"Formatter(currency='{self._currency_symbol}', "
            f"default_lease_term='{self._default_lease_term}')"
        )