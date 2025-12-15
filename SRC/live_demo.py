"""
live_demo.py

This script simulates how the Rental Hunters system would work
before building a graphical UI.

It allows a user to:
1. Get a rental score
2. Save the rental to CSV
3. View saved rentals
4. Delete saved rentals
5. View detailed score breakdowns
6. End the session

This demonstrates:
- Object creation
- Validation
- Scoring
- Persistence (CSV I/O)
- End-to-end workflow
"""


# live_demo.py

from rental_property import RentalProperty
from score_calculator import ScoreCalculator
from listing_manager import PropertyManager
from commute import Commute

CAMPUS_ADDRESS = "7649 Library Ln, College Park, MD 20742"



def display_score_breakdown(rental, calculator):
    """Display a detailed breakdown of the rental score."""

    price_score = calculator.price_score(rental.rent)
    flexibility_score = calculator.flexibility_score(rental.lease_term)
    commute_score = calculator.commute_score(rental.distances)
    type_score = rental.property_type_obj.type_score()
    overall = calculator.overall_score(rental)

    print("\n📊 RENTAL SCORE BREAKDOWN")
    print("--------------------------------")
    print(f"💰 Price Score:        {price_score}/10")
    print(f"📄 Lease Flexibility:  {flexibility_score}/10")
    print(f"🚶 Commute Score:      {commute_score}/10")
    print(f"🏠 Property Type:      {type_score}/10")
    print("--------------------------------")
    print(f"⭐ OVERALL SCORE:      {overall}/10\n")

    # --------------------------------
    # COMMUTE DETAILS (RECOMPUTED)
    # --------------------------------
    print("🚗 COMMUTE DETAILS")

    for mode in rental.distances.keys():
        commute = Commute(
            rental.address,
            CAMPUS_ADDRESS,
            mode=mode
        )

        print(
            f"{mode.title():<6}: "
            f"{commute.distance_miles} miles → "
            f"{commute.time_minutes} minutes"
        )



def get_rental_score(manager, calculator):
    """Collect user input, calculate score, and optionally save rental."""

    print("\n🏡 GET RENTAL SCORE")

    address = input("Enter rental address: ").strip()
    rent = float(input("Monthly rent ($): "))
    zipcode = int(input("ZIP code: "))
    utilities = input("Utilities included? (yes/no): ").strip().lower() == "yes"
    lease_term = int(input("Lease term (6 or 12 months): "))

    print("\nProperty Types:")
    print("Studio, 1x1, 2x2, 3x3, 4x4, Basement, Shared House")
    property_type = input("Select property type: ").strip()

    print("\n📍 Calculating commute to campus...")

    walk_commute = Commute(address, CAMPUS_ADDRESS, mode="walk")
    drive_commute = Commute(address, CAMPUS_ADDRESS, mode="drive")

    # Distances are the SAME miles, but times differ
    distances = {
        "walk": walk_commute.distance_miles,
        "drive": drive_commute.distance_miles
    }



    rental = RentalProperty(
        address=address,
        rent=rent,
        zipcode=zipcode,
        utilities_included=utilities,
        property_type_name=property_type,
        lease_term=lease_term,
        distances=distances
    )

    display_score_breakdown(rental, calculator)

    save = input("Save this rental? (yes/no): ").strip().lower()
    if save == "yes":
        score = calculator.overall_score(rental)
        manager.add_rental(rental, score)
        manager.save_to_csv("saved_rentals.csv")
        print("💾 Rental saved.\n")
    else:
        print("❌ Rental not saved.\n")


# -------------------------------
# SAVED RENTALS SUBMENU
# -------------------------------

def saved_rentals_menu(manager, calculator):
    """Menu for interacting with saved rentals."""

    try:
        manager.load_from_csv("saved_rentals.csv")
    except ValueError:
        print("\nNo saved rentals found.")
        return

    while True:
        rentals = manager.list_properties()

        if not rentals:
            print("\nNo saved rentals.")
            return

        print("\n📂 SAVED RENTALS")
        for i, r in enumerate(rentals, start=1):
            print(f"{i}. {r['Address']} | Score: {r['Overall Score']}/10")

        print("\nOptions:")
        print("1. View detailed property info")
        print("2. Delete a property")
        print("3. Back to main menu")

        choice = input("Choose an option (1–3): ").strip()

        if choice == "1":
            index = int(input("Select property number: ")) - 1
            if index < 0 or index >= len(rentals):
                print("Invalid selection.")
                continue

            rental = RentalProperty.from_dict(rentals[index])
            display_score_breakdown(rental, calculator)

        elif choice == "2":
            index = int(input("Select property number to delete: ")) - 1
            if index < 0 or index >= len(rentals):
                print("Invalid selection.")
                continue

            deleted = rentals.pop(index)
            manager._properties = rentals
            manager.save_to_csv("saved_rentals.csv")
            print(f"🗑️ Deleted: {deleted['Address']}")

        elif choice == "3":
            return

        else:
            print("Invalid option.")


# -------------------------------
# MAIN MENU
# -------------------------------

def main():
    """Main interactive menu."""

    manager = PropertyManager()
    calculator = ScoreCalculator()

    while True:
        print("\n==============================")
        print("🏠 RENTAL HUNTERS LIVE DEMO")
        print("==============================")
        print("1. Get Rental Score")
        print("2. View Saved Rentals")
        print("3. End Session")

        choice = input("Choose an option (1–3): ").strip()

        if choice == "1":
            get_rental_score(manager, calculator)
        elif choice == "2":
            saved_rentals_menu(manager, calculator)
        elif choice == "3":
            print("\n👋 Session ended.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
