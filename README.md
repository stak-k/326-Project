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
UMD students often struggle to find rentals that balance affordability, commute convenience, 
and lease flexibility.

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

# Testing Strategy
This project includes a comprehensive testing suite using Python’s `unittest`
framework.

Tests include:
    - Unit tests for isolated logic
    - Integration tests for class coordination
    - System tests for complete end-to-end workflows
    - I/O tests for CSV persistence and validation

All tests pass at submission.

See `docs/testing_strategy.md` for full testing documentation.

# Running Tests


This project includes unit, integration, and system tests written using
Python’s built-in `unittest` framework.

To run the full test suite from the project root directory:

``` bash
python -m unittest discover tests
```

# Installation & Setup

## Requirements
- Python 3.9 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
``` python
git clone https://github.com/<your-username>/326-Project.git
cd 326-Project
```

### Step 2: (Optional) Create a Virtual Environment 
``` bash
python3 -m venv venv
source venv/bin/activate      # macOS/Linux  
venv\Scripts\activate         # Windows
```

### Step 3:  Install required packages
All required packages are listed in requirements.txt 
You can install it manually:
``` bash
pip install -r requirements.txt
```

### Step 4: Demos
#### Demo Scripts

The `examples/` directory contains multiple demo scripts, each serving
a specific purpose.

### Primary System Demo (Recommended)
```bash
python examples/demo_project_3.py
```
### Additional Demos

```bash
python examples/demo_script.py
python examples/demo_script_classes.py
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
# Video presentation
A 5–10 minute project presentation video can be found here:

[ INSERT VIDEO LINK ]

# Contribution guidelines for team members
    Serra Tak 
        - Created and tested validation and formatting functions
        - Contributed to methods and CSV persistence logic
        - Implemented and expanded system-level tests
        - Organized the project structure and folder layout
        - Led testing, debugging, and documentation cleanup
    
    Nicholas Stroble
        - Contributed to docstring documentation and initial setup
        - Collaborated on designing and setting up a database structure for existing rental properties.
    
    Bryan Sturgis
        - Created the wireframe design for the user interface and visual layout
        - Implemented medium, complex, and advanced functions, including geolocation and scoring logic.
        - Collaborated on designing and setting up a database structure for existing rental properties.
        - Validated outputs, reviewed final test results, and assisted with integration testing and README updates.

    
