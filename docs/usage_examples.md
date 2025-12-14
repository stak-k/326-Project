# Usage examples for key functions

## Creating Rental Properties
``` python
from rental_property import RentalProperty

# 1. Create rental properties
rental1 = RentalProperty(
    address="7303 Baltimore Ave, College Park, MD",
    rent=1200,
    zipcode=20740,
    utilities_included=True,
    property_type_name="2x2",
    lease_term=12,
    distances={"drive": 10, "walk": 25}
)

rental2 = RentalProperty(
    address="4500 Knox Rd, College Park, MD",
    rent=1450,
    zipcode=20740,
    utilities_included=False,
    property_type_name="4x4",
    lease_term=6,
    distances={"drive": 5, "walk": 15}
)
```

## Creating Score Rental
``` python
from score_calculator import ScoreCalculator

# 2. Score rentals
calculator = ScoreCalculator()
score1 = calculator.overall_score(rental1)
score2 = calculator.overall_score(rental2)

print("Scores:")
print(rental1.address, score1)
print(rental2.address, score2)
```

## Manage listings
``` python
from listing_manager import PropertyManager

# 3. Manage listings
manager = PropertyManager()
manager.add_rental(rental1, score1)
manager.add_rental(rental2, score2)

# 4. View ranked properties
ranked = manager.list_properties()
print("\nRanked Rentals:")
for r in ranked:
    print(r)

# 5. Save results
manager.save_to_csv("ranked_rentals.csv")
print("\nResults saved to ranked_rentals.csv")
```
