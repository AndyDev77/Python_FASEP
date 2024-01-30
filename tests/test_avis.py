import unittest
from main import extract_avis_from_table

class TestExtractAvis(unittest.TestCase):
    def test_extract_avis(self):
        # Assurez-vous que la fonction extract_avis_from_table fonctionne comme prévu
        # Pour le moment, c'est un exemple très basique
        result = extract_avis_from_table(4, 1, "Avis sur le versement intermédiaire")
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()
