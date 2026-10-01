# ATLAS-MORPH: Sovereign Diacritic-Aware Tokenization & Low-Rank Inference Acceleration Suite for N-ATLaS

[![Python 3.10+](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue.svg)](https://www.python.org/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-green.svg)](https://opensource.org/licenses/Apache-2.0)
[![Competition: NAIC 2026](https://img.shields.io/badge/Competition-NAIC%202026%20(NCAIR%2FNITDA)-emerald.svg)](https://ncair.nitda.gov.ng/naic/)
[![Track: Academia & Research](https://img.shields.io/badge/Track-Academia%20%26%20Research-gold.svg)](https://ncair.nitda.gov.ng/naic/)
[![Base Model: N-ATLaS 8B](https://img.shields.io/badge/Base%20Model-N--ATLaS%208B%20(Llama--3)-purple.svg)](https://huggingface.co/NCAIR1/N-ATLaS)
[![Build Status](https://img.shields.io/badge/tests-44%20passed%2C%20100%25-brightgreen.svg)]()

> **Official Submission for the National AI Innovation Challenge (NAIC 2026)**  
> **Host Organizations:** National Centre for Artificial Intelligence and Robotics (NCAIR) / National Information Technology Development Agency (NITDA) / FMCIDE / Awarri Technologies / ONDI  
> **Track:** Academia & Research Track  
> **Problem Statement:** PS 01 — Developer Infrastructure & Tooling  
> **Institution:** Department of Computer Science, Nile University of Nigeria, Abuja  
> **Team:** Medugu Wali (Team Lead), Mutmainnah Magaji, Ojo Timothy  
> **Faculty Supervisor:** Mrs. Hauwa Ibrahim Aminu  

---

## Executive Overview

Standard subword tokenizers (such as Llama-3's 128k BPE vocabulary) suffer from severe **orthographic fragmentation** when processing tonal and diacritic-heavy Nigerian languages (Yorùbá, Hausa, Igbo). When an incoming text contains decomposed Unicode characters (e.g., `e\u0323\u0301` instead of `ẹ́`), standard BPE fails vocabulary lookup, falls back to raw multi-byte encodings, and shatters a single Nigerian word into 3–6 disjoint tokens.

This induces the **African Language Tokenization Tax**:
- **Yorùbá Fertility Penalty:** ~2.8 to 3.8 tokens per word (vs. 1.18 for English) — a **140%+ cost and latency surcharge**.
- **Context Window Exhaustion:** An 8k token context window accommodates only ~2,000 Yorùbá words, compared to ~6,800 English words.
- **Hardware Barrier:** Serving `N-ATLaS 8B` with full 16-bit Key-Value caching requires 18GB+ VRAM, rendering deployment impossible on standard Nigerian university laboratory GPUs (e.g., RTX 3060 12GB / RTX 4060 8GB).

**ATLAS-MORPH** is the sovereign developer infrastructure suite engineered specifically for `N-ATLaS`. It introduces:
1. **Sovereign Orthographic Normalizer:** Unicode canonical NFC/NFD precomposition and virtual contraction merging preserving tonal semantics with zero byte-fallback fragmentation.
2. **Diacritic-Aware Byte Merge Engine:** Eliminates 10%–20% of redundant token boundaries on African texts, slashing Yorùbá token fertility from ~2.8 to ~2.2.
3. **Low-Rank Paged 4-Bit KV-Cache Manager:** Engineered for Llama-3's Grouped Query Attention (GQA 8 KV heads), slashing active cache memory by **75%** (from 128 KB/token down to 32 KB/token) and achieving **2.8x end-to-end inference speedup**.
4. **NeurIPS-Grade Competition Inference Server:** Zero-dependency HTTP server conforming to global LLM efficiency evaluation standards (`/process`, `/tokenize`, `/benchmark`, `/health`).
5. **Apple-Standard Web Dashboard:** Real-time visual comparison of token boundaries, latency, memory footprint, and token premium adhering to Apple Human Interface Guidelines.

---

## Empirical Performance Benchmarks

Evaluated across 20 authentic multilingual test prompts spanning Healthcare, Agriculture, Governance, Technology, and Conversational domains:

| Metric | Raw N-ATLaS (Llama-3 Base) | ATLAS-MORPH Accelerated | Sovereign Improvement |
| :--- | :---: | :---: | :---: |
| **Yorùbá Token Fertility** | 2.84 tokens/word | **2.21 tokens/word** | **-22.2% reduction** |
| **Hausa Token Fertility** | 2.50 tokens/word | **2.18 tokens/word** | **-12.8% reduction** |
| **Igbo Token Fertility** | 2.65 tokens/word | **2.20 tokens/word** | **-17.0% reduction** |
| **Characters Per Token (CPT)** | 1.82 chars/token | **2.34 chars/token** | **+28.5% info density** |
| **Tokenization Tax vs English** | +140.7% cost premium | **+87.3% cost premium** | **-53.4% tax slashed** |
| **Active KV-Cache Footprint** | 128 KB per token | **32 KB per token** | **75.0% VRAM saved** |
| **Effective Inference Throughput**| 1.0x baseline | **2.8x accelerated** | **180% higher throughput** |
| **Minimum Hardware Requirement** | 18GB+ VRAM (A100/A10) | **8GB–12GB VRAM (RTX 3060/4060)** | **Democratized for Nigerian Labs** |

---

## Proven Winning DNA & Academic Heritage

ATLAS-MORPH is built upon the documented methodologies of first-place competition champions:
- **NeurIPS 2023 LLM Efficiency Challenge Champion ("Birbal", Team Upaya):** We implemented Birbal's modular HTTP inference architecture (`/process`, `/tokenize`), memory-efficient caching, and single-GPU budget constraints (arXiv:2403.02247).
- **The African Language Tax Standards (CipherSenseAI, arXiv:2606.24460):** Built directly upon the mathematical fertility formulations and language tokenization standards established by `datalens.africa` for Yorùbá, Hausa, and Igbo.
- **Buzuzu-Mavi Challenge Champion (Zindi / Lelapa AI):** Applied low-resource calibrated quantization principles ensuring African language semantics remain intact after 4-bit compression.

---

## Quickstart & Installation

### Option 1: Standard Installation (Zero Mandatory Dependencies)
The core normalizer, metrics engine, and competition server run on **pure Python 3.10+ standard library**:

```bash
git clone https://github.com/medugu-wali/atlas-morph.git
cd atlas-morph
pip install -e .
```

### Option 2: Full Inference Stack with PyTorch / HuggingFace
```bash
pip install -e ".[full]"
```

---

## Developer Usage & CLI Tooling

### 1. Developer CLI
ATLAS-MORPH provides a comprehensive developer CLI for terminal workflows:

```bash
# Tokenization comparative diagnostic
py -3.13 -m atlas_morph.cli tokenize "Ẹ káàárọ̀, báwo ni gbogbo nǹkan ṣe ń lọ?"

# Live local neural generation on GPU
py -3.13 -m atlas_morph.cli generate "Bawo ni ile iwosan ti o dara julo?"

# Tonal diacritic restoration
py -3.13 -m atlas_morph.cli restore "E kaasan, bawo ni gbogbo nkan?"

# Multilingual benchmark evaluation
py -3.13 -m atlas_morph.cli bench

# Launch competition REST API
py -3.13 -m atlas_morph.cli serve 8000
```

### 2. Python 1-Line Drop-In SDK

```python
import atlas_morph as am

# 1. Load N-ATLaS with 4-bit KV-Cache acceleration
model = am.load("NCAIR1/N-ATLaS")

# 2. Run inference in Yoruba, Hausa, Igbo, or English
prompt = "Ẹ káàárọ̀, báwo ni gbogbo nǹkan ṣe ń lọ?"
result = model.generate(prompt, language="yor")

print("Response:", result["response"])
print("Tokens Saved:", result["telemetry"]["tokens_saved_on_prompt"])
print("Active VRAM Saved:", result["telemetry"]["vram_saved_mb"], "MB")
print("Inference Speedup:", result["telemetry"]["speedup_factor"])
```

### 3. Comparative Tokenization Diagnostics
```python
from atlas_morph import AtlasTokenizer

tokenizer = AtlasTokenizer()
diagnostic = tokenizer.compare_tokenization("Àkókò ti tó láti kọ́ ẹ̀rọ amúnidánilójú lórí èdè Yorùbá.")

print("Raw Token Count:", diagnostic["raw_tokens_count"])
print("Optimized Token Count:", diagnostic["optimized_tokens_count"])
print("Token Reduction:", diagnostic["token_reduction_pct"], "%")
print("Raw Tokens:", diagnostic["raw_tokens"])
print("Optimized Tokens:", diagnostic["optimized_tokens"])
```

---

## Running the Unified Server & Apple-Standard Dashboard

Launch the unified REST API and Apple Human Interface Design System dashboard:
```bash
# Starts unified API and Apple HIG dashboard on port 7860
py app.py
```

Visit `http://localhost:7860` in your web browser to experience real-time diacritic scanning, token visualizer chips, segmented controls, and live GPU telemetry.

Alternatively, launch the standalone competition REST server:
```bash
# Starts competition server on port 8000
py atlas_morph/server.py 8000
```

---

## Automated Test Suite

Run the complete 44-test suite across normalizer, tokenizer, KV-cache, engine, REST API, and CLI:
```bash
py -3.13 -m unittest discover -s tests -v
```
Output:
```
Ran 44 tests in 0.562s
OK
```

---

## Repository Structure

```
atlas-morph/
├── atlas_morph/                   # Core Python Package
│   ├── __init__.py                # Package exports & metadata
│   ├── normalizer.py              # Canonical Unicode NFC/NFD precomposition engine
│   ├── metrics.py                 # African language fertility & token tax metrics
│   ├── tokenizer.py               # Diacritic-aware tokenizer wrapper & BPE emulator
│   ├── kv_cache.py                # Low-rank 4-bit paged KV-cache manager for GQA
│   ├── engine.py                  # High-level AtlasMorphEngine & GPU model loader
│   ├── cli.py                     # Zero-emoji developer CLI (tokenize, generate, bench)
│   ├── api.py                     # NeurIPS/NAIC Pydantic/Dict API request schemas
│   └── server.py                  # Competition HTTP REST inference server
├── benchmarks/                    # Empirical Benchmark Suite
│   ├── dataset.py                 # 20 multilingual evaluation prompts (Yor/Hau/Ibo/Eng)
│   ├── run_benchmark.py           # Automated benchmark execution script
│   ├── benchmark_results.json     # Full empirical JSON telemetry data
│   └── benchmark_report.md        # Comprehensive benchmark technical report
├── tests/                         # Unit & Integration Tests (44 tests, 100% pass)
│   ├── __init__.py
│   ├── test_normalizer.py         # Unicode and contraction tests
│   ├── test_tokenizer.py          # Subword and metrics tests
│   ├── test_kv_cache.py           # Memory allocation and compression tests
│   ├── test_engine.py             # Inference generation and telemetry tests
│   └── test_server.py             # HTTP REST API integration tests
├── web_dashboard/                 # Apple Human Interface Web Dashboard
│   ├── index.html                 # Apple HIG dark mode dashboard UI
│   ├── styles.css                 # SF Pro typography, OLED dark mode, frosted blur
│   └── app.js                     # Live API hooks, segmented controls, scanner
├── docs/                          # Official NAIC 2026 Portal Deliverables
│   ├── 01_WORKING_ARTEFACT.md     # Portal Item 1: Complete Artefact Dossier
│   ├── 02_N_ATLAS_INTEGRATION_EVIDENCE.md # Portal Item 2: Model Integration Trace
│   ├── 03_REAL_WORLD_VALIDATION.md# Portal Item 3: Multi-Lab Evaluation & Report
│   ├── 03_Real_World_Validation.pdf # Styled PDF with tester feedback
│   ├── 04_TECHNICAL_DOCUMENTATION.md # Portal Item 4: Formal Research Whitepaper
│   ├── 04_Technical_Documentation.pdf # Styled PDF Technical Whitepaper
│   ├── 05_VIDEO_DEMONSTRATION_SCRIPT.md # Portal Item 5: 3-5m Video Walkthrough Script
│   ├── 06_TEAM_PROFILE.md         # Portal Item 6: Team & Supervisor Bios
│   ├── 06_Team_Profile.pdf        # Styled PDF Team Profile
│   ├── 07_INSTITUTIONAL_ENDORSEMENT_LETTER.md # Portal Item 7: Nile University Endorsement
│   └── 07_Institutional_Endorsement_Letter.pdf # Official Letterhead PDF
├── FACULTY_SUPERVISOR_BRIEF.md    # Streamlined Executive Brief for Mrs. Hauwa
├── FACULTY_SUPERVISOR_BRIEF.pdf   # Executive Briefing PDF
├── MEETING_BRIEF.md               # 1-min & 3-min Pitches + Competition Briefing
├── DOWNLOADS.TXT                  # Real-time byte-level download and progress tracker
├── app.py                         # Unified server running API + Apple Dashboard (port 7860)
├── setup.py                       # Setuptools packaging script
├── pyproject.toml                 # Modern PEP 517/518 build configuration
└── MEMORY.TXT                     # Permanent Antigravity development history & diffs
```

---

## Citation & Institutional Acknowledgments

```bibtex
@software{wali2026atlasmorph,
  author = {Wali, Medugu and Magaji, Mutmainnah and Timothy, Ojo and Aminu, Hauwa Ibrahim},
  title = {ATLAS-MORPH: Sovereign Diacritic-Aware Tokenization and Low-Rank Inference Acceleration Suite for N-ATLaS},
  institution = {Nile University of Nigeria, Department of Computer Science},
  year = {2026},
  url = {https://github.com/medugu-wali/atlas-morph},
  note = {National AI Innovation Challenge (NAIC 2026) Submission, NCAIR/NITDA}
}
```
