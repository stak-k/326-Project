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
        """
        Format an address string for consistency (title case, remove extra spaces).

        Args:
            address (str): The rental address to format. 
        
        Returns:
            str: A formatted address string with proper capitalization and spacing.
        
        Raises:
            TypeError: If the address is not a string.
            ValueError: If the address is an empty string.
        
        Examples:   
                >>> format_address("123 main st, college park ")
                '123 Main St, College Park'
                >>> format_address("  ")
                ValueError: Address cannot be empty.
                >>> format_address(12345)
                TypeError: Address must be a string.
        """

        # Validate correct data type
        if not isinstance(address, str):
            raise TypeError("Address must be a string.")
        
        # Basic formatting: title case and strip extra spaces
        clean_address = " ".join(address.title().split())

        # Ensure the address is not empty after formatting
        if not clean_address:
            raise ValueError("Address cannot be empty.")
        
        for state in ["MD", "DC", "VA"]:
            clean_address = clean_address.replace(state.title(), state)

        return clean_address

    #---------
    #listing title formetter (new)
    #-------
     def format_listing_title(self,title: str) -> str:
         """
         Formats the rental listing title for display consistency.

         Args: 
            title(str): The listing title or property name 

         Returns: 
            str: title-cased and cleaned title string

         Raises:
            TypeError: If titile is not string
            ValueError: If title is empty

         Exmp:
            format_listing_title(" 123 college park rd")
            '123 College Park Rd'
         """
         if not isinstance(title, str):
             raise TypeError("Title must be string.")
         
         clean_title = " ".join(title.title().split())

         if not clean_title:
             raise ValueError("Title cannot be empty.")
         
         return clean_title
             
    #----------
    #rent display (formated)
    #-------

     def format_rent_display(self, price: float, lease_term:str | None = None) -> str:
        """
        Convert numeric rent into formatted string depend on lease term.

        Args:
            price (float): The monthly rent entered by the user.
            lease_term(str| None): The selected lease term.
                If none use default lease term 
        
        Returns:
            str: Formatted rent string.
        
        Raises:
            TypeError: If price is not a float or int.
            ValueError: If price is negative or zero.
        
        Examples:   
                >>> format_rent_display(1250)
                '$1,250 / month'
                >>> format_rent_display(-500)
                ValueError: Rent price must be a positive number.
                >>> format_rent_display("1000")
                TypeError: Rent price must be a number.
        """
        #Type check
        if not isinstance(price, (int, float)):
            raise TypeError("Rent price must be a number.")
        
        # Negative check
        if price <= 0:
            raise ValueError("Rent price must be a positive number.")
        
        term = lease_term or self._default_lease_term

        if term == "6 Month":
            suffix = " / 6 month"
        elif term == "12 Month":
            suffix = " / year"
        else: #default or unknown
            suffix = "/ month"
        
        return f"{self._currency_symbol}{price:,.0f} {suffix}"
     
    #--------
    #summary listing
    #-----
     def generate_listing_summary(self, title: str, price: float, address: str, score: float, lease_term: str | None = None,) -> str:

        """
        Generate a formatted summary line for a property listing.

        Args:
            title (str): The listing title provided by the user.
            price (float): The rent price for the property.
            lease_term(str): works with price display termly deal
            address (str): The property address.
            score (float): The computed overall rental score (0-10).

        Returns:
            str: A formatted summary string combining the title, price, address, and score.

        Raises:
            TypeError: If title or address is not a string, or if price/score are not numeric.
            ValueError: If any field is empty or invalid.

        Examples:
            >>> generate_listing_summary("Spacious Apartment Near UMD", 1450, "7303 Baltimore Ave, College Park, MD", 8.7)
            '🏠 Spacious Apartment Near Umd — $1,450 / month at 7303 Baltimore Ave, College Park, Md | Score: 8.7/10'
            >>> generate_listing_summary("", 1450, "7303 Baltimore Ave", 8.7)
            ValueError: Listing title cannot be empty.
            >>> generate_listing_summary("Luxury Loft", "1400", "123 Main St", 9)
            TypeError: Price must be numeric.
        """

        # Type validation
        if not isinstance(title, str) or not isinstance(address, str):
            raise TypeError("Title and address must be strings.")
        if not isinstance(price, (int, float)) or not isinstance(score, (int, float)):
            raise TypeError("Price and score must be numeric.")
        
        # Empty validation
        if not title.strip():
            raise ValueError("Listing title cannot be empty.")
        if not address.strip():
            raise ValueError("Address cannot be empty.")
            
            # Clean and format
        formatted_title = self.format_listing_title(title)
        formatted_address = self.format_address(address)
        formatted_price = self.format_rent_display(price, lease_term)

        #Score validation (the system calcs score 
        #but this check helps catch unexpected futur bugs or out-of-range values )
        if not (0 <= score <= 10):
            raise ValueError("Scor must between 0 and 100")
    
        # Build and return the summary string
        summary = (f"{formatted_title} — {formatted_price} at {formatted_address} | Score: {score}/10")
        return summary
     
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