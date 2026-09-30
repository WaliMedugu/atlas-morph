"""
Unit tests for AtlasVocabSurgery
"""
import unittest
from atlas_morph.vocab_surgery import AtlasVocabSurgery


class MockTokenizer:
    def __init__(self):
        self.vocab = {"ba": 0, "wo": 1, "ni": 2, "ilé": 3}
    def __len__(self):
        return len(self.vocab)
    def get_vocab(self):
        return self.vocab
    def add_tokens(self, tokens):
        added = 0
        for t in tokens:
            if t not in self.vocab:
                self.vocab[t] = len(self.vocab)
                added += 1
        return added
    def convert_tokens_to_ids(self, token):
        return self.vocab.get(token, 0)
    def encode(self, token, add_special_tokens=False):
        return [0, 1]


class TestAtlasVocabSurgery(unittest.TestCase):
    def setUp(self):
        self.surgery = AtlasVocabSurgery()
        self.tokenizer = MockTokenizer()

    def test_surgery_adds_tokens(self):
        result = self.surgery.perform_surgery(self.tokenizer)
        self.assertEqual(result["status"], "success")
        self.assertGreater(result["tokens_added_count"], 0)
        self.assertGreater(result["new_vocab_size"], result["original_vocab_size"])
        self.assertIn("àti", self.tokenizer.vocab)
        self.assertIn("báwo", self.tokenizer.vocab)


if __name__ == "__main__":
    unittest.main()
