# tests/test_io_persistence.py
import sys
from pathlib import Path
import unittest
import os
import json

# Add SRC directory to Python path
sys.path.append(str(Path(__file__).resolve().parents[1] / "SRC"))

from listing_manager import PropertyManager
from rental_property import RentalProperty

TEST_CSV = Path(__file__).parent / "test_persistence.csv"


class TestIOPersistence(unittest.TestCase):

    def tearDown(self):
        # Clean up test CSV after each run
        if TEST_CSV.exists():
            TEST_CSV.unlink()

    def test_save_and_load_properties(self):
        manager = PropertyManager()

        rental = RentalProperty(
            address="123 College Ave, College Park, MD",
            rent=1200,
            zipcode=20740,
            utilities_included=True,
            property_type_name="1x1",
            lease_term=12,
            distances={"UMD": 10}
        )

        # Save
        manager.add_rental(rental, score=8.5)
        manager.save_to_csv(TEST_CSV)

        # Load
        new_manager = PropertyManager()
        new_manager.load_from_csv(TEST_CSV)
        loaded = new_manager.list_properties()

        # Assertions
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0]["ZIP"], "20740")
        self.assertIn("Distances", loaded[0])


        # Distances should be JSON string in CSV
        distances = json.loads(loaded[0]["Distances"])
        self.assertEqual(distances["UMD"], 10)

    def test_load_missing_file_raises_error(self):
        manager = PropertyManager()
        with self.assertRaises(ValueError):
            manager.load_from_csv("missing.csv")


if __name__ == "__main__":
    unittest.main(verbosity=2)
