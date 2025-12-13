from rental_property import RentalProperty
from score_calculator import ScoreCalculator
from listing_manager import PropertyManager

def main():
    print("Welcome to Rental Hunters!")
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

    calculator = ScoreCalculator()
    manager = PropertyManager()

    for rental in rentals:
        score = calculator.overall_score(rental)
        manager.add_rental(rental, score)

    results = manager.list_properties()
    results.sort(key=lambda r: r["Overall Score"], reverse=True)

    print("📊 Ranked Rentals:\n")
    for i, r in enumerate(results, start=1):
        print(
            f"{i}. {r['Address']} | "
            f"${r['Rent']} | "
            f"{r['Property Type']} | "
            f"Score: {r['Overall Score']}/10"
        )

    manager.save_to_csv("ranked_rentals.csv")
    print("\n💾 Results saved to ranked_rentals.csv")

if __name__ == "__main__":
    main()