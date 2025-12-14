
# This script demonstrates a full end-to-end workflow:
# - Create rental properties
# - Calculate scores
# - Rank rentals by value
# - Save results to a CSV file

from rental_property import RentalProperty
from score_calculator import ScoreCalculator
from listing_manager import PropertyManager

def main():
    """
    Main execution function for Rental Hunters.

        This function simulates a real user workflow by:
        - Creating sample rental listings
        - Scoring each rental
        - Ranking rentals by overall value
        - Persisting results to a CSV file
    """
    print("Welcome to Rental Hunters!")

# Step 1: Create sample rental properties
# These objects represent off-campus housing options
# near the University of Maryland

    rentals = [
        RentalProperty(
            address="7303 Baltimore Ave, College Park, MD",
            rent=1500,
            zipcode=20740,
            utilities_included=True,
            property_type_name="4x4",
            lease_term=12,
            distances={"drive": 10, "walk": 25}
        ),
        RentalProperty(
            address="4500 Knox Rd, College Park, MD",
            rent=1350,
            zipcode=20742,
            utilities_included=False,
            property_type_name="Studio",
            lease_term=6,
            distances={"drive": 8, "walk": 20}
        ),
        RentalProperty(
            address="8500 Paint Branch Dr, College Park, MD",
            rent=1700,
            zipcode=20740,
            utilities_included=True,
            property_type_name="2x2",
            lease_term=12,
            distances={"drive": 12, "walk": 35}
        )
    ]
#Step 2: Initialize system components
# ScoreCalculator handles scoring logic
# PropertyManager stores and manages ranked results
    calculator = ScoreCalculator()
    manager = PropertyManager()

# Step 3: Score rentals and store results
    for rental in rentals:
        score = calculator.overall_score(rental)
        manager.add_rental(rental, score)

 # Step 4: Rank rentals by overall score
    results = manager.list_properties()
    results.sort(key=lambda r: r["Overall Score"], reverse=True)

# Step 5: Display ranked rentals
    print("📊 Ranked Rentals:\n")
    for i, r in enumerate(results, start=1):
        print(
            f"{i}. {r['Address']} | "
            f"${r['Rent']} | "
            f"{r['Property Type']} | "
            f"Score: {r['Overall Score']}/10"
        )

# Step 6: Save ranked results to CSV
    manager.save_to_csv("ranked_rentals.csv")
    print("\n💾 Results saved to ranked_rentals.csv")

# Run the program
# This ensures the script only runs when executed directly,
# not when imported for testing.
if __name__ == "__main__":
    main()