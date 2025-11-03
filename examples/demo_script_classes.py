import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Import each class from its file
from formatter import Formatter
from commute import Commute
from validator import Validator
from coordinates import Coordinates

def run_test(description, func_name, *args):
    """Helper to run tests neatly with labels."""
    try:
        result = func_name(*args)
        print(f"✅ {description}: {result}")
    except Exception as e:
        print(f"❌ {description}: {type(e).__name__} - {e}")

print("\n=== Formatter Class Tests ===")

f = Formatter()

# format_address
#valid test 
run_test("Format Address", f.format_address, "123 main st, college park, md")
#invalid test
run_test("Invalid Address (empty)", f.format_address, "")
run_test("Invalid Address (number)", f.format_address, 123)

#format_listing_title
#valid test
run_test("Format Title", f.format_listing_title, "spacious apartment near umd")
#invalid test
run_test("Invalid Title (empty)", f.format_listing_title, "")

#format_rent_display
#valid test
run_test("Format Rent Display (default term)", f.format_rent_display, 1450)
run_test("Format Rent Display (custom term)", f.format_rent_display, 1800, "Year")
#invalid
run_test("Invalid Rent (negative)", f.format_rent_display, -1000)
run_test("Invalid Rent (string price)", f.format_rent_display, "1500")

#generate_listing_summary
#valid test
run_test("Generate Summary", f.generate_listing_summary, "Cozy Studio", 1250, "123 Main St, College Park, MD", 9.1)
#invalid test
run_test("Invalid Summary (missing address)", f.generate_listing_summary, "Cozy Studio", 1250, "", 8.5)
run_test("Invalid Summary (wrong score type)", f.generate_listing_summary, "Modern Loft", 1800, "4500 Knox Rd", "high")

#setting
#valid
run_test("Settings Property", lambda: f.settings)

#__str__ / String Representation
#valid
run_test("String Representation", str, f)


print("\n=== Commute Class Tests ===")

# valid object
c = Commute("7303 Baltimore Ave, College Park, MD", 
            "Edward St. John Learning Center, College Park, MD", 
            "walk")

# object creation confirmation valid test
run_test("Valid Commute Creation", c.summary)

#valid test for values 
run_test("Start Address Retrieved", c.start_address)
run_test("End Address Retrieved", c.end_address)
run_test("Transportation Mode Retrieved", c.mode)
run_test("Distance (miles) Retrieved", c.distance_miles)
run_test("Time (minutes) Retrieved", c.time_minutes)

#__str__ String Representation
run_test("String Representation (__str__)", str, c)

# MODE UPDATE TESTS 
print("\n MODE UPDATE TESTS")
c.mode = "drive"
run_test("Mode changed to drive", c.mode)

c.mode = "metro"
run_test("Mode changed to metro", c.mode)

#refresh commmute calculation
run_test("Commute Recalculate", c.refresh_commute)

# SUMMARY DICTIONARY TEST
print("\n SUMMARY DICTIONARY TEST")
run_test("Generate Full Commute Summary", c.summary)

#Invalid Test
print("\n INVALID TEST ")

def invalid_start_address():
    return Commute("", "Edward St. John Learning Center, College Park, MD", "walk")

def invalid_mode():
    return Commute("7303 Baltimore Ave, College Park, MD", "Edward St. John Learning Center, College Park, MD", "fly")

run_test("Invalid Start Address (empty)", invalid_start_address)
run_test("Invalid Mode (unsupported)", invalid_mode)

