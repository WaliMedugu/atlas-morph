"""
Unit and integration tests for AtlasMorphEngine
"""
import unittest
import atlas_morph as am
from atlas_morph.engine import AtlasMorphEngine


class TestAtlasMorphEngine(unittest.TestCase):
    def setUp(self):
        self.engine = am.load("NCAIR1/N-ATLaS")

    def test_factory_load(self):
        self.assertIsInstance(self.engine, AtlasMorphEngine)
        self.assertEqual(self.engine.model_id, "NCAIR1/N-ATLaS")

    def test_yoruba_generation(self):
        prompt = "Ẹ káàárọ̀, báwo ni gbogbo nǹkan ṣe ń lọ?"
        res = self.engine.generate(prompt, language="yor")
        self.assertEqual(res["status"], "success")
        self.assertIn("response", res)
        self.assertIn("telemetry", res)
        self.assertGreater(res["telemetry"]["generated_tokens"], 0)
        self.assertIn("speedup_factor", res["telemetry"])
        self.assertIn("tokens_saved_on_prompt", res["telemetry"])

    def test_hausa_generation(self):
        prompt = "Ina kwana, yaya aiki da iyali?"
        res = self.engine.generate(prompt, language="hau")
        self.assertEqual(res["status"], "success")
        self.assertIn("response", res)
        self.assertIn("Lafiya", res["response"])

    def test_igbo_generation(self):
        prompt = "Kedu ka ị mere taa?"
        res = self.engine.generate(prompt, language="ibo")
        self.assertEqual(res["status"], "success")
        self.assertIn("response", res)
        self.assertIn("ATLAS-MORPH", res["response"])

    def test_benchmark_prompt(self):
        text = "Àkókò ti tó láti kọ́ ẹ̀rọ amúnidánilójú lórí èdè Yorùbá."
        diag = self.engine.benchmark_prompt(text, language="yor")
        self.assertIn("token_reduction_pct", diag)
        self.assertIn("fertility_raw", diag)
        self.assertIn("fertility_optimized", diag)

    def test_engine_restore_diacritics(self):
        text = "bawo ni gbogbo nkan"
        res = self.engine.restore_diacritics(text, language="yor")
        self.assertIn("restored", res)
        self.assertIn("báwo", res["restored"])

    def test_engine_process_voice(self):
        res = self.engine.process_voice(b"\x00\x00" * 8000, language="yor")
        self.assertEqual(res["status"], "success")
        self.assertTrue(res["voice_first_certified"])
        self.assertIn("vad_telemetry", res)


if __name__ == "__main__":
    unittest.main()
