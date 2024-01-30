import unittest
from main import extract_montant_from_table

class TestExtractMontant(unittest.TestCase):
    def test_extract_montant(self):
        # Assurez-vous que la fonction extract_montant_from_table fonctionne comme prévu
        # Pour le moment, c'est un exemple très basique
        result = extract_montant_from_table(1, 2, "Montant du FASEP")
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()
