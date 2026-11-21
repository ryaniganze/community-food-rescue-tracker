import tempfile
import unittest
from pathlib import Path

from database import Database, Food


class FoodRescueTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        db_path = Path(self.temp_dir.name) / "test_food.db"
        self.db = Database(str(db_path))


    def add_sample_food(self):
        sample = Food(
            name="Beans",
            quantity=5,
            unit="kg",
            condition="Packaged",
            location="Community Centre",
            expiry_date="2099-12-31"
        )
        return self.db.add_food(sample)

    def test_add_and_retrieve_food(self):
        food_id = self.add_sample_food()
        food = self.db.get_food_by_id(food_id)
        self.assertIsNotNone(food)
        self.assertEqual(food["name"], "Beans")

    def test_available_food(self):
        self.add_sample_food()
        foods = self.db.get_available_food()
        self.assertEqual(len(foods), 1)
        self.assertEqual(foods[0]["status"], "Available")

    def test_search_by_location(self):
        self.add_sample_food()
        results = self.db.search_food("Community")
        self.assertEqual(len(results), 1)

    def test_update_collection(self):
        food_id = self.add_sample_food()
        changed = self.db.update_collection(
            food_id, "Alex", "2026-11-19"
        )
        self.assertTrue(changed)
        food = self.db.get_food_by_id(food_id)
        self.assertEqual(food["status"], "Collected")


if __name__ == "__main__":
    unittest.main()
    unittest.main()