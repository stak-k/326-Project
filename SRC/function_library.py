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

# Format the address entered by user for consistency (title case, remove extra spaces)
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

# Calculate a flexibility score based on the lease term of rental property.
def calculate_flexibilty_score(lease_term: str) -> int:
     """
     Calculate a flexibility score based on the lease term of rental property.

     Args:
           lease_term (str): The lease term option chosen by the user. 
                              Options: "Month-to-Month", "6 Months", "12 Months"
     
     Returns:
           int: A score between 4 and 10, where higher scores indicate more flexibility.
     
     Raises:
           ValueError: If no option is selected or if the option is invalid.
     
     Examples:   
               >>> calculate_flexibilty_score("Month-to-Month")
               10
               >>> calculate_flexibilty_score("6 Months")
               7
               >>> calculate_flexibilty_score("12 Months")
               4
               >>> calculate_flexibilty_score("")
               ValueError: No lease term was selected. Choose from 'Month-to-Month', '6 Months', or '12 Months'.
     """
     # Predefined flexibility options and their corresponding scores
     flexibility_options = {
          "Month-to-Month": 10,
          "6 Months": 7,
          "12 Months": 4,
     }

     # Validate input
     if not lease_term:
          raise ValueError("No lease term was selected. Choose from 'Month-to-Month', '6 Months', or '12 Months'.")

     return flexibility_options[lease_term]

# Converts numeric rent into formatted string like "$1,250 / month".
# def format_rent_display():


#medium

# Calculate a price score (1-10) based on the rental price compared to the average rent.
def calculate_price_score(price: float, average_price: float) -> float:
     """
     Calculate a price score (1-10) based on the rental price compared to the average rent.
     
     Higher scores = better value (lower price compared to average).

     Args:
            price (float): The monthly rent entered by the user.
            average_price (float): The average rental price for similar properties in College Park.
     
     Returns:
            float: A score between 0 and 10, where higher scores indicate better value.
     
     Raises:
            TypeError: If either price or average_price is not a float or int.
            ValueError: If either price or average_price is negative or zero.
     
     Examples:   
                 >>> calculate_price_score(1200, 1500)
                 8.0
                 >>> calculate_price_score(4500, 1500)
                 0.0
                 >>> calculate_price_score(-500, 1500)
                 ValueError: Price and average price must be positive numbers.
                 >>> calculate_price_score(1200, "1500")
                 TypeError: Price and average price must be numbers.
     """
     #Type check
     if not isinstance(price, (int, float)) or not isinstance(average_price, (int, float)):
          raise TypeError("Price and average price must be numbers.")
     
     # Negative check
     if price <= 0 or average_price <= 0:
          raise ValueError("Price and average price must be positive numbers.")
     
     # Scoring Logic
     ratio = price / average_price

     if ratio <= 0.5: # 50% or less of average price
          score = 10.0
     elif ratio >= 3.0: # 300% above average price
          score = 0.0
     else:
          score = round(10 * (1.5 - ratio), 2) # Linear scale for score between 0.5x and 3x the average price


     return score
     
# Produces a normalized score (higher = safer).  
# def calculate_safety_score(crime_rate: float, avg_crime_rate: float)

# Converts miles → estimated minutes based on travel mode (“walk”, “bike”, “drive”, “bus”).
# def calculate_commute_time(distance: float, mode: str)




#Complex

# Validate that the user has selected at least one class location from the defined options (up to a maximum of 5)
def validate_class_locations(selected, max_select: int = 5) -> list[str]:
     """
     Validate that the user has selected at least one class location
     from the defined options (up to a maximum of 5)
     
     Args:
          selected (list[str]): List of class locations selected by the user.
          max_select (int): Maximum number of locations that can be selected. Default is 5.

     Returns:
          list[str]: A cleaned list of valid class locations selected by the user.

     Raises:
          ValueError: If no locations are selected or more than `max_select` are chosen.

     Examples:
          >>> validate_class_locations(["CP", "UMD"])
          ['CP', 'UMD']
          >>> validate_class_locations([])
          ValueError: At least one class location must be selected.
          >>> validate_class_locations(["CP", "UMD", "PGC", "DC", "VA", "NY"])
          ValueError: No more than 5 class locations can be selected.
     
     """
     # Check if selected is none
     if selected is None:
          raise ValueError("At least one class location must be selected.")
     # Check if list is empty
     if not selected:
          raise ValueError("At least one class location must be selected.")
     # Ensure no more than max_select locations are chosen
     if len(selected) > max_select:
          raise ValueError(f"No more than {max_select} class locations can be selected.")
     
     # Verify that all elemements are strings
     if not all(isinstance(loc, str) for loc in selected):
          raise TypeError("All class locations must be strings.")
     
     # Clean and return the list of selected locations
     cleaned_locations = [loc.strip().title() for loc in selected if loc.strip()]

     # Return the cleaned list of locations
     return cleaned_locations



# Uses walking, driving, biking, and bus distance averages to compute an overall commute score.
# def calculate_commute_score()


# Combines weighted values of price, safety, commute, and flexibility into a single total score.
# def calculate_overall_rental_score()


# Saves rental and score info into CSV or database (integration + error handling).
# def update_rental_database(new_property_data)

