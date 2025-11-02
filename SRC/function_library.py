#15 functions in this library
#3 functions for each for now

# Installed for getting coordiantes for rental property entered
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderServiceError, GeocoderTimedOut
from geopy.distance import geodesic

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
        clean_address = " ".join(address.title().split())

        # Ensure the address is not empty after formatting
        if not clean_address:
            raise ValueError("Address cannot be empty.")
        
        for state in ["MD", "DC", "VA"]:
            clean_address = clean_address.replace(state.title(), state)

        return clean_address

# fromat listing title 
def format_listing_title(title: str) -> str:
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

# Converts numeric rent into formatted string like "$1,250 / month".
def format_rent_display(price: float, lease_term:str | None = None,
                        currency_symbol: str = "$", default_lease_term: str = "Month-to-month") -> str:
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
        
        term = lease_term or default_lease_term

        if term == "6 Month":
            suffix = " / 6 month"
        elif term == "12 Month":
            suffix = " / year"
        else: #default or unknown
            suffix = "/ month"
        
        return f"{currency_symbol}{price:,.0f} {suffix}"

# Utilities check
def check_utilities_included(is_included: bool) -> bool:
     """Return the toggle state for utilities inclusion.

     Args:
          is_included (bool): True if toggle is on (utilities included), 
                              False if off.
     
     Returns:
          bool: True if utilities are included, False otherwise.
     
     Raises:
          TypeError: If input is not boolean.
     
     Examples:   
               >>> check_utilities_included("True")
               True
               >>> check_utilities_included("False")
               False
     """

     if not isinstance(is_included, bool):
        raise TypeError("Input must be a boolean value (True or False).")
     
     return is_included

#listing title entered by the user is valid text 
#(not empty or non-string), and formats it consistently using title case
def validate_listing_title(title: str) -> str:
     """Validate and clean the listing title format.

     Args:
          title (str): The listing title provided by the user. 

     Returns:
          str: A cleaned and formatted version of the listing title.

     Raises:
          TypeError: If the title is not a string.
          ValueError: If the title is an empty string.

     Examples:   
          >>> validate_listing_title("spacious apartment near umd")
          'Spacious Apartment Near Umd'
          >>> validate_listing_title("  ")
          ValueError: Listing title cannot be empty.
          >>> validate_listing_title(12345)
          TypeError: Listing title must be a string.
          """
     
     # Type check
     if not isinstance(title, str):
          raise TypeError("Title must be a string.")
     
     # Clean and format the title (remove extra spaces + title case)
     clean_title = ' '.join(title.title().split())
     
     # Empty check after stripping spaces
     if not clean_title:
          raise ValueError("Title cannot be empty.")
     
     return clean_title


import re
def validate_email_contact(email: str) -> bool:
     """Validate the email contact format.

     Args:
          email (str): The email address to validate. 

     Returns:
          bool: True if the email is valid, False otherwise.

     Raises:
          TypeError: If the email is not a string.
          ValueError: If the email is an empty string or invalid format.

     Examples:   
               >>> validate_email_contact("")
               ValueError: Email cannot be empty.
               >>> validate_email_contact(12345)
               TypeError: Email must be a string.
               >>> validate_email_contact("invalid-email")
               ValueError: Invalid email format.
               >>> validate_email_contact("user@example.com")
               True
               """
     if not isinstance(email, str):
          raise TypeError("Email must be a string.")
     
     if not email.strip():
          raise ValueError("Email cannot be empty.")
     
     pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
     if not re.match(pattern, email.strip()):
          raise ValueError("Invalid email format.")
     return True

# Generate a formatted summary line for a property listing.
def generate_listing_summary(title: str, price: float, address: str, score: float, lease_term: str | None = None,) -> str:

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
        
        #Score validation (the system calcs score 
        #but this check helps catch unexpected futur bugs or out-of-range values )
        if not (0 <= score <= 10):
            raise ValueError("Scor must between 0 and 10")
            
            # Clean and format
        formatted_title = format_listing_title(title)
        formatted_address = format_address(address)
        formatted_price = format_rent_display(price, lease_term)

        
    
        # Build and return the summary string
        return f"{formatted_title} — {formatted_price} at {formatted_address} | Score: {score}/10"
   

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
def calculate_commute_time(distance: float, mode: str) -> float:
     """
     Estimate commute time in minutes based on distance and travel mode.
     
     Args:
          distance (float): Distance in miles.
          mode (str): Mode of transportation. Options: "walk", "bike", "drive", "bus".

     Returns:
          float: Estimated commute time in minutes.

     Raises:
          ValueError: If distance is negative or if no mode is selected.


     Examples:
          >>> calculate_commute_time(1.2, 'walk')
          24.0
          >>> calculate_commute_time(3, 'drive')
          7.2
     """

     if distance < 0:
          raise ValueError("Distance cannot be negative.")

     
     speeds = {
     'walk': 3,    # Average walking speed in mph}
     'bike': 10,   # Average biking speed in mph
     'drive': 25,  # Average driving speed in College Park
     'bus': 15     # Average bus speed in mph in College Park
     }
     
     mode = mode.lower()
     if mode not in speeds:
          raise ValueError(f"Mode of transportation must be selected (walk, bike, drive, or bus).")
     
     time_minutes = round((distance / speeds[mode]) * 60, 2)
     
     return time_minutes
   
