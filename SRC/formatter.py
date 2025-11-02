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
            Args:
                currency_symbol(str): defult currency 
                defult_lease_term (str): Lease term to use when none is provided
        """
        if not isinstance(currency_symbol, str) or not currency_symbol.strip():
            raise ValueError("Currency symbol must be a non-empty string.")
        if not isinstance(default_lease_term, str) or not default_lease_term.strip():
            raise ValueError("Defult lease term must be non-empty string.")
            
        self._currency_symbol = currency_symbol.strip()
        self._default_lease_term = default_lease_term.strip()

#----------
#Address Formating
#-----------
     def format_address(self, address: str) -> str:
        return format_address(address)

    #---------
    #listing title formetter (new)
    #-------
     def format_listing_title(self,title: str) -> str:
         return format_listing_title(title)
             
    #----------
    #rent display (formated)
    #-------

     def format_rent_display(self, price: float, lease_term:str | None = None) -> str:
        return format_rent_display(
            price,
            lease_term,
            currency_symbol = self._currency_symbol,
            default_lease_term= self._default_lease_term
        )
     
    #--------
    #summary listing
    #-----
     def generate_listing_summary(self, title: str, price: float, address: str, score: float, lease_term: str | None = None,) -> str:
        return generate_listing_summary(
            title,
            price,
            address,
            score, 
            lease_term
        )
     #------
     #settings
     #-----
     @property
     def settings(self) -> dict:
         """Return current formatte as a dictionary."""
         
         return {
            "currency_symbol": self._currency_symbol,
            "default_lease_term": self._default_lease_term
        }
     #-------
     #String reps
     #-----
     def __str__(self) -> str:
        """
         Readable description of formatter setting .
         """
        return (
            f"Formatter(currency='{self._currency_symbol}', "
            f"default_lease_term='{self._default_lease_term}')"
        )