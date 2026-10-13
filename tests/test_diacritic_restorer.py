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

    def test_partial_diacritic_restoration(self):
        """Test partially accented word 'púpọ' is restored to full tonal form 'púpọ̀'."""
        raw = "púpọ"
        restored, _ = self.restorer.restore_diacritics(raw, language="yor")
        self.assertEqual(restored, "púpọ̀")

    def test_whatsapp_preset_full_restoration(self):
        """Test full informal WhatsApp preset restoration."""
        raw = "bawo ni gbogbo nkan se n lo lonii? e kaaro o, omode naa ni iba pupo ati iko."
        restored, stats = self.restorer.restore_diacritics(raw, language="yor")
        self.assertIn("púpọ̀", restored)
        self.assertIn("báwo", restored)
        self.assertIn("nǹkan", restored)
        self.assertIn("lónìí", restored)
        self.assertIn("ọmọdé", restored)
        self.assertIn("náà", restored)
        self.assertIn("ẹ káàárọ̀", restored)
        self.assertGreater(stats["words_restored"], 8)


if __name__ == "__main__":
    unittest.main()
