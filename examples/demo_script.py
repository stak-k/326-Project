import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from function_library import *




def run_test(func_name, *args):
    """Helper to run tests neatly."""
    try:
        result = func_name(*args)
        print(f"✅ {func_name.__name__}{args} → {result}")
    except Exception as e:
        print(f"❌ {func_name.__name__}{args} → {type(e).__name__}: {e}")

print("=== Simple functions test ===")

#try:
run_test(validate_rental_address, "123 Main St, Springfield, IL 62704")
run_test(validate_rental_address, "")
run_test(validate_rent_input, 1500)
run_test(validate_rent_input, -1500)
run_test(validate_rent_input, "1500")
run_test(validate_rent_input, "1500")
run_test(validate_zipcode, "62704")
run_test(validate_zipcode, "abcde")
run_test(validate_zipcode, "627")
run_test(format_address, "123 main st, college park 62704")
run_test(format_address, "")
run_test(format_address, 62704)
run_test(format_rent_display, 1250)
run_test(format_rent_display, -1250)
run_test(format_rent_display, "1250")
run_test(check_utilities_included, True)
run_test(check_utilities_included, False)


print("\n=== Medium Functions Test ===")

run_test(calculate_price_score, 1200, 1500)
run_test(calculate_price_score, 4500, 1500)
run_test(calculate_price_score, -1200, 1500)
run_test(calculate_price_score, "1200", 1500)
run_test(calculate_commute_time, 3, "drive")
run_test(calculate_commute_time, 5, "bike")
run_test(calculate_commute_time, -2, "walk")
run_test(calculate_commute_time, 3, "fly")
run_test(calculate_flexibilty_score, "Month-to-Month")
run_test(calculate_flexibilty_score, "")
run_test(calculate_flexibilty_score, "6Month")

print("\n=== Complex Functions Test ===")

run_test(validate_class_locations, ["ESJ", "HBK", "KEY"])
run_test(validate_class_locations, [])
run_test(validate_class_locations, ["ESJ", "HBK", "KEY", "MMH", "CCC", "TWS"])
run_test(calculate_commute_score, {'walk': 10, 'bike': 20, 'drive': 5})
run_test(calculate_commute_score, {'walk': -10, 'bike': 20, 'drive': 5})

print("\n=== Geocoding Function Test ===")

# Valid address test
run_test(get_property_coordinates, "7303 Baltimore Ave, College Park, MD")

# Invalid address test (should raise ValueError)
run_test(get_property_coordinates, " ")

# Nonsense address test (should likely raise ValueError for not found)
run_test(get_property_coordinates, "1234 Nowhere Land XYZ")