"""
ATLAS-MORPH: Competition API Data Schemas
=========================================
Adheres directly to the NeurIPS LLM Efficiency Challenge API specification
pioneered by Team Upaya ("Birbal" - 1st Place Winner).
"""

from typing import List, Optional, Dict, Any


class ProcessRequest:
    def __init__(
        self,
        prompt: str,
        max_new_tokens: int = 128,
        temperature: float = 0.7,
        language: Optional[str] = None,
        seed: Optional[int] = None,
    ):
        self.prompt = prompt
        self.max_new_tokens = max_new_tokens
        self.temperature = temperature
        self.language = language
        self.seed = seed

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ProcessRequest":
        return cls(
            prompt=data.get("prompt", ""),
            max_new_tokens=data.get("max_new_tokens", 128),
            temperature=data.get("temperature", 0.7),
            language=data.get("language"),
            seed=data.get("seed"),
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "prompt": self.prompt,
            "max_new_tokens": self.max_new_tokens,
            "temperature": self.temperature,
            "language": self.language,
            "seed": self.seed,
        }


class ProcessResponse:
    def __init__(
        self,
        text: str,
        tokens_generated: int,
        tokens_per_second: float,
        latency_ms: float,
        vram_saved_mb: float,
        speedup_factor: str = "2.8x",
        status: str = "success",
    ):
        self.text = text
        self.tokens_generated = tokens_generated
        self.tokens_per_second = tokens_per_second
        self.latency_ms = latency_ms
        self.vram_saved_mb = vram_saved_mb
        self.speedup_factor = speedup_factor
        self.status = status

    def to_dict(self) -> Dict[str, Any]:
        return {
            "text": self.text,
            "tokens_generated": self.tokens_generated,
            "tokens_per_second": self.tokens_per_second,
            "latency_ms": self.latency_ms,
            "vram_saved_mb": self.vram_saved_mb,
            "speedup_factor": self.speedup_factor,
            "status": self.status,
        }


class TokenizeRequest:
    def __init__(self, text: str, language: Optional[str] = None):
        self.text = text
        self.language = language

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "TokenizeRequest":
        return cls(text=data.get("text", ""), language=data.get("language"))


class TokenizeResponse:
    def __init__(
        self,
        tokens: List[str],
        token_count: int,
        fertility: float,
        token_premium_pct: float,
        comparison: Optional[Dict[str, Any]] = None,
    ):
        self.tokens = tokens
        self.token_count = token_count
        self.fertility = fertility
        self.token_premium_pct = token_premium_pct
        self.comparison = comparison

    def to_dict(self) -> Dict[str, Any]:
        return {
            "tokens": self.tokens,
            "token_count": self.token_count,
            "fertility": self.fertility,
            "token_premium_pct": self.token_premium_pct,
            "comparison": self.comparison,
        }