# Calculate distance
def calculate_distance(start_address: str, end_address: str) -> float:
     """
     Calculate the distance in miles between 2 addresses using geopy
     
     Args:
          start_address (str): The starting address
          end_address (str): The end adress
          
     Returns:
          float: Distance in miles (rounded to 2 decimal places)

     Raises:
        TypeError: If either input is not a string.
        ValueError: If either address is empty or could not be geocoded.

     Examples:
        >>> calculate_distance("7303 Baltimore Ave, College Park, MD", "Edward St. John Learning Center, College Park, MD")
        1.25
          """
     
     start_coords = get_property_coordinates(start_address)
     end_coords = get_property_coordinates(end_address)

     # Calculate distance in miles
     miles = round(geodesic(start_coords, end_coords).miles, 2)


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

# Get the score for convenience based on proximity to amenities.
# def calculate_convenience_score()

#Complex

# Validate that the user has selected at least one class location from the defined options (up to a maximum of 5)
def validate_class_locations(selected: list[str], max_select: int = 5) -> list[str]:
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
         >>> validate_class_locations(["ESJ", "HBK", "KEY"])
        ['Esj', 'Hbk', 'Key']
        >>> validate_class_locations([])
        ValueError: At least one class location must be selected.
        >>> validate_class_locations(["ESJ", "HBK", "KEY", "MMH", "CCC", "TWS"])
        ValueError: No more than 5 class locations can be selected
     
     """
     building_options = ["ESJ", "HBK", "KEY", "MMH", "CCC", "TWS"]
     # Check if selected is none
     # Check if list is empty
     if selected is None or not selected:
          raise ValueError("At least one class location must be selected.")
     
     # Ensure no more than max_select locations are chosen
     if len(selected) > max_select:
          raise ValueError(f"No more than {max_select} class locations can be selected.")
     
     # Verify that all elemements are strings
     if not all(isinstance(loc, str) for loc in selected):
          raise TypeError("All class locations must be strings.")
     
     # Clean and return the list of selected locations
     cleaned_locations = []
     for loc in selected:
          loc = loc.strip().upper()
          if loc not in building_options:
               raise ValueError(f"Invalid class location selected: {loc}. Choose from {', '.join(building_options)}.")
          cleaned_locations.append(loc.title())
     # Return the cleaned list of locations
     return cleaned_locations



# Uses walking, driving, biking, and bus distance averages to compute an overall commute score.
def calculate_commute_score(distances: dict) -> float:
     """
     Calculate an overall commute score (0-10) based on average distances for each mode of transportation.

     Args:
          distances (dict): A dictionary containing avg distance (in miles) for each mode.
                            Example: {'walk': 0.8, 'bike': 1.5, 'drive': 3.2, 'bus': 2.7}

     Returns:
          float: Commute score between 0 and 10 (higher = better proximity).

     Raises:
          ValueError: If no valid modes are provided or distances are negative.
          

     Examples:
          >>> calculate_commute_score({'walk': 0.8, 'drive': 3.0})
          8.5
     """
     if not isinstance(distances, dict):
          raise TypeError("Distances must be provided as a dictionary.")
     
     if not distances:
          raise ValueError("Distances dictionary cannot be empty.")
     
     valid_modes = {'walk', 'bike', 'drive', 'bus'}
     total_score = 0
     count = 0

     for mode, dist in distances.items():
          if mode not in valid_modes:
               continue # Skip any modes not valid
          if dist < 0:
               raise ValueError(f"Distance for mode '{mode}' cannot be negative.")
          
          # Get commute time using our previously defined function
          time = calculate_commute_time(dist, mode)

          # Convert commute time → score (shorter = higher)
          # <10 min = 10 points, 10–30 min = scaled, >60 = 0
          if time <= 10:
               score = 10
          elif time >= 60:
               score = 0
          else:
               score = round(10 * (1 - (time - 10) / 50), 2)

          total_score += score
          count += 1

     if count == 0:
          raise ValueError("No valid transportation modes provided.")

     # Average the scores across all modes
     return round(total_score / count, 2)


# Combines weighted values of price, safety, commute, and flexibility into a single total score.
# def calculate_overall_rental_score()


# Saves rental and score info into CSV or database (integration + error handling).
# def update_rental_database(new_property_data)

def get_property_coordinates(address: str) -> tuple:
     """
     Get the latitude and longitude coordinates for a given address using geopy.
     Uses the Nominatim geocoding service to convert a formatted address into geographic coordinates.

     Args:
          address (str): The rental address to geocode.

     Returns:
          tuple[float, float]: A tuple containing (latitude, longitude).


     Raises:
          TypeError: If the address is not a string.
          ValueError: If the address is empty or could not be geocoded.
          GeocoderServiceError: If the geocoding service encounters an error.

     Examples:
          >>> get_property_coordinates("7303 Baltimore Ave, College Park, MD")
          (38.9786286, -76.937705)
          >>> get_property_coordinates("")
          ValueError: Address cannot be empty.
          >>> get_property_coordinates(12345)
          TypeError: Address must be a string.
     """

     # Validate input
     if not isinstance(address, str):
          raise TypeError("Address must be a string.")
     
     # Clean up address using exsisting function
     clean_address = format_address(address)

     if not clean_address:
          raise ValueError("Address cannot be empty.")
     
     # Initialize Nominatim geocoder
     geolocator = Nominatim(user_agent="rental_hunters")

     try:
          location = geolocator.geocode(clean_address, timeout = 10)
     except (GeocoderServiceError, GeocoderTimedOut) as e:
          raise ConnectionError(f"Geocoding service error: {e}")
     
     if location is None:
          raise ValueError("Could not provide coordinates for the provided address.")
     
     return (location.latitude, location.longitude)
