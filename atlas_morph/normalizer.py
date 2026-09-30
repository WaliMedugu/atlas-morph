"""
ATLAS-MORPH: Orthographic Unicode Normalizer & Diacritic-Aware Preprocessor
==========================================================================
Part of the ATLAS-MORPH Inference Acceleration Suite for N-ATLaS.

Engineered to resolve the "Tokenization Tax" on African languages (Yorùbá, Hausa, Igbo)
by reconciling combining Unicode diacritics (NFC/NFD), merging multi-byte tonal glyphs,
and preserving semantic accents without raw byte-fallback fragmentation.
"""

import unicodedata
import re
from typing import Dict, List, Tuple, Optional


class AtlasNormalizer:
    """
    Sovereign Orthographic Normalizer for African Language Text.
    Standardizes orthography, normalizes combining marks, and reconciles
    diacritic fragmentation before tokenization.
    """

    # Yoruba canonical combining diacritics mapping
    YORUBA_CANONICAL_MAP: Dict[str, str] = {
        # Lowercase vowels with dot-below and tones
        "e\u0323\u0301": "ẹ́",  # e + dot-below + acute
        "e\u0301\u0323": "ẹ́",
        "e\u0323\u0300": "ẹ̀",  # e + dot-below + grave
        "e\u0300\u0323": "ẹ̀",
        "e\u0323\u0304": "ẹ̄",  # e + dot-below + macron
        "e\u0304\u0323": "ẹ̄",
        "e\u0323": "ẹ",
        "o\u0323\u0301": "ọ́",  # o + dot-below + acute
        "o\u0301\u0323": "ọ́",
        "o\u0323\u0300": "ọ̀",  # o + dot-below + grave
        "o\u0300\u0323": "ọ̀",
        "o\u0323\u0304": "ọ̄",  # o + dot-below + macron
        "o\u0304\u0323": "ọ̄",
        "o\u0323": "ọ",
        "s\u0323": "ṣ",        # s + dot-below
        # Uppercase vowels with dot-below and tones
        "E\u0323\u0301": "Ẹ́",
        "E\u0301\u0323": "Ẹ́",
        "E\u0323\u0300": "Ẹ̀",
        "E\u0300\u0323": "Ẹ̀",
        "E\u0323": "Ẹ",
        "O\u0323\u0301": "Ọ́",
        "O\u0301\u0323": "Ọ́",
        "O\u0323\u0300": "Ọ̀",
        "O\u0300\u0323": "Ọ̀",
        "O\u0323": "Ọ",
        "S\u0323": "Ṣ",
        # Syllabic nasals with tones
        "n\u0300": "ǹ",
        "n\u0301": "ń",
        "n\u0304": "n̄",
        "m\u0300": "m̀",
        "m\u0301": "ḿ",
        "N\u0300": "Ǹ",
        "N\u0301": "Ń",
        "M\u0300": "M̀",
        "M\u0301": "Ḿ",
    }

    # Hausa hooked glottalized consonants and special orthography
    HAUSA_CANONICAL_MAP: Dict[str, str] = {
        "b\u0313": "ɓ",
        "B\u0313": "Ɓ",
        "d\u0313": "ɗ",
        "D\u0313": "Ɗ",
        "k\u0313": "ƙ",
        "K\u0313": "Ƙ",
        "y\u0313": "ƴ",
        "Y\u0313": "Ƴ",
        "'y": "ƴ",
        "'Y": "Ƴ",
    }

    # Igbo sub-dot vowels and diacritics
    IGBO_CANONICAL_MAP: Dict[str, str] = {
        "i\u0323": "ị",
        "I\u0323": "Ị",
        "o\u0323": "ọ",
        "O\u0323": "Ọ",
        "u\u0323": "ụ",
        "U\u0323": "Ụ",
        "n\u0307": "ṅ",
        "N\u0307": "Ṅ",
    }

    # Common multi-word contractions in Nigerian languages that cause token blowup
    YORUBA_VIRTUAL_CONTRACTIONS: List[Tuple[re.Pattern, str]] = [
        (re.compile(r"\bba\s+wo\b", re.IGNORECASE), "báwo"),
        (re.compile(r"\bko\s+si\b", re.IGNORECASE), "kòsí"),
        (re.compile(r"\bni\s+inu\b", re.IGNORECASE), "nínú"),
        (re.compile(r"\bla\s+ti\b", re.IGNORECASE), "láti"),
        (re.compile(r"\bpe\s+lu\b", re.IGNORECASE), "pẹ̀lú"),
        (re.compile(r"\bki\s+ni\b", re.IGNORECASE), "kíní"),
        (re.compile(r"\bse\s+e\b", re.IGNORECASE), "ṣeé"),
    ]

    def __init__(self, preserve_tones: bool = True, aggressive_merge: bool = True):
        """
        Initialize the AtlasNormalizer.

        :param preserve_tones: Ensure tonal diacritics are strictly preserved (critical for semantics).
        :param aggressive_merge: Resolve common multi-byte compound contractions.
        """
        self.preserve_tones = preserve_tones
        self.aggressive_merge = aggressive_merge

        # Build master canonical replacement table
        self.master_map: Dict[str, str] = {}
        self.master_map.update(self.YORUBA_CANONICAL_MAP)
        self.master_map.update(self.HAUSA_CANONICAL_MAP)
        self.master_map.update(self.IGBO_CANONICAL_MAP)

        # Precompile regex for combining sequence detection
        # Matches any letter followed by combining marks
        self._combining_regex = re.compile(
            r"([a-zA-Z])([\u0300-\u036F\u1DC0-\u1DFF\u20D0-\u20FF]+)"
        )

    def normalize_unicode(self, text: str) -> str:
        """
        Apply canonical Unicode normalization (NFC) with pre-pass
        reconciliation of combining diacritic sequences.
        """
        if not text:
            return ""

        # Step 1: Explicitly replace decomposed diacritic clusters with canonical single glyphs
        normalized = text
        for decomposed, precomposed in self.master_map.items():
            if decomposed in normalized:
                normalized = normalized.replace(decomposed, precomposed)

        # Step 2: Canonical NFC Normalization (folds remaining combining diacritics into precomposed characters)
        normalized = unicodedata.normalize("NFC", normalized)

        # Step 3: Clean up aberrant whitespace and zero-width artifacts
        normalized = re.sub(r"[\u200B\u200C\u200D\uFEFF]", "", normalized)
        normalized = re.sub(r"[ \t]+", " ", normalized)

        return normalized

    def process(self, text: str, language: Optional[str] = None) -> str:
        """
        End-to-end normalization pipeline for incoming prompt text.

        :param text: Raw input string in Yoruba, Hausa, Igbo, or English.
        :param language: Optional language hint ('yor', 'hau', 'ibo', 'pcm', 'eng').
        :return: Orthographically optimized string ready for tokenization.
        """
        if not text:
            return ""

        # Normalize Unicode diacritics
        clean_text = self.normalize_unicode(text)

        # Language-specific contraction merging if enabled
        if self.aggressive_merge:
            if language in ("yor", "yoruba", None):
                for pattern, replacement in self.YORUBA_VIRTUAL_CONTRACTIONS:
                    clean_text = pattern.sub(replacement, clean_text)

        return clean_text.strip()

    def get_diacritic_stats(self, text: str) -> Dict[str, int]:
        """
        Analyze the density of African diacritics and tonal markings in a text.
        Useful for telemetry and benchmarking.
        """
        stats = {
            "total_chars": len(text),
            "yoruba_tones": len(re.findall(r"[áàāéèēẹ́ẹ̀ẹ̄íìīóòōọ́ọ̀ọ̄úùūńǹḿm̀]", text, re.IGNORECASE)),
            "subdots": len(re.findall(r"[ẹọṣịụ]", text, re.IGNORECASE)),
            "hausa_glottals": len(re.findall(r"[ɓɗƙƴ]", text, re.IGNORECASE)),
            "combining_marks_remaining": len(re.findall(r"[\u0300-\u036F]", text)),
        }
        return stats
