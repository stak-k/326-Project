# Project Description

Rental Hunters is a Python-based function library created to analyze Rental Hunters is a student-focused housing analysis system that helps University of Maryland students find the best rental options near campus.
The system evaluates properties based on price fairness, commute convenience, safety, lease flexibility, and access to nearby amenities — producing an overall “Best Value Score” for each rental.


# Team Members:
    Serra Tak 
    Nicholas Stroble
    Bryan Sturgis


# Domain Focus and Problem Statement

Domain: Off-Campus Student Housing Analysis

Problem: UMD students often struggle to find rentals that balance affordability, safety, and convenience.

Solution: This library provides Python functions that calculate rental scores using price comparisons, commute times, nearby amenities, and safety metrics. These will later be integrated into a complete scoring system and user interface.

# Installation & Setup

To run the Rental Hunters Function Library locally:

Clone the repository
``` python 
git clone https://github.com/<your-username>/326-Project.git
cd 326-Project
```
Open the repository on GitHub and click “Open with GitHub Desktop”

Once cloned, open it in VS Code

(Optional) — If you want to use a virtual environment (recommended for Python projects):
``` python
python3 -m venv venv
source venv/bin/activate      # macOS/Linux  
venv\Scripts\activate         # Windows
```

Install required packages
Currently, this project only requires the geopy library for geolocation features.
You can install it manually:
``` python
pip install geopy
```


Run the demo script to test all functions
``` python
python3 examples/demo_script.py
```

# Usage examples for key functions

Usage Examples
Creating Rental Properties
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

Creating Score Rental
from score_calculator import ScoreCalculator

# 2. Score rentals
calculator = ScoreCalculator()
score1 = calculator.overall_score(rental1)
score2 = calculator.overall_score(rental2)

print("Scores:")
print(rental1.address, score1)
print(rental2.address, score2)

Manage listings
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

# Function library overview and organization

- `src/function_library.py`: Main file containing all 15 functions (Simple, Medium, and Complex).
- `examples/demo_script.py`: Script that tests each function and prints results to the terminal.
- `docs/usage_examples.md`: Markdown file showing formatted usage examples.
- `requirements.txt`: Lists external dependencies (e.g., geopy).


# Contribution guidelines for team members
    Serra Tak 
        - Created and tested multiple validation and formatting functions
        - Organized project structure and folder setup
        - Researched and prepared documentation sources such as CSV datasets
        - Conducted testing, debugging, and documentation cleanup
    Nicholas Stroble
        - Contributed to docstring documentation and initial setup
        - Collaborated on designing and setting up a database structure for existing rental properties.
    Bryan Sturgis
        - Created the wireframe design for the user interface and visual layout
        - Implemented medium, complex, and advanced functions, including geolocation and scoring logic.
        - Collaborated on designing and setting up a database structure for existing rental properties.
        - Validated outputs, reviewed final test results, and assisted with integration testing and README updates.

    
