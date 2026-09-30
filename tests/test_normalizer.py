"""
Unit tests for AtlasNormalizer
"""
import unittest
from atlas_morph.normalizer import AtlasNormalizer


class TestAtlasNormalizer(unittest.TestCase):
    def setUp(self):
        self.normalizer = AtlasNormalizer()

    def test_yoruba_decomposed_vowel_recomposition(self):
        """Test decomposed combining accents (e.g. e + dot-below + acute) normalize to NFC precomposed glyph."""
        decomposed = "e\u0323\u0301"  # ẹ́ decomposed
        normalized = self.normalizer.normalize_unicode(decomposed)
        self.assertEqual(normalized, "ẹ́")

        decomposed_o = "o\u0323\u0300"  # ọ̀ decomposed
        normalized_o = self.normalizer.normalize_unicode(decomposed_o)
        self.assertEqual(normalized_o, "ọ̀")

    def test_hausa_hooked_letters(self):
        """Test Hausa hooked glottalized consonants (ɓ, ɗ, ƙ, ƴ)."""
        decomposed_b = "b\u0313"
        self.assertEqual(self.normalizer.normalize_unicode(decomposed_b), "ɓ")

        decomposed_y = "'y"
        self.assertEqual(self.normalizer.normalize_unicode(decomposed_y), "ƴ")

    def test_igbo_subdot_vowels(self):
        """Test Igbo sub-dot vowels (ị, ọ, ụ)."""
        decomposed_i = "i\u0323"
        self.assertEqual(self.normalizer.normalize_unicode(decomposed_i), "ị")
        decomposed_u = "u\u0323"
        self.assertEqual(self.normalizer.normalize_unicode(decomposed_u), "ụ")

    def test_whitespace_and_zero_width_sanitization(self):
        """Test aberrant zero-width characters and excessive spaces are cleaned."""
        raw = "Bawo\u200B  ni   gbogbo   nkan?"
        cleaned = self.normalizer.process(raw)
        self.assertNotIn("\u200B", cleaned)
        self.assertNotIn("  ", cleaned)

    def test_yoruba_contraction_merge(self):
        """Test Yoruba virtual contractions like 'ba wo' -> 'báwo', 'ko si' -> 'kòsí'."""
        text = "Ba wo ni nkan?"
        processed = self.normalizer.process(text, language="yor")
        self.assertTrue(processed.startswith("báwo") or "báwo" in processed.lower())

    def test_diacritic_stats(self):
        """Test diacritic density calculation for telemetry."""
        sample = "Ẹ káàárọ̀ gbogbo ilé. Ọjọ́ rere!"
        stats = self.normalizer.get_diacritic_stats(sample)
        self.assertGreater(stats["yoruba_tones"], 0)
        self.assertGreater(stats["subdots"], 0)


if __name__ == "__main__":
    unittest.main()
