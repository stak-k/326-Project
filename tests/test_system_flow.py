"""
Comprehensive test suit for Rental Hunter system
Includes:
- System test: end to end workflow from rental creation to CSV output
- Integration Test: class to class interactions
- I/O Test: file read/write operations
"""
import unittest
import os
import sys
from unittest.mock import patch

#allow imports from SRC directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'SRC'))) 

from rental_property import RentalProperty
from score_calculator import ScoreCalculator
from listing_manager import PropertyManager

# --------------------------------------------------
# UNIT TESTS
# --------------------------------------------------

class TestScoreCalculatorUnit(unittest.TestCase):
    """Unit tests for score calculation logic."""

    @patch("coordinates.get_property_coordinates", return_value=(38.99, -76.94))
    def setUp(self, mock_geo):
        self.rental = RentalProperty(
            address="7303 Baltimore Ave, College Park, MD",
            rent=1200,
            zipcode=20740,
            utilities_included=True,
            property_type_name="2x2",
            lease_term=12,
            distances={"drive": 10, "walk": 25}
        )
        self.calculator = ScoreCalculator()

    def test_score_is_float(self):
        score = self.calculator.overall_score(self.rental)
        self.assertIsInstance(score, float)

    def test_score_within_valid_range(self):
        score = self.calculator.overall_score(self.rental)
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 10)


# --------------------------------------------------
# INTEGRATION TESTS
# --------------------------------------------------

class TestIntegrationFlow(unittest.TestCase):
    """Integration tests: class coordination & data flow."""

    @patch("coordinates.get_property_coordinates", return_value=(38.99, -76.94))
    def setUp(self, mock_geo):
        self.calculator = ScoreCalculator()
        self.manager = PropertyManager()

        self.rental1 = RentalProperty(
            address="7303 Baltimore Ave, College Park, MD",
            rent=1200,
            zipcode=20740,
            utilities_included=True,
            property_type_name="2x2",
            lease_term=12,
            distances={"drive": 10, "walk": 25}
        )

        self.rental2 = RentalProperty(
            address="4500 Knox Rd, College Park, MD",
            rent=1800,
            zipcode=20740,
            utilities_included=False,
            property_type_name="4x4",
            lease_term=6,
            distances={"drive": 15}
        )

    def test_property_scored_and_added(self):
        score = self.calculator.overall_score(self.rental1)
        self.manager.add_rental(self.rental1, score)
        self.assertEqual(len(self.manager.list_properties()), 1)

    def test_multiple_properties_added(self):
        s1 = self.calculator.overall_score(self.rental1)
        s2 = self.calculator.overall_score(self.rental2)

        self.manager.add_rental(self.rental1, s1)
        self.manager.add_rental(self.rental2, s2)

        self.assertEqual(len(self.manager.list_properties()), 2)

    def test_rent_affects_score(self):
        s1 = self.calculator.overall_score(self.rental1)
        s2 = self.calculator.overall_score(self.rental2)
        self.assertGreater(s1, s2)

    def test_property_type_influences_score(self):
        s1 = self.calculator.overall_score(self.rental1)
        s2 = self.calculator.overall_score(self.rental2)
        self.assertNotEqual(s1, s2)

    def test_scores_preserved_with_properties(self):
        score = self.calculator.overall_score(self.rental1)
        self.manager.add_rental(self.rental1, score)
        listing = self.manager.list_properties()[0]
        self.assertIn("Overall Score", listing)


# --------------------------------------------------
# SYSTEM TESTS
# --------------------------------------------------

class TestSystemWorkflow(unittest.TestCase):
    """System tests: end-to-end workflows & persistence."""

    @patch("coordinates.get_property_coordinates", return_value=(38.99, -76.94))
    def setUp(self, mock_geo):
        self.manager = PropertyManager()
        self.calculator = ScoreCalculator()
        self.test_file = "test_ranked_rentals.csv"

        self.rental = RentalProperty(
            address="7303 Baltimore Ave, College Park, MD",
            rent=1200,
            zipcode=20740,
            utilities_included=True,
            property_type_name="2x2",
            lease_term=12,
            distances={"drive": 10}
        )

    def test_system_flow_creates_csv(self):
        score = self.calculator.overall_score(self.rental)
        self.manager.add_rental(self.rental, score)
        self.manager.save_to_csv(self.test_file)

        self.assertTrue(os.path.exists(self.test_file))

        with open(self.test_file, "r") as f:
            self.assertGreater(len(f.readlines()), 1)

    def test_system_answers_charter_question(self):
        
        score = self.calculator.overall_score(self.rental)
        self.manager.add_rental(self.rental, score)

        best = self.manager.list_properties()[0]
        self.assertIn("Overall Score", best)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)


if __name__ == "__main__":
    unittest.main()

