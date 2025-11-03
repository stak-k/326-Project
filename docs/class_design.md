# Class Design Document

## Overview
The Rental Hunters Function Library is a modular system for managing and scoring rental properties. 
Each class has a distinct responsibility, promoting code reusability and maintainability.

## Classes and Responsibilities

### 1. Formatter
- **Purpose:** Standardizes text and numerical formatting for consistent output.
- **Key Methods:** 
  - `format_address(address)`
  - `format_listing_title(title)`
  - `format_rent_display(rent, term)`
  - `generate_listing_summary(title, rent, address, score)`

### 2. Validator
- **Purpose:** Ensures all user inputs (address, rent, ZIP, email, etc.) are valid before being processed.
- **Key Methods:** 
  - `validate_address()`, `validate_rent()`, `validate_zip()`, etc.

### 3. PropertyManager
- **Purpose:** Stores multiple property listings and handles CSV export/import.
- **Relationships:** Uses validated/cleaned data from `Validator` and `Formatter`.

### 4. RentalProperty
- **Purpose:** Represents one individual property.
- **Relationships:** 
  - Uses `Validator` for input checks.  
  - Uses `Coordinates` to get latitude/longitude.  
  - Uses `Formatter` to format addresses and rent.

### 5. Coordinates
- **Purpose:** Retrieves and stores latitude/longitude for a given address.
- **Dependencies:** `get_property_coordinates()` from `function_library.py`.

### 6. ScoreCalculator
- **Purpose:** Calculates category-specific scores (price, flexibility, commute) and combines them into one.
- **Dependencies:** Calls functions like `calculate_price_score()`, `calculate_commute_score()`.

### 7. Commute
- **Purpose:** Manages commute calculations between start and end points.
- **Dependencies:** Uses `Coordinates` and commute functions from `function_library`.


## Relationships Summary
- `RentalProperty` ↔ `Validator`, `Formatter`, `Coordinates`
- `PropertyManager` stores multiple `RentalProperty` objects.
- `ScoreCalculator` and `Commute` analyze property attributes.

## Design Principles
- **Encapsulation:** Each class protects its internal data through getters/setters.
- **Modularity:** Classes can be tested independently.
- **Reusability:** Core functions in `function_library.py` can serve other projects.
- **Error Handling:** Consistent use of exceptions (`TypeError`, `ValueError`) with clear messages.


## Future Extensions
- Add `CrimeScore` and `ConvenienceScore` to `ScoreCalculator`.
- Add UI integration for rental property visualization.

