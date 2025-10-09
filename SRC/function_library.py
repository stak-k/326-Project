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
         ValueError: If the address is not a string or is empty.
    Examples:   
            >>> validate_rental_address("123 Main St, Springfield, IL 62701")
            True
            >>> validate_rental_address("")
            False
            >>> validate_rental_address(12345)
            Traceback (most recent call last):
    """
   # Simple validation: check if address is a non-empty string

    if not isinstance(address, str) or not address.strip():
        raise ValueError("Address must be a non-empty.")
    return True



#medium



#Complex
