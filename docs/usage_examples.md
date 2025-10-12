# Usage Examples

This document demonstrates how to use and how to use and test the functions in the ** Rental Hunters Function Library **.

Each example below shows expected outputs and common error cases.

## Simple Functions

###  `validate_rental_address(address)`
```python
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
