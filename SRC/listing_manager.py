# class that stores multiple properties and can store into CSV

import csv

class PropertyManager:
    """
    Manages multiple rental property listings and allows exporting them to CSV.
    Handles data storage, validation, and formatted retrieval of property information.
    """

    def __init__(self):
        """
        Initializes an empty property manager.

        Attributes:
            _properties (list[dict]): Internal list storing property listings.
        """
        self._properties = []

    # ----------
    # Validation helpers
    # ----------

    def _validate_string(self, value: str, field_name: str) -> str:
        """
        Validates that a value is a non-empty string.

        Args:
            value (str): The value to validate.
            field_name (str): The name of the field for error messages.

        Returns:
            str: Trimmed and validated string.

        Raises:
            TypeError: If value is not a string.
            ValueError: If value is empty.
        """
        if not isinstance(value, str):
            raise TypeError(f"{field_name} must be a string.")
        clean_value = value.strip()
        if not clean_value:
            raise ValueError(f"{field_name} cannot be empty.")
        return clean_value

    def _validate_rent(self, rent) -> float:
        """
        Validates and converts rent to float.

        Args:
            rent (float | str): The rent value (may include '$' or ',')

        Returns:
            float: Clean numeric rent.

        Raises:
            ValueError: If rent cannot be converted or is non-positive.
        """
        if isinstance(rent, str):
            rent = rent.replace("$", "").replace(",", "").strip()
        try:
            rent = float(rent)
        except ValueError:
            raise ValueError("Rent must be a numeric value.")
        if rent <= 0:
            raise ValueError("Rent must be positive.")
        return rent

    def _validate_score(self, score: float) -> float:
        """
        Ensures a rental score is between 0 and 10.

        Args:
            score (float): The rental score.

        Returns:
            float: The validated score.

        Raises:
            ValueError: If score is outside 0-10.
        """
        if not isinstance(score, (int, float)):
            raise TypeError("Score must be numeric.")
        if not (0 <= score <= 10):
            raise ValueError("Score must be between 0 and 10.")
        return round(float(score), 2)

    # ----------
    # Add and manage listings
    # ----------

    def add_property(
        self,
        title: str,
        address: str,
        city: str,
        state: str,
        zipcode: str,
        rent: float,
        score: float
    ) -> dict:
        """
        Adds a property listing to the internal list.

        Args:
            title (str): Property title.
            address (str): Street address.
            city (str): City name.
            state (str): State abbreviation.
            zipcode (str): 5-digit ZIP code.
            rent (float): Monthly rent.
            score (float): Overall rental score (0–10).

        Returns:
            dict: The stored listing as a dictionary.

        Raises:
            TypeError, ValueError: If validation fails.
        """
        clean_title = self._validate_string(title, "Title")
        clean_address = self._validate_string(address, "Address")
        clean_city = self._validate_string(city, "City")
        clean_state = self._validate_string(state, "State")

        if not (zipcode.isdigit() and len(zipcode) == 5):
            raise ValueError("ZIP code must be a 5-digit number.")

        rent_value = self._validate_rent(rent)
        score_value = self._validate_score(score)

        listing = {
            "Title": clean_title.title(),
            "Address": f"{clean_address.title()}, {clean_city.title()}, {clean_state.upper()} {zipcode}",
            "Rent": rent_value,
            "Score": score_value
        }

        self._properties.append(listing)
        return listing

    def list_properties(self) -> list[dict]:
        """
        Returns a copy of all stored property listings.

        Returns:
            list[dict]: List of property dictionaries.
        """
        return self._properties.copy()

    # ----------
    # CSV Operations
    # ----------

    def save_to_csv(self, filename: str = "properties.csv") -> None:
        """
        Saves the property listings to a CSV file.

        Args:
            filename (str): Output file name (default: 'properties.csv').

        Raises:
            ValueError: If no properties exist to save.
        """
        if not self._properties:
            raise ValueError("No properties to save.")

        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=self._properties[0].keys())
            writer.writeheader()
            writer.writerows(self._properties)

    def load_from_csv(self, filename: str = "properties.csv") -> list[dict]:
        """
        Loads property listings from a CSV file.

        Args:
            filename (str): The CSV file to read.

        Returns:
            list[dict]: List of loaded property dictionaries.
        """
        with open(filename, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            self._properties = list(reader)
        return self._properties

    # ----------
    # Display and representation
    # ----------

    def __str__(self) -> str:
        """
        Returns a readable summary of the property manager state.

        Returns:
            str: Number of stored listings.
        """
        count = len(self._properties)
        return f"PropertyManager({count} listings stored)"
