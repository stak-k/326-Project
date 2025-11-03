# Usage Examples

This document demonstrates how to use and how to use and test the functions in the ** Rental Hunters Function Library **.

Each example below shows expected outputs and common error cases.


```python
=== Simple functions test ===
✅ validate_rental_address('123 Main St, Springfield, IL 62704',) → True
❌ validate_rental_address('',) → ValueError: Address cannot be empty.
✅ validate_rent_input(1500,) → True
❌ validate_rent_input(-1500,) → ValueError: Rent price cannot be negative or equal to zero.
❌ validate_rent_input('1500',) → TypeError: Rent price must be a number.
❌ validate_rent_input('1500',) → TypeError: Rent price must be a number.
✅ validate_zipcode('62704',) → True
❌ validate_zipcode('abcde',) → ValueError: Zipcode must be 5 digits.
❌ validate_zipcode('627',) → ValueError: Zipcode must be 5 digits.
✅ format_address('123 main st, college park 62704',) → 123 Main St, College Park 62704
❌ format_address('',) → ValueError: Address cannot be empty.
❌ format_address(62704,) → TypeError: Address must be a string.
✅ format_rent_display(1250,) → $1,250 / month
❌ format_rent_display(-1250,) → ValueError: Rent price must be a positive number.
❌ format_rent_display('1250',) → TypeError: Rent price must be a number.
✅ check_utilities_included(True,) → True
✅ check_utilities_included(False,) → False
✅ validate_listing_title('spacious apartment near umd',) → Spacious Apartment Near Umd
❌ validate_listing_title('  ',) → ValueError: Title cannot be empty.
❌ validate_listing_title(12345,) → TypeError: Title must be a string.
✅ validate_email_contact('user@example.com',) → True
❌ validate_email_contact('',) → ValueError: Email cannot be empty.
❌ validate_email_contact(12345,) → TypeError: Email must be a string.
❌ validate_email_contact('invalid-email',) → ValueError: Invalid email format.
✅ generate_listing_summary('Spacious Apartment Near UMD', 1450, '7303 Baltimore Ave, College Park, MD', 8.7) → 🏠 Spacious Apartment Near Umd — $1,450 / month at 7303 Baltimore Ave, College Park, Md | Score: 8.7/10
❌ generate_listing_summary('', 1450, '7303 Baltimore Ave, College Park, MD', 8.7) → ValueError: Listing title cannot be empty.
❌ generate_listing_summary('Luxury Loft', '1400', '123 Main St', 9) → TypeError: Price and score must be numeric.
❌ generate_listing_summary('Cozy Studio', 1300, '', 8.2) → ValueError: Address cannot be empty.
❌ generate_listing_summary('Modern Apartment', 1800, '4500 Knox Rd, College Park, MD', 'ten') → TypeError: Price and score must be numeric.

=== Medium Functions Test ===
✅ calculate_price_score(1200, 1500) → 7.0
✅ calculate_price_score(4500, 1500) → 0.0
❌ calculate_price_score(-1200, 1500) → ValueError: Price and average price must be positive numbers.
❌ calculate_price_score('1200', 1500) → TypeError: Price and average price must be numbers.
✅ calculate_commute_time(3, 'drive') → 7.2
✅ calculate_commute_time(5, 'bike') → 30.0
❌ calculate_commute_time(-2, 'walk') → ValueError: Distance cannot be negative.
❌ calculate_commute_time(3, 'fly') → ValueError: Mode of transportation must be selected (walk, bike, drive, or bus).
✅ calculate_flexibilty_score('Month-to-Month',) → 10
❌ calculate_flexibilty_score('',) → ValueError: No lease term was selected. Choose from 'Month-to-Month', '6 Months', or '12 Months'.
❌ calculate_flexibilty_score('6Month',) → KeyError: '6Month'

=== Complex Functions Test ===
✅ validate_class_locations(['ESJ', 'HBK', 'KEY'],) → ['Esj', 'Hbk', 'Key']
❌ validate_class_locations([],) → ValueError: At least one class location must be selected.
❌ validate_class_locations(['ESJ', 'HBK', 'KEY', 'MMH', 'CCC', 'TWS'],) → ValueError: No more than 5 class locations can be selected.
✅ calculate_commute_score({'walk': 10, 'bike': 20, 'drive': 5},) → 3.2
❌ calculate_commute_score({'walk': -10, 'bike': 20, 'drive': 5},) → ValueError: Distance for mode 'walk' cannot be negative.

=== Geocoding Function Test ===
❌ get_property_coordinates('7303 Baltimore Ave, College Park, MD',) → ConnectionError: Geocoding service error: HTTPSConnectionPool(host='nominatim.openstreetmap.org', port=443): Max retries exceeded with url: /search?q=7303+Baltimore+Ave%2C+College+Park%2C+Md&format=json&limit=1 (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1032)')))
❌ get_property_coordinates(' ',) → ValueError: Address cannot be empty.
❌ get_property_coordinates('1234 Nowhere Land XYZ',) → ConnectionError: Geocoding service error: HTTPSConnectionPool(host='nominatim.openstreetmap.org', port=443): Max retries exceeded with url: /search?q=1234+Nowhere+Land+Xyz&format=json&limit=1 (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1032)')))


=== CLASS TESTS ===
=== CLASS TESTS ===

=== Formatter Class Tests===
✅ Format Address: 123 Main St, College Park, MD
❌ Invalid Address (empty): ValueError - Address cannot be empty.
❌ Invalid Address (number): TypeError - Address must be a string.
✅ Format Title: Spacious Apartment Near Umd
❌ Invalid Title (empty): ValueError - Title cannot be empty.
✅ Format Rent Display (default term): $1,450 / month
✅ Format Rent Display (custom term): $1,800 / month
❌ Invalid Rent (negative): ValueError - Rent price must be a positive number.
❌ Invalid Rent (string price): TypeError - Rent price must be a number.
✅ Generate Summary: Cozy Studio — $1,250 / month at 123 Main St, College Park, MD | Score: 9.1/10
❌ Invalid Summary (missing address): ValueError - Address cannot be empty.
❌ Invalid Summary (wrong score type): TypeError - Price and score must be numeric.
✅ Settings Property: {'currency_symbol': '$', 'default_lease_term': 'Month-to-month'}
✅ String Representation: Formatter(currency='$', default_lease_term='Month-to-month')


=== Validator  Class Test ===
✅ Valid Address: True
❌ Invalid Address (empty): ValueError - Address cannot be empty.
❌ Invalid Address (number): TypeError - Address must be a string.
✅ Valid Rent: True
❌ Invalid Address (number): TypeError - Address must be a string.
❌ Invalid Rent (negative): ValueError - Rent price cannot be negative or equal to zero.
❌ Invalid Rent (string): TypeError - Rent price must be a number.
✅ Valid ZIP: True
❌ Invalid ZIP (too short): ValueError - Zipcode must be 5 digits.
✅ Valid Title: Spacious Apartment Near Umd
❌ Invalid Title (empty): ValueError - Title cannot be empty.
✅ Valid Email: True
❌ Invalid Email (no @): ValueError - Invalid email format.
✅ Valid Class Locations: ['Esj', 'Hbk', 'Key']
❌ Invalid Locations (too many): ValueError - No more than 5 class locations can be selected.
✅ String Representation: Validator(active: address, rent, zip, title, email, class locations)

=== PropertyManager Class Tests ===
✅ Add Valid Property: {'Title': 'Cozy Studio', 'Address': '123 Main St, College Park, MD 20740', 'Rent': 1250.0, 'Score': 8.9}
✅ Add Another Property: {'Title': 'Luxury Apartment', 'Address': '4500 Knox Rd, College Park, MD 20740', 'Rent': 1950.0, 'Score': 9.5}
❌ Invalid Title (empty): ValueError - Title cannot be empty.
❌ Invalid Address (non-string): TypeError - Title must be a string.
❌ Invalid Rent (negative): ValueError - Rent must be positive.
❌ Invalid Rent (non-numeric): ValueError - Rent must be a numeric value.
❌ Invalid Score (too high): ValueError - Score must be between 0 and 10.
❌ Invalid ZIP (letters): ValueError - ZIP code must be a 5-digit number.
❌ Invalid ZIP (short): ValueError - ZIP code must be a 5-digit number.
✅ List All Properties: [{'Title': 'Cozy Studio', 'Address': '123 Main St, College Park, MD 20740', 'Rent': 1250.0, 'Score': 8.9}, {'Title': 'Luxury Apartment', 'Address': '4500 Knox Rd, College Park, MD 20740', 'Rent': 1950.0, 'Score': 9.5}]
✅ Save Properties to CSV: None
✅ Load Properties from CSV: [{'Title': 'Cozy Studio', 'Address': '123 Main St, College Park, MD 20740', 'Rent': '1250.0', 'Score': '8.9'}, {'Title': 'Luxury Apartment', 'Address': '4500 Knox Rd, College Park, MD 20740', 'Rent': '1950.0', 'Score': '9.5'}]
✅ String Representation (__str__): PropertyManager(2 listings stored)

Testing Empty Save Scenario:
❌ Save with No Properties: ValueError - No properties to save.

=== RentalProperty Class Tests ===
✅ Valid Property Creation: {'address': '7303 Baltimore Ave, College Park, MD', 'rent': '$1,450 / month', 'zipcode': 20740, 'utilities_included': True, 'coordinates': (38.9786286, -76.937705)}
✅ Updated Rent: {'address': '7303 Baltimore Ave, College Park, MD', 'rent': '$1,600 / month', 'zipcode': 20740, 'utilities_included': True, 'coordinates': (38.9786286, -76.937705)}
✅ Updated Address: {'address': '4500 Knox Rd, College Park, MD', 'rent': '$1,600 / month', 'zipcode': 20740, 'utilities_included': True, 'coordinates': (38.980723, -76.936795)}
✅ Updated ZIP: {'address': '4500 Knox Rd, College Park, MD', 'rent': '$1,600 / month', 'zipcode': 20742, 'utilities_included': True, 'coordinates': (38.980723, -76.936795)}
✅ Updated Utilities Included: {'address': '4500 Knox Rd, College Park, MD', 'rent': '$1,600 / month', 'zipcode': 20742, 'utilities_included': False, 'coordinates': (38.980723, -76.936795)}
❌ Invalid Rent (negative): ValueError - Rent price cannot be negative or equal to zero.
❌ Invalid ZIP (short): ValueError - Zipcode must be 5 digits.
❌ Invalid Address (empty): ValueError - Address cannot be empty.
✅ String Representation (__str__): 4500 Knox Rd, College Park, MD — $1,600 / month | ZIP: 20742 | Utilities Included: No

=== ScoreCalculator Class Tests ===
✅ Create ScoreCalculator Object: ScoreCalculator object created
✅ Price Score Calculation: 5.67
✅ Flexibility Score Calculation: 7
✅ Commute Score Calculation: 1.6
❌ Overall Score Calculation: KeyError - '6'
❌ Invalid Price Score (negative rent): ValueError - Price and average price must be positive numbers.
❌ Invalid Flexibility Score (non-integer): KeyError - '-6'
❌ Invalid Commute Score (negative time): ValueError - Distance for mode 'drive' cannot be negative.

=== Coordinates Class Tests ===
✅ Create Coordinates Object: Address: 7303 Baltimore Ave, College Park, MD, Latitude: 38.9786286, Longitude: -76.937705
✅ Get Address: 7303 Baltimore Ave, College Park, MD
✅ Get Coordinates Tuple: (38.9786286, -76.937705)
✅ String Representation (__str__): Address: 7303 Baltimore Ave, College Park, MD, Latitude: 38.9786286, Longitude: -76.937705
❌ Update Address and Refresh Coordinates: TypeError - 'str' object is not callable
✅ Check Coordinates After Address Update: (38.980723, -76.936795)
✅ Manual Refresh of Coordinates: (38.980723, -76.936795)
❌ Invalid Address Set (empty): ValueError - Address cannot be empty.

=== Commute Class Test ===
#The test results cannot be accessed at the moment because there is a problem with the tester's computer. It will be resolved as soon as possible.
