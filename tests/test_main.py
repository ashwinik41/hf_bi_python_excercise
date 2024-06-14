import unittest
from utils.helper_utils import has_chilies, get_total_minutes, determine_difficulty, extract_chilies_recipes, calculate_averages


class TestRecipes(unittest.TestCase):

    def test_has_chilies(self):
        self.assertTrue(has_chilies("Chilies, Salt, Pepper"))
        self.assertTrue(has_chilies("Chiles, Salt, Pepper"))
        self.assertTrue(has_chilies("Chili, Salt, Pepper"))
        self.assertTrue(has_chilies("Chile, Salt, Pepper"))
        self.assertTrue(has_chilies("Chilly, Salt, Pepper"))
        self.assertFalse(has_chilies("Salt, Pepper"))

    def test_get_total_minutes(self):
        self.assertEqual(get_total_minutes("PT1H30M"), 90)
        self.assertEqual(get_total_minutes("PT45M"), 45)
        self.assertEqual(get_total_minutes("PT2H"), 120)
        self.assertEqual(get_total_minutes("PT"), 0)
        self.assertEqual(get_total_minutes(None), 0)

    def test_determine_difficulty(self):
        self.assertEqual(determine_difficulty("PT30M", "PT45M"), "Hard")
        self.assertEqual(determine_difficulty("PT15M", "PT15M"), "Medium")
        self.assertEqual(determine_difficulty("PT10M", "PT15M"), "Easy")
        self.assertEqual(determine_difficulty("", ""), "Easy")
        self.assertEqual(determine_difficulty(None, None), "Easy")

    def test_extract_chilies_recipes(self):
        # Sample data with duplicates
        data = [
            {"url": "1", "ingredients": "Chilies, Salt, Pepper"},
            {"url": "2", "ingredients": "Chiles, Salt, Pepper"},
            {"url": "3", "ingredients": "Chili, Salt, Pepper"},
            {"url": "1", "ingredients": "Chilies, Salt, Pepper"},  # Duplicate of url "1"
            {"url": "4", "ingredients": "Salt, Pepper"}  # No chilies
        ]

        result = extract_chilies_recipes(data)
        print(result)

        # Verify the length of result matches expected number of unique recipes
        self.assertEqual(len(result), 3)

    def test_calculate_averages(self):
        data = [
            {"difficulty": "Hard", "prepTime": "PT1H", "cookTime": "PT30M"},
            {"difficulty": "Hard", "prepTime": "PT1H", "cookTime": "PT45M"},
            {"difficulty": "Medium", "prepTime": "PT30M", "cookTime": "PT15M"},
            {"difficulty": "Easy", "prepTime": "PT10M", "cookTime": "PT15M"},
            {"difficulty": "Easy", "prepTime": "PT5M", "cookTime": "PT10M"}
        ]
        averages = calculate_averages(data)
        expected_averages = [
            {"difficulty": "Hard", "average_total_time": 97},
            {"difficulty": "Medium", "average_total_time": 45},
            {"difficulty": "Easy", "average_total_time": 20}
        ]
        self.assertEqual(len(averages), 3)
        for expected, actual in zip(expected_averages, averages):
            self.assertEqual(expected["difficulty"], actual["difficulty"])
            self.assertEqual(expected["average_total_time"], actual["average_total_time"])


if __name__ == '__main__':
    unittest.main()
