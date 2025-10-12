from src.function_library import *

print("=== Simple functions test ===")

try:
    print("validate_rental_address:", validate_rental_address("123 Main St, Springfield, IL 62704"))
    print("validate_rental_address:", validate_rental_address(""))
except Exception as e:
    print("Error:", e)

try:
    print("validate_rent_input:", validate_rent_input(1500))
    print("validate_rent_input:", validate_rent_input(-1500))
    print("validate_rent_input:", validate_rent_input("1500"))
except Exception as e:
    print("Error:", e)

try:
    print("validate_zipcode:",validate_zipcode("62704"))
    print("validate_zipcode:",validate_zipcode("abcde"))
    print("validate_zipcode:",validate_zipcode("627"))
except Exception as e:
    print("Error:", e)

try:
    print("format_address:", format_address("123 main st, college park 62704"))
    print("format_address:", format_address(""))
    print("format_address:", format_address(62704))
except Exception as e:
    print("Error:", e)

try:
    print("format_rent_display:", format_rent_display(1250))
    print("format_rent_display:", format_rent_display(-1250))
    print("format_rent_display:", format_rent_display("1250"))
except Exception as e:
    print("Error:", e)

try:
    print("check_utilities_included:", check_utilities_included(True))
    print("check_utilities_included:", check_utilities_included(False))
except Exception as e:
    print("Error:", e)

print("\n=== Medium Functions Test ===")


try:
    print("calculate_price_score:", calculate_price_score(1200, 1500))
    print("calculate_price_score:", calculate_price_score(4500, 1500)) #check from terminal!
    print("calculate_price_score:", calculate_price_score(1600, 1500))
    print("calculate_price_score:", calculate_price_score(-1200, 1500))
    print("calculate_price_score:", calculate_price_score("1200", 1500))
except Exception as e:
    print("Error:", e)

try:
    print("calculate_commute_time:", calculate_commute_time(3, 'drive')) 
    print("calculate_commute_time:", calculate_commute_time(5, 'bike'))
    print("calculate_commute_time:", calculate_commute_time(-2, 'walk'))
    print("calculate_commute_time:", calculate_commute_time('abc', 'drive'))
    print("calculate_commute_time:", calculate_commute_time(3, 'fly'))
except Exception as e:
    print("Error:", e)      

try:
    print("calculate_flexibilty_score:", calculate_flexibilty_score("high"))
    print("calculate_flexibilty_score:", calculate_flexibilty_score("12 Months"))
    print("calculate_flexibilty_score:", calculate_flexibilty_score("Month-to-Month"))
    print("calculate_flexibilty_score:", calculate_flexibilty_score("6 Month"))
    print("calculate_flexibilty_score:", calculate_flexibilty_score(""))
except Exception as e:
    print("Error:", e)

print("\n=== Complex Functions Test ===")

try:
    print("validate_class_locations:", validate_class_locations(["ESJ", "HBK", "KEY"]))
    print("validate_class_locations:", validate_class_locations([]))
    print("validate_class_locations:", validate_class_locations(["ESJ", "HBK", "KEY", "MMH", "CCC", "TWS"]))
except Exception as e:
    print("Error:", e)

try:
    print("calculate_commute_score", calculate_commute_score({'walk': 10, 'bike': 20, 'drive': 5}))
    print("calculate_commute_score", calculate_commute_score({'walk': -10, 'bike': 20, 'drive': 5}))
except Exception as e:
    print("Error:", e) 