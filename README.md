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

- I dont know yet 

# Usage examples for key functions

- The key function get_property_coordinates() will be very helpful for generating geographic coordinates for various aspects of our project. One way we will need this is to the rental property coordinates in order to calculate distances from buildings, bus stops, and other locations.

- calculate_commute_score() Combines multiple transportation options (walk, bike, bus, drive) into a single average commute score (1–10).
Shorter times = higher scores.

- calculate_commute_time() Converts a given distance (in miles) into an estimated travel time (in minutes) depending on the chosen transportation mode — walking, biking, driving, or bus

- calculate_price_score() Generates a score (1–10) that reflects how affordable a rental is compared to the local average.
Used to evaluate the “Price” portion of the total rental value score.

- validate_zipcode() is important for checking that the entered ZIP code follows a valid U.S. 5-digit format.
This prevents location-based calculations from failing due to invalid ZIPs.

- format_address() Standardizes the address (e.g., “123 main st” → “123 Main St”) to maintain consistent data formatting before it’s sent for geocoding or comparisons.

- validate_rental_address() Ensures that the user enters a valid rental address before the property is evaluated.
It prevents missing or incorrectly formatted data from being submitted to the system.

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

    
