import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Import each class from its file
from formatter import Formatter
from commute import Commute
from validator import Validator
from coordinates import Coordinates
from listing_manager import PropertyManager
from rental_property import RentalProperty

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

print("\n=== Validator Class Tests ===")

v = Validator()

#valid_address
#valid test
run_test("Valid Address", v.validate_address, "123 Main St, College Park, MD")
#invalid test
run_test("Invalid Address (empty)", v.validate_address, "")
run_test("Invalid Address (number)", v.validate_address, 123)

#validate_rent
#valid test
run_test("Valid Rent", v.validate_rent, 1500)
#invalid test
run_test("Invalid Address (number)", v.validate_address, 123)
run_test("Invalid Rent (negative)", v.validate_rent, -1200)
run_test("Invalid Rent (string)", v.validate_rent, "one thousand")

#validate_zip
#valid test
run_test("Valid ZIP", v.validate_zip, "20740")
#invalid test
run_test("Invalid ZIP (too short)", v.validate_zip, "207")

#validate_title
#valid test
run_test("Valid Title", v.validate_title, "Spacious Apartment Near UMD")
#invalid test
run_test("Invalid Title (empty)", v.validate_title, "")

#validate_email
#valid test
run_test("Valid Email", v.validate_email, "user@example.com")
#invalid test
run_test("Invalid Email (no @)", v.validate_email, "invalidemail.com")

#validate_locations
#valid test
run_test("Valid Class Locations", v.validate_locations, ["ESJ", "HBK", "KEY"])
#invalid test
run_test("Invalid Locations (too many)", v.validate_locations, ["ESJ", "HBK", "KEY", "MMH", "CCC", "TWS"])

#__str__ String Representation
run_test("String Representation", str, v)


print("\n=== PropertyManager Class Tests ===")

pm = PropertyManager()

# add_property 
# valid test
run_test("Add Valid Property", pm.add_property,
         "Cozy Studio", "123 Main St", "College Park", "MD", "20740", 1250, 8.9)
run_test("Add Another Property", pm.add_property,
         "Luxury Apartment", "4500 Knox Rd", "College Park", "MD", "20740", "1,950", 9.5)
# invalid tests
run_test("Invalid Title (empty)", pm.add_property,
         "", "123 Main St", "College Park", "MD", "20740", 1250, 8.9)
run_test("Invalid Address (non-string)", pm.add_property,
         123, "Main St", "College Park", "MD", "20740", 1250, 8.9)
run_test("Invalid Rent (negative)", pm.add_property,
         "Cozy Studio", "123 Main St", "College Park", "MD", "20740", -1000, 8.9)
run_test("Invalid Rent (non-numeric)", pm.add_property,
         "Cozy Studio", "123 Main St", "College Park", "MD", "20740", "one thousand", 8.9)
run_test("Invalid Score (too high)", pm.add_property,
         "Cozy Studio", "123 Main St", "College Park", "MD", "20740", 1250, 12)
run_test("Invalid ZIP (letters)", pm.add_property,
         "Cozy Studio", "123 Main St", "College Park", "MD", "20A40", 1250, 8.9)
run_test("Invalid ZIP (short)", pm.add_property,
         "Cozy Studio", "123 Main St", "College Park", "MD", "207", 1250, 8.9)

#valids
run_test("List All Properties", pm.list_properties)
run_test("Save Properties to CSV", pm.save_to_csv, "test_properties.csv")
run_test("Load Properties from CSV", pm.load_from_csv, "test_properties.csv")
run_test("String Representation (__str__)", str, pm)

# CSV save with no data
print("\nTesting Empty Save Scenario:")
pm_empty = PropertyManager()
run_test("Save with No Properties", pm_empty.save_to_csv, "empty.csv")


print("\n=== RentalProperty Class Tests ===")
# Valid Property Creation
rp = RentalProperty("7303 Baltimore Ave, College Park, MD", 1450, "20740", True)
run_test("Valid Property Creation", rp.summary)

#update tests
def test_updated_rent():
    rp.rent = 1600
    return rp.summary()

def test_updated_address():
    rp.address = "4500 Knox Rd, College Park, MD"
    return rp.summary()

def test_updated_zip():
    rp.zipcode = "20742"
    return rp.summary()

def test_updated_utilities():
    rp.utilities_included = False
    return rp.summary()

run_test("Updated Rent", test_updated_rent)
run_test("Updated Address", test_updated_address)
run_test("Updated ZIP", test_updated_zip)
run_test("Updated Utilities Included", test_updated_utilities)

#invalid test
def invalid_rent_negative():
    rp.rent = -1000

def invalid_zip_short():
    rp.zipcode = "207"

def invalid_address_empty():
    rp.address = ""

run_test("Invalid Rent (negative)", invalid_rent_negative)
run_test("Invalid ZIP (short)", invalid_zip_short)
run_test("Invalid Address (empty)", invalid_address_empty)

run_test("String Representation (__str__)", str, rp)

print("\n=== Coordinates Class Tests ===")

# Create a valid Coordinates object
def create_coords():
    return Coordinates("7303 Baltimore Ave, College Park, MD")

run_test("Create Coordinates Object", create_coords)
c = create_coords()

#valid tests
def get_address():
    return c.address

def get_coordinates():
    return c.coordinates

def string_output():
    return str(c)

run_test("Get Address", get_address)
run_test("Get Coordinates Tuple", get_coordinates)
run_test("String Representation (__str__)", string_output)

#update test
def update_address():
    c.address = "4500 Knox Rd, College Park, MD"
    return c.address()
run_test("Update Address and Refresh Coordinates", update_address)

def check_coordinates_refresh():
    return c.coordinates
run_test("Check Coordinates After Address Update", check_coordinates_refresh)

def manual_refresh():
    return c.refresh_coordinates()
run_test("Manual Refresh of Coordinates", manual_refresh)

#invalid test
def invalid_address_set():
    c.address = ""
run_test("Invalid Address Set (empty)", invalid_address_set)

print("\n=== Commute Class Tests ===")
# valid object
c = Commute("7303 Baltimore Ave, College Park, MD", 
            "8500 Paint Branch Dr, College Park, MD",
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

