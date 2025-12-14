import unittest
import os
import sys

#allow imports from SRC directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'SRC'))) 

from rental_property import RentalProperty
from score_calculator import ScoreCalculator
from listing_manager import PropertyManager

class TestSystemFlow(unittest.TestCase):
    """system test: end to end workflow
       unit test: score calculation """

    # Create sample rental properties
    def setUp(self):
        self.calculator = ScoreCalculator()
        self.manager = PropertyManager()
        self.test_file = "test_ranked_rentals.csv"

        self.rental = RentalProperty(
            address="7303 Baltimore Ave, College Park, MD",
            rent=1200,
            zipcode=20740,
            utilities_included=True,
            property_type_name="2x2",
            lease_term=12,
            distances={"drive": 10, "walk": 25}
        )

    # ------------------------
    # SYSTEM TEST
    # ------------------------
    def test_full_system_flow_creates_csv(self):
        """System test: rental → score → manager → CSV"""

        score = self.calculator.overall_score(self.rental)
        self.manager.add_rental(self.rental, score)
        self.manager.save_to_csv(self.test_file)

        self.assertTrue(os.path.exists(self.test_file))
        self.assertEqual(len(self.manager.list_properties()), 1)

        with open(self.test_file, "r") as file:
            lines = file.readlines()
            self.assertGreater(len(lines), 1)

    # ------------------------
    # UNIT TEST
    # ------------------------
    def test_overall_score_range(self):
        """Unit test: overall score stays within 0–10"""

        score = self.calculator.overall_score(self.rental)
        self.assertIsInstance(score, float)
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 10)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)


if __name__ == "__main__":
    unittest.main()
