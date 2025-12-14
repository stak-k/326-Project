# Rental Hunters - INST326 Project

Rental Hunters is a **student-focused housing analysis system** designed to help
University of Maryland (UMD) students identify the best off-campus rental options
near campus.

This project serves as the **Project 4 Capstone** for INST326 and integrates
validation, scoring logic, data persistence, and comprehensive testing into
a complete, functional system.

The system evaluates rentals based on:
- Price fairness
- Commute convenience
- Lease flexibility
- Property type desirability

Each rental receives an overall **Best Value Score**, allowing students to
compare and rank housing options objectively.

# Team Members:
   - Bryan Sturgis
   - Serra Tak 
   - Nicholas Stroble
    


# Domain Focus and Problem Statement

### Domain
Off-Campus Student Housing Analysis

### Problem
UMD students often struggle to find rentals that balance affordability, safety, and convenience.

### Solution: 
Rental Hunters provides a Python-based system that:
- Validates rental data
- Scores properties using multiple weighted factors
- Ranks rentals to answer the charter question:
  **“Which rental is the best option?”**

# File Structure
``` css
.
├── src/
│   ├── function_library.py
│   ├── validator.py
│   ├── formatter.py
│   ├── coordinates.py
│   ├── commute.py
│   ├── property.py
│   ├── property_type.py
│   ├── rental_property.py
│   ├── score_calculator.py
│   ├── listing_manager.py
│   └── main.py
│
├── tests/
│   └── test_system_flow.py
│
├── examples/
│   ├── demo_project_3.py
│   ├── demo_script.py
│   └── demo_script_classes.py
│
├── docs/
│   ├── architecture.txt
│   ├── class_design.md
│   ├── testing_strategy.md
│   └── usage_examples.md
│
├── requirements.txt
└── README.md
``` 

# System Architecture
The system follows a modular, object-oriented architecture using:

    - Inheritance for property types
    - Composition for system integration
    - Polymorphism for scoring behavior

See `docs/architecture.txt` for a detailed architecture diagram and explanation.

# Data Persistence & I/O
Rental Hunters supports full data persistence using CSV files.

Features include:
    - Saving ranked rental results to CSV
    - Loading saved state in a new session
    - Import validation to prevent corrupted or invalid data
    - Graceful error handling for missing or malformed files

# Testin Strategy

# Installation & Setup

### Requirments:
    - Python 3.9+
    - geopy

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

    
