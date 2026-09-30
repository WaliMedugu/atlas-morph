"""
ATLAS-MORPH
===========
Sovereign Diacritic-Aware Tokenization & Low-Rank Inference Acceleration Suite for N-ATLaS.

Official submission for the National AI Innovation Challenge (NAIC 2026)
Organized by NCAIR, NITDA, FMCIDE, and Awarri Technologies.

Quickstart:
    >>> import atlas_morph as am
    >>> model = am.load("NCAIR1/N-ATLaS")
    >>> result = model.generate("Ẹ káàárọ̀, báwo ni gbogbo nǹkan ṣe ń lọ?")
    >>> print(result["response"])
"""

from atlas_morph.normalizer import AtlasNormalizer
from atlas_morph.tokenizer import AtlasTokenizer
from atlas_morph.metrics import AtlasMetrics, TokenMetrics
from atlas_morph.kv_cache import PagedKVCache, PagedKVCacheConfig
from atlas_morph.engine import AtlasMorphEngine, load

__version__ = "1.0.0"
__author__ = "Medugu Wali (Team Lead), Mutmainnah Magaji, Ojo Timothy"
__supervisor__ = "Mrs. Hauwa Ibrahim Aminu"
__institution__ = "Department of Computer Science, Nile University of Nigeria"
__challenge__ = "NAIC 2026 (NCAIR / NITDA / FMCIDE)"

__all__ = [
    "load",
    "AtlasMorphEngine",
    "AtlasTokenizer",
    "AtlasNormalizer",
    "AtlasMetrics",
    "TokenMetrics",
    "PagedKVCache",
    "PagedKVCacheConfig",
    "__version__",
]
