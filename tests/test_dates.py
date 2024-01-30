import unittest
from main import extract_dates_from_table

class TestExtractDates(unittest.TestCase):
    def test_extract_dates(self):
        # Assurez-vous que la fonction extract_dates_from_table fonctionne comme prévu
        # Pour le moment, c'est un exemple très basique
        result = extract_dates_from_table(3, 1, ["Date de signature"])
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

if __name__ == '__main__':
    unittest.main()
