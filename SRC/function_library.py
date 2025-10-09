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



#medium



#Complex
