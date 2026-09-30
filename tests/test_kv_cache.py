"""
Unit tests for PagedKVCache
"""
import unittest
from atlas_morph.kv_cache import PagedKVCache, PagedKVCacheConfig


class TestPagedKVCache(unittest.TestCase):
    def setUp(self):
        self.config = PagedKVCacheConfig(
            num_layers=32,
            num_heads=32,
            num_kv_heads=8,
            head_dim=128,
            block_size=16,
            quant_bits=4,
        )
        self.cache = PagedKVCache(self.config)

    def test_allocation_for_prompt(self):
        alloc = self.cache.allocate_for_prompt(512)
        self.assertEqual(alloc["prompt_tokens"], 512)
        # 512 tokens / 16 block_size = 32 blocks
        self.assertEqual(alloc["allocated_blocks"], 32)
        self.assertEqual(alloc["memory_reduction_pct"], 75.0)
        self.assertGreater(alloc["standard_fp16_vram_mb"], alloc["atlas_morph_4bit_vram_mb"])

    def test_append_generated_tokens(self):
        self.cache.allocate_for_prompt(256)
        expanded = self.cache.append_generated_tokens(64)
        self.assertEqual(expanded["total_active_tokens"], 320)
        # 320 / 16 = 20 blocks
        self.assertEqual(expanded["total_blocks"], 20)

    def test_stats_and_clear(self):
        self.cache.allocate_for_prompt(100)
        stats = self.cache.get_stats()
        self.assertEqual(stats["active_tokens"], 100)
        self.assertEqual(stats["memory_savings_pct"], "75%")

        self.cache.clear()
        self.assertEqual(self.cache.active_tokens, 0)
        self.assertEqual(self.cache.allocated_blocks, 0)


if __name__ == "__main__":
    unittest.main()
