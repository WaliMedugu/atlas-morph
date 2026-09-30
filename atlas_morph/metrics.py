"""
ATLAS-MORPH: Tokenization Tax & Fertility Metrics Engine
========================================================
Based on the peer-reviewed mathematical formulations from the African Language Tax
research (CipherSenseAI / arXiv:2606.24460) and datalens.africa benchmark standards.

Provides precise empirical quantification of:
- Token Count
- Word Count
- Token Fertility (tokens per word)
- Characters Per Token (CPT)
- Tokenization Tax / Premium vs. English baseline
- Computational and Memory (VRAM) savings
"""

import re
from typing import Dict, Any, Optional
from dataclasses import dataclass, asdict


@dataclass
class TokenMetrics:
    text: str
    language: str
    tokens: int
    words: int
    characters: int
    fertility: float
    cpt: float
    token_premium_pct: float
    estimated_latency_ms: float
    estimated_vram_mb: float

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class AtlasMetrics:
    """
    Evaluation engine measuring the Tokenization Tax across African languages.
    """

    # Baseline English fertility standard (from afri-fertility benchmark on Llama-3 / cl100k)
    ENGLISH_BASELINE_FERTILITY: float = 1.18

    # Llama-3 8B parameters for memory estimation (32 layers, GQA 8 KV heads, d_head 128)
    LLAMA3_BYTES_PER_TOKEN_KV_FP16: float = 2 * 32 * 2 * 8 * 128  # 131,072 bytes/token (~128 KB)
    LLAMA3_BYTES_PER_TOKEN_KV_4BIT: float = 0.5 * 32 * 2 * 8 * 128  # 32,768 bytes/token (~32 KB)

    @staticmethod
    def count_words(text: str) -> int:
        """
        Count words using whitespace and punctuation boundaries.
        Matches standard NLP word-fertility denominator.
        """
        words = re.findall(r"\b\w+\b", text, re.UNICODE)
        return max(1, len(words))

    @staticmethod
    def calculate_fertility(token_count: int, word_count: int) -> float:
        """
        Calculate token fertility = tokens / words.
        """
        if word_count <= 0:
            return 0.0
        return round(token_count / word_count, 3)

    @staticmethod
    def calculate_cpt(char_count: Any, token_count: int) -> float:
        """
        Calculate Characters Per Token (CPT) = characters / tokens.
        Higher CPT means higher information density per token.
        """
        if token_count <= 0:
            return 0.0
        count = len(char_count) if isinstance(char_count, str) else int(char_count)
        return round(count / token_count, 3)

    @classmethod
    def calculate_premium(cls, fertility: float, baseline: Optional[float] = None) -> float:
        """
        Calculate Tokenization Tax / Premium vs. English baseline.
        Premium = ((fertility - baseline_en) / baseline_en) * 100%
        """
        base = baseline or cls.ENGLISH_BASELINE_FERTILITY
        if base <= 0:
            return 0.0
        premium = ((fertility - base) / base) * 100.0
        return round(max(0.0, premium), 1)

    @classmethod
    def calculate_tokenization_tax(cls, fertility: float, baseline: Optional[float] = None) -> float:
        """Alias for calculate_premium."""
        return cls.calculate_premium(fertility, baseline)

    @classmethod
    def evaluate(
        cls,
        text: str,
        token_count: int,
        language: str = "yor",
        use_4bit_cache: bool = True,
        avg_ms_per_token: float = 24.5,
    ) -> TokenMetrics:
        """
        Generate complete empirical metrics payload for an input text and its token count.
        """
        words = cls.count_words(text)
        chars = len(text)
        fertility = cls.calculate_fertility(token_count, words)
        cpt = cls.calculate_cpt(chars, token_count)
        premium = cls.calculate_premium(fertility)

        # Latency estimate based on forward passes
        latency_ms = round(token_count * avg_ms_per_token, 2)

        # KV-Cache memory consumption estimate
        bytes_per_tok = (
            cls.LLAMA3_BYTES_PER_TOKEN_KV_4BIT
            if use_4bit_cache
            else cls.LLAMA3_BYTES_PER_TOKEN_KV_FP16
        )
        vram_mb = round((token_count * bytes_per_tok) / (1024 * 1024), 2)

        return TokenMetrics(
            text=text,
            language=language,
            tokens=token_count,
            words=words,
            characters=chars,
            fertility=fertility,
            cpt=cpt,
            token_premium_pct=premium,
            estimated_latency_ms=latency_ms,
            estimated_vram_mb=vram_mb,
        )

    @classmethod
    def compare(
        cls,
        text: str,
        raw_token_count: int,
        optimized_token_count: int,
        language: str = "yor",
    ) -> Dict[str, Any]:
        """
        Generate a side-by-side comparison between Raw N-ATLaS tokenization
        and ATLAS-MORPH optimized tokenization.
        """
        raw_m = cls.evaluate(text, raw_token_count, language, use_4bit_cache=False)
        opt_m = cls.evaluate(text, optimized_token_count, language, use_4bit_cache=True)

        token_savings = raw_token_count - optimized_token_count
        token_savings_pct = (
            round((token_savings / max(1, raw_token_count)) * 100, 1)
            if raw_token_count > 0
            else 0.0
        )
        speedup_factor = round(
            raw_m.estimated_latency_ms / max(1.0, opt_m.estimated_latency_ms), 2
        )
        memory_savings_pct = round(
            ((raw_m.estimated_vram_mb - opt_m.estimated_vram_mb) / max(0.01, raw_m.estimated_vram_mb))
            * 100,
            1,
        )

        fert_red = round(raw_m.fertility - opt_m.fertility, 2)

        return {
            "language": language,
            "raw": raw_m.to_dict(),
            "optimized": opt_m.to_dict(),
            "raw_tokens_count": raw_token_count,
            "optimized_tokens_count": optimized_token_count,
            "token_reduction_pct": token_savings_pct,
            "token_savings": token_savings,
            "fertility_reduction": fert_red,
            "fertility_raw": raw_m.fertility,
            "fertility_optimized": opt_m.fertility,
            "comparison": {
                "token_savings": token_savings,
                "token_savings_percentage": token_savings_pct,
                "fertility_reduction": fert_red,
                "speedup_factor": f"{speedup_factor}x",
                "memory_savings_percentage": f"{memory_savings_pct}%",
            },
        }
