"""
Unit tests for AtlasTokenizer and AtlasMetrics
"""
import unittest
from atlas_morph.tokenizer import AtlasTokenizer
from atlas_morph.metrics import AtlasMetrics


class TestAtlasTokenizer(unittest.TestCase):
    def setUp(self):
        self.tokenizer = AtlasTokenizer()

    def test_basic_tokenization(self):
        text = "Ẹ káàárọ̀, báwo ni gbogbo nǹkan ṣe ń lọ?"
        tokens = self.tokenizer.tokenize(text, language="yor")
        self.assertIsInstance(tokens, list)
        self.assertGreater(len(tokens), 0)

    def test_tokenize_with_metrics(self):
        text = "Láti inú ìwé ìròyìn lónìí, a rí i pé ètò ọrọ̀-ajé ń tẹ̀síwájú."
        res = self.tokenizer.tokenize(text, language="yor", return_metrics=True)
        self.assertIn("tokens", res)
        self.assertIn("metrics", res)
        self.assertIn("fertility", res["metrics"])
        self.assertIn("cpt", res["metrics"])
        self.assertGreater(res["token_count"], 0)

    def test_compare_tokenization(self):
        text = "Ilé-ìwé gíga jẹ́ ibi pàtàkì fún ìmọ̀ àti ẹ̀kọ́ ní orílẹ̀-èdè Nàìjíríà."
        comp = self.tokenizer.compare_tokenization(text, language="yor")
        self.assertIn("raw_tokens", comp)
        self.assertIn("optimized_tokens", comp)
        self.assertIn("token_reduction_pct", comp)
        self.assertIn("fertility_reduction", comp)
        # Optimized tokens count should be less than or equal to raw tokens
        self.assertLessEqual(comp["optimized_tokens_count"], comp["raw_tokens_count"])

    def test_encode_decode(self):
        text = "Ina da kyau, barka da yamma."
        token_ids = self.tokenizer.encode(text, language="hau")
        self.assertIsInstance(token_ids, list)
        self.assertGreater(len(token_ids), 0)
        decoded = self.tokenizer.decode(token_ids)
        self.assertIsInstance(decoded, str)


class TestAtlasMetrics(unittest.TestCase):
    def test_fertility_calculation(self):
        # 10 words, 15 tokens -> fertility = 1.5
        fertility = AtlasMetrics.calculate_fertility(15, 10)
        self.assertEqual(fertility, 1.5)

    def test_cpt_calculation(self):
        # 50 chars, 10 tokens -> CPT = 5.0
        cpt = AtlasMetrics.calculate_cpt("1234567890" * 5, 10)
        self.assertEqual(cpt, 5.0)

    def test_tokenization_tax(self):
        # Target fertility 2.0 vs English baseline 1.3
        tax = AtlasMetrics.calculate_tokenization_tax(2.0, 1.3)
        self.assertAlmostEqual(tax, 53.8, places=1)


if __name__ == "__main__":
    unittest.main()
