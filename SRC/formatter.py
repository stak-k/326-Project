#Import functions from the function_library file so this class can use them 
# handle text formatting and summary creation.
from function_library import(
     format_address,
     format_rent_display,
     format_listing_title,
     generate_listing_summary
)

class Formatter:
     """
     Handles text and display formatting for rental listings

        Example:
            f = Formatter()
            f.format_rent_display(1500)
            '$1,500/month'
     """
     
     def __init__(self, currency_symbol: str = "$", default_lease_term: str= "Month-to-month", ):
        """ 
            Sets up the basic settings for how the listing should look

            Args:
                currency_symbol (str): Default currency symbol 
                default_lease_term (str): Lease term to use when none is provided
            
            Raises:
                ValueError: If inputs are empty or not strings.    
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

        Args:
            address (str): The address entered by the user.

        Returns:
            str: A formatted address (title-cased and properly spaced).

        Example:
            >>> f = Formatter()
            >>> f.format_address("123 main st, college park")
            '123 Main St, College Park'
        """
        return format_address(address)

    #Listing Title Formatting (new)
     def format_listing_title(self,title: str) -> str:
         """ 
         Formats the rental title so it looks clean and properly capitalized.

         Args:
            title (str): The title of the property.
        
         Returns:
            str: Cleaned and formatted title.

         Example:
            f = Formatter()
            f.format_listing_title("spacious apartment near umd")
            'Spacious Apartment Near Umd'
         """
         return format_listing_title(title)
             
    #Rent Display Formatting

     def format_rent_display(self, price: float, lease_term:str | None = None) -> str:
        """
        Formats the rent price so it looks professional and human-readable.

        Args:
            price(float): The rental price entered by the user.
            lease_term(str | None): Lease duration(optional).

        Returns: 
            str: A formatted rent string

        Example: 
            f = Formatter()
            f.format_rent_display(1800, "12 Month")
            '$1,800 / year'
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
        
        Args:
            title (str): Listing title.
            price (float): Rent price.
            address (str): Property address.
            score (float): Overall rental score (0–10).
            lease_term (str | None): Lease duration (optional).

        Returns:
            str: Combined summary string for display.

        Example:
            f = Formatter()
            f.generate_listing_summary("Cozy Studio", 1250, "123 Main St", 9.1)
            'Cozy Studio — $1,250 / month at 123 Main St | Score: 9.1/10'
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
        
        Returns:
            dict: The current currency symbol and default lease term.

        Example:
            f = Formatter()
            f.settings
            {'currency_symbol': '$', 'default_lease_term': 'Month-to-month'}
        """
         return {
            "currency_symbol": self._currency_symbol,
            "default_lease_term": self._default_lease_term
        }
     
     #String Representation
     def __str__(self) -> str:
        """
        Returns a readable summary of the formatter settings.

        Returns:
            str: Text showing the current currency and lease term.

        Example:
            f = Formatter()
            print(f)
            Formatter(currency='$', default_lease_term='Month-to-month')
        """
        return (
            f"Formatter(currency='{self._currency_symbol}', "
            f"default_lease_term='{self._default_lease_term}')"
        )