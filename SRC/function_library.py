#15 functions in this library
#3 functions for each for now


#simple

def validate_rental_address(address):
   """Validate the rental address format.
    Args:
         address (str): The rental address to validate. 

    Returns:
         bool: True if the address is valid, False otherwise.

    Raises:
         TypeError: If the address is not a string.
         ValueError: If the address is an empty string.

    Examples:   
            >>> validate_rental_address("123 Main St, Springfield, IL 62701")
            True
            >>> validate_rental_address("")
            Traceback (most recent call last):
            ...
            ValueError: Address cannot be empty.
            >>> validate_rental_address(12345)
            Traceback (most recent call last):
            ...
            TypeError: Address must be a string.
    """
   # Simple validation checks
   #Type check
   if not isinstance(address, str):
        raise TypeError("Address must be a string.")
   
   # Empty check
   if not address.strip():
        raise ValueError("Address cannot be empty.")
   
   return True

def validate_rent_input(price):
    """Validate the rent input format, need positive number.
    Args:
         price (float): The monthly rent entered by the user. 

    Returns:
         bool: True if the price is valid - positive -, False otherwise.

    Raises:
         TypeError: If the price is not a float or int.
         ValueError: If the price is negative, price <= 0.

    Examples:   
            >>> validate_rent_input(1200.50)
            True
            >>> validate_rent_input(-500)
            Traceback (most recent call last):
            ...
            ValueError: Rent price cannot be negative.
            >>> validate_rent_input("1000")
            Traceback (most recent call last):
            ...
            TypeError: Rent price must be a number.
    """
    #Type check
    if not isinstance(price, (int, float)):
        raise TypeError("Rent price must be a number.")
    
    # Negative check
    if price <= 0:
        raise ValueError("Rent price cannot be negative or equal to zero.")
    
    return True

# Ensure the Zipcode is valid and properly formated
def validate_zipcode(zipcode: str) -> bool:
    """Validate the zipcode format.
    Args:
         zipcode (str): The zipcode to validate. 

    Returns:
         bool: True if the zipcode is valid, Otherwise raises ValueError.

     Raises:
          ValueError: If the ZIP code is not exactly 5 digits or contains non-numeric characters

     Example:
          >>> validate_zip_code("20740")
          True
          >>> validate_zip_code("abcde")
          ValueError: Zipcode must be 5 digits.
          
     
    """
    # Length and digit check
    if len(zipcode) != 5 or not zipcode.isdigit():
        raise ValueError("Zipcode must be 5 digits.")
    
    return True


def format_address(address: str) -> str:
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
     clean_address = ' '.join(address.title().split())

     # Ensure the address is not empty after formatting
     if not clean_address:
          raise ValueError("Address cannot be empty.")
     
     
     
     return clean_address


#medium



#Complex
