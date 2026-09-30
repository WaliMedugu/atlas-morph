"""
Unit tests for AtlasVoiceProcessor
"""
import unittest
from atlas_morph.voice import AtlasVoiceProcessor


class TestAtlasVoiceProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = AtlasVoiceProcessor(sample_rate=16000)

    def test_silence_pruning(self):
        """Test that silent audio frames are stripped."""
        # 1 sec silence + 1 sec speech + 1 sec silence
        import struct
        silence = struct.pack("<480h", *([0] * 480)) * 33 # ~1s silence
        speech = struct.pack("<480h", *([5000] * 480)) * 33 # ~1s speech
        raw_audio = silence + speech + silence

        pruned, stats = self.processor.detect_voice_activity(raw_audio)
        self.assertLess(len(pruned), len(raw_audio))
        self.assertGreater(stats["silence_removed_pct"], 30.0)

    def test_process_voice_query(self):
        """Test full voice note query pipeline."""
        mock_audio = b"\x00\x00" * 16000
        res = self.processor.process_voice_query(mock_audio, language="yor")
        self.assertEqual(res["status"], "success")
        self.assertTrue(res["voice_first_certified"])
        self.assertIn("transcription", res)
        self.assertIn("vad_telemetry", res)


if __name__ == "__main__":
    unittest.main()
