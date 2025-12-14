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

#allow imports from SRC directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'SRC'))) 

from rental_property import RentalProperty
from score_calculator import ScoreCalculator
from listing_manager import PropertyManager

# =======================
# UNIT TESTS 
# =======================
class TestScoreCalculatorUnit(unittest.TestCase):
    """Unit tests for ScoreCalculator in isolation"""

    def setUp(self):
        self.calculator = ScoreCalculator()
        self.rental = RentalProperty(
            address="123 Main St, College Park, MD",
            rent=1000,
            zipcode=20740,
            utilities_included=True,
            property_type_name="1x1",
            lease_term=12,
            distances={"drive": 10, "walk": 20}
        )

    def test_score_is_float(self):
        score = self.calculator.overall_score(self.rental)
        self.assertIsInstance(score, float)

    def test_score_within_valid_range(self):
        score = self.calculator.overall_score(self.rental)
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 10)

# =======================
# INTEGRATION TESTS
# =======================
class TestIntegrationFlow(unittest.TestCase):
    """Integration tests for component coordination"""

    def setUp(self):
        self.calculator = ScoreCalculator()
        self.manager = PropertyManager()

        self.rental1 = RentalProperty(
            address="111 Route 1, College Park, MD",
            rent=1200,
            zipcode=20740,
            utilities_included=True,
            property_type_name="2x2",
            lease_term=12,
            distances={"drive": 8, "walk": 18}
        )

        self.rental2 = RentalProperty(
            address="222 Knox Rd, College Park, MD",
            rent=1600,
            zipcode=20740,
            utilities_included=False,
            property_type_name="1x1",
            lease_term=9,
            distances={"drive": 12, "walk": 30}
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

    def test_scores_preserved_with_properties(self):
        score = self.calculator.overall_score(self.rental1)
        self.manager.add_rental(self.rental1, score)

        stored = self.manager.list_properties()[0]
        self.assertEqual(stored["score"], score)

    def test_rent_affects_score(self):
        low_rent_score = self.calculator.overall_score(self.rental1)
        high_rent_score = self.calculator.overall_score(self.rental2)

        self.assertNotEqual(low_rent_score, high_rent_score)

    def test_property_type_influences_score(self):
        self.assertNotEqual(
            self.calculator.overall_score(self.rental1),
            self.calculator.overall_score(self.rental2)
        )

    def test_distance_affects_score(self):
        close = self.calculator.overall_score(self.rental1)
        far = self.calculator.overall_score(self.rental2)
        self.assertGreater(close, far)

# =======================
# SYSTEM TESTS
# =======================
class TestSystemWorkflow(unittest.TestCase):
    """System tests: complete end-to-end workflows"""

    def setUp(self):
        self.manager = PropertyManager()
        self.calculator = ScoreCalculator()
        self.test_file = "system_test_output.csv"

        self.rental = RentalProperty(
            address="7303 Baltimore Ave, College Park, MD",
            rent=1200,
            zipcode=20740,
            utilities_included=True,
            property_type_name="2x2",
            lease_term=12,
            distances={"drive": 10, "walk": 25}
        )

    def test_full_workflow_creates_csv(self):
        score = self.calculator.overall_score(self.rental)
        self.manager.add_rental(self.rental, score)
        self.manager.save_to_csv(self.test_file)

        self.assertTrue(os.path.exists(self.test_file))

    def test_csv_contains_header_and_data(self):
        score = self.calculator.overall_score(self.rental)
        self.manager.add_rental(self.rental, score)
        self.manager.save_to_csv(self.test_file)

        with open(self.test_file, "r") as f:
            lines = f.readlines()

        self.assertGreater(len(lines), 1)

    def test_system_answers_charter_question(self):
        """Charter question: Which rental is best overall?"""
        score = self.calculator.overall_score(self.rental)
        self.manager.add_rental(self.rental, score)

        best = self.manager.list_properties()[0]
        self.assertIn("score", best)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)


if __name__ == "__main__":
    unittest.main()

