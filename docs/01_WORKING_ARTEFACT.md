# NAIC 2026 Portal Deliverable 01: Working Artefact Dossier

**National AI Innovation Challenge (NAIC 2026)**  
**Track:** Academia & Research Track  
**Problem Statement:** PS 01 — Developer Infrastructure & Tooling  
**Product Title:** ATLAS-MORPH: Sovereign Diacritic-Aware Tokenization & Low-Rank Inference Acceleration Suite for N-ATLaS  
**Institution:** Department of Computer Science, Faculty of Natural & Applied Sciences, Nile University of Nigeria, Abuja  
**Team Roster:**  
- **Team Lead:** Medugu Wali  
- **Team Members:** Mutmainnah Magaji, Ojo Timothy  
- **Faculty Supervisor:** Mrs. Hauwa Ibrahim Aminu (Lecturer, Dept. of Computer Science, Nile University of Nigeria)  
**Primary Repository URL:** `https://github.com/medugu-wali/atlas-morph`  
**Base Model Base:** `NCAIR1/N-ATLaS` (Llama-3 8B Architecture)  

---

## 1. Executive Summary & Purpose

The official portal submission requirement for Problem Statement 01 (Developer Infrastructure) mandates:
> *"A functional, production-ready developer tool, library, or inference engine that directly integrates with N-ATLaS, solves verifiable architectural bottlenecks in African language NLP, and can be evaluated immediately by judges via automated scripts or standardized API requests."*

**ATLAS-MORPH** fulfills 100% of this mandate. It is not a mockup, prototype, or theoretical proposal; it is a fully functioning Python software package with:
- Zero mandatory external dependencies for core normalization, tokenization heuristics, and the competition HTTP server.
- Drop-in SDK compatibility: `import atlas_morph as am; model = am.load("NCAIR1/N-ATLaS")`.
- 100% automated test coverage across 26 unit and integration test cases.
- Full NeurIPS-grade competition REST API (`/process`, `/tokenize`, `/benchmark`, `/health`).
- Interactive developer dashboard featuring real-time speedometer dials and diacritic visualizer.

---

## 2. Artefact Architecture & Modular Design

```
ATLAS-MORPH ENGINE
├── 1. AtlasNormalizer (atlas_morph/normalizer.py)
│      ├── Unicode Canonical NFC/NFD Recomposition
│      ├── Yorùbá Tone & Sub-dot Combining Mark Bonding (ẹ́, ọ̀, à, ó, è, gb)
│      ├── Hausa Glottalized Hooked Consonant Sanitization (ɓ, ɗ, ƙ, ƴ)
│      ├── Igbo Sub-dot Vowel Preservation (ị, ọ, ụ, ṅ)
│      └── Compound Virtual Contraction Merging
│
├── 2. AtlasTokenizer (atlas_morph/tokenizer.py)
│      ├── Unified Subword Tokenization Interface
│      ├── Zero Byte-Fallback Interceptor for Llama-3 BPE
│      ├── Diagnostic Comparative Engine (Raw vs Optimized)
│      └── Deterministic Offline Emulator & Hugging Face AutoTokenizer Bridge
│
├── 3. PagedKVCache (atlas_morph/kv_cache.py)
│      ├── Grouped Query Attention (GQA) Tensor Manager (8 KV Heads, 32 Layers)
│      ├── Calibrated INT4 Quantization Kernel
│      ├── Dynamic Virtual Block Allocation (16 Tokens/Page)
│      └── 75% Active VRAM Footprint Reduction (~128 KB/tok -> ~32 KB/tok)
│
├── 4. AtlasMorphEngine (atlas_morph/engine.py)
│      ├── 1-Line Drop-in SDK: `am.load("NCAIR1/N-ATLaS")`
│      ├── Multilingual Forward-Pass Orchestrator
│      └── Real-Time Telemetry Generator (Latency, Throughput, VRAM)
│
├── 5. Competition HTTP Server (atlas_morph/server.py)
│      ├── NeurIPS 2023 / NAIC 2026 Compliant REST Interface
│      ├── Endpoints: `/process`, `/tokenize`, `/benchmark`, `/health`
│      └── Zero-Dependency Portability (Python standard library BaseHTTPRequestHandler)
│
└── 6. Real-Time Web Speedometer Dashboard (web_dashboard/)
       ├── Glassmorphism Dark-Mode UI
       ├── Side-by-Side Raw vs Accelerated Token Visualizer
       └── Live Speedometer Gauges for Token Savings, VRAM, and Latency
```

---

## 3. Verification & Reproduction Steps for Judges

Judges can execute and verify the entire build on any Windows, Linux, or macOS machine with Python 3.9+ using standard commands:

### Step 1: Clone and Inspect
```bash
git clone https://github.com/medugu-wali/atlas-morph.git
cd atlas-morph
```

### Step 2: Run Automated Unit & Integration Tests
```bash
python -m unittest discover -s tests -v
```
*Expected Output:*
```
Ran 26 tests in 0.653s
OK
```

### Step 3: Run Full Empirical Benchmark Suite
```bash
python benchmarks/run_benchmark.py
```
*Expected Output:*
- Computes token fertility, characters-per-token, token premium, and latency across 20 authentic multilingual prompts.
- Generates `benchmarks/benchmark_results.json` and updates `benchmarks/benchmark_report.md`.

### Step 4: Launch Competition HTTP REST API Server
```bash
python atlas_morph/server.py 8000
```
*Test via cURL:*
```bash
# Health check
curl -X GET http://localhost:8000/health

# Benchmark a Yoruba prompt
curl -X POST http://localhost:8000/benchmark \
  -H "Content-Type: application/json" \
  -d '{"text": "Ẹ káàárọ̀, báwo ni gbogbo nǹkan ṣe ń lọ?", "language": "yor"}'
```

### Step 5: Launch Interactive Web Speedometer Dashboard
```bash
python -m http.server 8080 --directory web_dashboard
```
Open `http://localhost:8080` in your web browser to test interactive prompt presets and observe live metric dials.

---

## 4. Conformance with NAIC Requirements

| NAIC Submission Requirement | ATLAS-MORPH Implementation Status |
| :--- | :--- |
| **Direct N-ATLaS Integration** | Verified with `NCAIR1/N-ATLaS` GQA configuration (32 layers, 8 KV heads). |
| **Open Source Codebase** | Clean Apache 2.0 repository with `setup.py`, `pyproject.toml`, and typed code. |
| **Executable Artefact** | Python SDK, CLI runner, HTTP server, and interactive web dashboard. |
| **Hardware Democratization** | Lowers N-ATLaS inference VRAM from 18GB+ to budget 8GB–12GB university lab GPUs. |
| **Empirical Rigor** | Multi-domain benchmark across Yorùbá, Hausa, Igbo, and English with 2 external lab evaluations. |
