import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))


from property_type import (
    Studio, OneByOne, TwoByOne, TwoByTwo,
    ThreeByTwo, ThreeByThree,
    FourByTwo, FourByThree, FourByFour,
    Basement, SharedHouse
)

def test_property_types():
    props = [
        Studio("A", 1000, 12),
        OneByOne("A", 1500, 12),
        TwoByOne("A", 800, 12),
        TwoByTwo("A", 900, 12),
        ThreeByTwo("A", 700, 12),
        ThreeByThree("A", 800, 12),
        FourByTwo("A", 600, 12),
        FourByThree("A", 650, 12),
        FourByFour("A", 700, 12),
        Basement("A", 1200, 12),
        SharedHouse("A", 800, 12)
    ]

    for p in props:
        print(p.rental_type(), p.type_score())

test_property_types()


print("-------------------TEST 2 ---------------------------")

from rental_property import RentalProperty

r = RentalProperty(
    address="7303 Baltimore Ave, College Park, MD",
    rent=1500,
    zipcode=20740,
    utilities_included=True,
    property_type_name="4x4",
    lease_term=12,
    distances={"drive": 10, "walk": 30}
)

print("Address:", r.address)
print("Rent:", r.rent)
print("ZIP:", r.zipcode)
print("Utilities:", r.utilities_included)
print("Lease Term:", r.lease_term)
print("Property Type Obj:", r.property_type_obj.rental_type())
print("Type Score:", r.property_type_obj.type_score())
print("Distances:", r.distances)
print("Coordinates:", r.coordinates)

print("-------------------TEST 3 ---------------------------")

from rental_property import RentalProperty
from score_calculator import ScoreCalculator

r = RentalProperty(
    address="7303 Baltimore Ave, College Park, MD",
    rent=1500,
    zipcode=20740,
    utilities_included=True,
    property_type_name="4x4",
    lease_term=12,
    distances={"drive": 10, "walk": 30}
)

sc = ScoreCalculator()

print("Price Score:", sc.price_score(r.rent))
print("Flex Score:", sc.flexibility_score(r.lease_term))
print("Commute Score:", sc.commute_score(r.distances))
print("Type Score:", r.property_type_obj.type_score())

print("\n=== OVERALL SCORE ===")
print(sc.overall_score(r))



print("-------------------TEST 4 ---------------------------")


from rental_property import RentalProperty
from score_calculator import ScoreCalculator
from listing_manager import PropertyManager

r = RentalProperty(
    address="7303 Baltimore Ave, College Park, MD",
    rent=1500,
    zipcode=20740,
    utilities_included=True,
    property_type_name="2x1",
    lease_term=6,
    distances={"drive": 12}
)

sc = ScoreCalculator()
score = sc.overall_score(r)

pm = PropertyManager()
listing = pm.add_rental(r, score)

print(listing)
print(pm.list_properties())





