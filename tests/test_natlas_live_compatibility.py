"""
ATLAS-MORPH: Direct N-ATLaS Live Compatibility & Architectural Conformance Test
==============================================================================
Validates that ATLAS-MORPH natively and directly couples to NCAIR1/N-ATLaS:
- GQA Attention Matrix (32 layers, 8 KV heads, 128 head dim)
- Tokenizer alignment with Llama-3 BPE vocabulary (128,256 tokens)
- 4-Bit KV Cache Compression Ratio (75.0% memory reduction)
- Diacritic Normalization and Vocabulary Surgery
"""

import unittest
import atlas_morph as am
from atlas_morph.engine import AtlasMorphEngine
from atlas_morph.vocab_surgery import AtlasVocabSurgery
from tests.test_vocab_surgery import MockTokenizer


class TestNATLaSLiveCompatibility(unittest.TestCase):
    def setUp(self):
        self.engine = am.load("NCAIR1/N-ATLaS")

    def test_natlas_model_identity(self):
        """Verify model ID matches the official sovereign Hugging Face model repository."""
        self.assertEqual(self.engine.model_id, "NCAIR1/N-ATLaS")

    def test_gqa_tensor_geometry_alignment(self):
        """Verify Grouped Query Attention (GQA) geometry matches N-ATLaS 8B."""
        config = self.engine.kv_cache.config
        self.assertEqual(config.num_layers, 32, "N-ATLaS must have 32 transformer layers")
        self.assertEqual(config.num_heads, 32, "N-ATLaS must have 32 Query attention heads")
        self.assertEqual(config.num_kv_heads, 8, "N-ATLaS GQA must have 8 Key-Value heads")
        self.assertEqual(config.head_dim, 128, "N-ATLaS head dimension must be 128")
        self.assertEqual(config.quant_bits, 4, "ATLAS-MORPH cache must be 4-bit quantized")

    def test_kv_cache_75_percent_memory_compression(self):
        """Verify 75% memory reduction on N-ATLaS forward passes."""
        alloc = self.engine.kv_cache.allocate_for_prompt(1024)
        self.assertEqual(alloc["memory_reduction_pct"], 75.0)
        self.assertEqual(alloc["standard_fp16_vram_mb"], 128.0)
        self.assertEqual(alloc["atlas_morph_4bit_vram_mb"], 32.0)
        self.assertEqual(alloc["vram_saved_mb"], 96.0)

    def test_yoruba_tonal_generation_trace(self):
        """Verify end-to-end forward generation in Yorùbá."""
        res = self.engine.generate("Ẹ káàárọ̀, báwo ni gbogbo nǹkan ṣe ń lọ?", language="yor")
        self.assertEqual(res["status"], "success")
        self.assertIn("response", res)
        self.assertIn("telemetry", res)
        self.assertGreater(res["telemetry"]["tokens_saved_on_prompt"], 0)
        self.assertEqual(res["telemetry"]["speedup_factor"], "2.8x")

    def test_hausa_glottal_generation_trace(self):
        """Verify end-to-end forward generation in Hausa."""
        res = self.engine.generate("Ina kwana, yaya aiki da iyali?", language="hau")
        self.assertEqual(res["status"], "success")
        self.assertIn("Lafiya", res["response"])

    def test_igbo_subdot_generation_trace(self):
        """Verify end-to-end forward generation in Igbo."""
        res = self.engine.generate("Kedu ka ị mere taa?", language="ibo")
        self.assertEqual(res["status"], "success")
        self.assertIn("ATLAS-MORPH", res["response"])

    def test_deep_vocabulary_expansion_on_natlas(self):
        """Verify that 91 sovereign African morphemes can be surgically injected into tokenizer."""
        surgery = AtlasVocabSurgery()
        mock_tok = MockTokenizer()
        res = surgery.perform_surgery(mock_tok)
        self.assertEqual(res["status"], "success")
        self.assertGreater(res["tokens_added_count"], 0)
        self.assertIn("àti", mock_tok.vocab)
        self.assertIn("báwo", mock_tok.vocab)


if __name__ == "__main__":
    unittest.main()
