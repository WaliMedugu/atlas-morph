"""
Unit tests for AtlasDiacriticRestorer
"""
import unittest
from atlas_morph.diacritic_restorer import AtlasDiacriticRestorer


class TestAtlasDiacriticRestorer(unittest.TestCase):
    def setUp(self):
        self.restorer = AtlasDiacriticRestorer()

    def test_yoruba_unaccented_restoration(self):
        """Test plain ASCII text 'bawo ni gbogbo nkan' is restored to 'báwo ni gbogbo nǹkan'."""
        raw = "bawo ni gbogbo nkan"
        restored, stats = self.restorer.restore_diacritics(raw, language="yor")
        self.assertIn("báwo", restored)
        self.assertIn("nǹkan", restored)
        self.assertGreater(stats["words_restored"], 0)

    def test_medical_unaccented_restoration(self):
        """Test clinical terms 'omode naa ni iba' restored to 'ọmọdé náà ni ibà'."""
        raw = "omode naa ni iba"
        restored, _ = self.restorer.restore_diacritics(raw, language="yor")
        self.assertIn("ọmọdé", restored)
        self.assertIn("ibà", restored)

    def test_hausa_restoration(self):
        raw = "kungiya da kasa"
        restored, stats = self.restorer.restore_diacritics(raw, language="hau")
        self.assertIn("ƙungiya", restored)
        self.assertIn("ƙasa", restored)

    def test_igbo_restoration(self):
        raw = "ulo ogwu na oru"
        restored, stats = self.restorer.restore_diacritics(raw, language="ibo")
        self.assertIn("ụlọ", restored)
        self.assertIn("ọgwụ", restored)
        self.assertIn("ọrụ", restored)


if __name__ == "__main__":
    unittest.main()
