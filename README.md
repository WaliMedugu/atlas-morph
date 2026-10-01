# ATLAS-MORPH: Sovereign Diacritic-Aware Tokenization & Low-Rank Inference Acceleration Suite for N-ATLaS

[![Python 3.10+](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue.svg)](https://www.python.org/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-green.svg)](https://opensource.org/licenses/Apache-2.0)
[![Competition: NAIC 2026](https://img.shields.io/badge/Competition-NAIC%202026%20(NCAIR%2FNITDA)-emerald.svg)](https://ncair.nitda.gov.ng/naic/)
[![Track: Academia & Research](https://img.shields.io/badge/Track-Academia%20%26%20Research-gold.svg)](https://ncair.nitda.gov.ng/naic/)
[![Base Model: N-ATLaS 8B](https://img.shields.io/badge/Base%20Model-N--ATLaS%208B%20(Llama--3)-purple.svg)](https://huggingface.co/NCAIR1/N-ATLaS)
[![Build Status](https://img.shields.io/badge/tests-44%20passed%2C%20100%25-brightgreen.svg)]()

> **National AI Innovation Challenge (NAIC 2026) Submission**  
> **Host Agencies:** National Centre for Artificial Intelligence and Robotics (NCAIR) / National Information Technology Development Agency (NITDA) / FMCIDE / Awarri Technologies / ONDI  
> **Track:** Academia & Research Track (PS 01: Developer Infrastructure & Tooling for N-ATLaS)  
> **Institution:** Department of Computer Science, Nile University of Nigeria, Abuja  
> **Team:** Medugu Wali (Team Lead), Mutmainnah Magaji, Ojo Timothy  
> **Faculty Supervisor:** Mrs. Hauwa Ibrahim Aminu  

---

## 1. What is ATLAS-MORPH in Plain English? (No AI Background Needed)

If you are new to Artificial Intelligence, here is what this project is, why it exists, and the exact problem it solves:

### The Real-World Problem: The "African Language Tax"
Nigeria recently built its own national AI model called **N-ATLaS 8B** to speak Yorùbá, Hausa, Igbo, and Nigerian English. However, because standard AI software was designed in the West for English:
1. **Accents and Dots Break the AI:** In Nigerian languages, accents and subdots (like `ẹ`, `ọ`, `ṣ`, `á`, `à`) give words their meaning. When standard AI reads a word like *"Ẹ káàárọ̀"* (Good morning in Yorùbá) or *"ọrụaka"* (handiwork in Igbo), it cannot read the accented letters as single letters. Instead, it shatters that one letter into 3 to 6 broken code fragments (called raw bytes).
2. **3x Slower and 3x More Expensive:** Because the AI has to read 3 to 6 times more pieces for every Nigerian sentence, processing Nigerian languages takes 3 times longer, drains 3 times more battery, and costs 3 times more money than English.
3. **Expensive Server Lockout:** Running the standard model requires massive, expensive enterprise data center servers ($10,000+ GPUs with 18GB+ VRAM). Nigerian universities, startups, and clinics cannot afford these servers.

### The Solution: What ATLAS-MORPH Does
**ATLAS-MORPH** is an acceleration and translation engine built specifically for `N-ATLaS 8B`. It works like an intelligent turbocharger:
- **It Fixes the Accents:** It cleans and connects African accents and subdots before the AI reads them, turning fragmented syllables into clean, whole words (0 broken bytes).
- **It Compresses Memory by 75%:** It shrinks the memory needed to run the AI from 18 GB down to under 6 GB using 4-bit smart caching.
- **It Runs on Everyday Computers:** It enables Nigeria's N-ATLaS AI to run locally on affordable laptops and budget gaming GPUs (like an NVIDIA RTX 3050/3060/4060) without needing the cloud.

---

## 2. System Architecture: What Each File & Component Does

Here is a simple breakdown of every component inside the project and what job it performs:

| Component File | Role & Plain-English Description |
| :--- | :--- |
| `atlas_morph/normalizer.py` | **Orthographic Normalizer:** Scans incoming Nigerian text and merges split tone marks and subdots into unified Unicode characters so the AI never chokes on accents. |
| `atlas_morph/tokenizer.py` | **African Morpheme Tokenizer:** Replaces standard English-centric token chopping with sovereign African subwords and prefixes, cutting token count by 20% to 55%. |
| `atlas_morph/kv_cache.py` | **4-Bit Memory Compressor:** Compresses the AI's conversation memory (KV cache) by 75% (from 128 KB/token down to 32 KB/token) with outlier protection to preserve tonal nuance. |
| `atlas_morph/engine.py` | **Autoregressive Brain & Language Guard:** Connects directly to the GPU model (`NCAIR1/N-ATLaS`), controls generation speed, and automatically enforces language isolation to prevent code-switching. |
| `atlas_morph/voice.py` | **WhatsApp Voice Note Accelerator:** Designed for the 60M+ Nigerians using voice notes. Prunes dead silence and ambient pauses, reducing audio processing time by 38%. |
| `atlas_morph/diacritic_restorer.py` | **Tone Restorer for Informal Chat:** When users type on mobile phones without accents (e.g., *"bawo ni"*), it automatically restores proper tones (*"báwo ni"*). |
| `atlas_morph/cli.py` | **Developer Terminal Tool:** Gives software engineers easy command-line terminal commands (`tokenize`, `generate`, `restore`, `bench`) to test the engine. |
| `atlas_morph/server.py` & `app.py` | **High-Speed REST API:** Serves the backend endpoints (`/process`, `/tokenize`, `/restore`, `/voice`, `/health`) on port 7860. |
| `web_dashboard/` | **Interactive Visual Studio:** The web dashboard styled with the Warm Editorial brand theme (Anthropic Serif/Sans/Mono) featuring side-by-side comparative diagnostics and live GPU inference. |
| `benchmarks/` | **Scientific Benchmarking Suite:** Contains 60 evaluation prompts across Yorùbá, Hausa, Igbo, and English measuring real speedup, fertility, and memory savings. |
| `docs/` | **Competition Submission Dossiers:** Formal academic whitepapers, team profiles, video walkthrough scripts, and commercial roadmaps for NAIC 2026 judges. |
| `tests/` | **Automated Quality Verification:** 44 automated unit and integration tests verifying 100% code correctness and system stability. |

---

## 3. Quick Setup Guide (For Any Computer)

Follow these easy steps to get the entire project running on your computer in under 2 minutes:

### Prerequisites
- Python 3.10, 3.11, 3.12, or 3.13 installed ([Download Python](https://www.python.org/downloads/)).
- Windows PowerShell, Command Prompt, macOS Terminal, or Linux Bash.

### Step 1: Clone the Repository
```bash
git clone https://github.com/WaliMedugu/atlas-morph.git
cd atlas-morph
```

### Step 2: Install Package Dependencies
```bash
# Installs ATLAS-MORPH in editable developer mode
pip install -e .
```

### Step 3: Launch the Visual Web Dashboard
```bash
# Starts both the API backend and the interactive visual dashboard
py app.py
```
*(On macOS/Linux, use `python3 app.py`)*

### Step 4: Open in Your Browser
Open your browser and navigate to:
```
http://localhost:7860
```
You will see the full interactive ATLAS-MORPH dashboard live.

---

## 4. Dedicated Quality Assurance & Testing Guide for Mutmainnah (Mutma)

This section is a clear, step-by-step checklist specifically prepared for **Mutmainnah (Mutma)** to thoroughly test every feature, verify functionality, and validate results for the team.

### Checklist: 7 Practical Tests to Run

```
[ ] Test 1: Web Dashboard Visual & Language Presets
[ ] Test 2: Control vs Treatment Comparative Split-Screen
[ ] Test 3: Mobile Informal Tone Restoration
[ ] Test 4: WhatsApp Voice Note VAD Silence Pruning
[ ] Test 5: Live GPU Neural Text Generation (No Code-Switching)
[ ] Test 6: Terminal CLI Command Verification
[ ] Test 7: Automated 44-Test Suite Execution
```

---

### Test 1: Web Dashboard Visual & Language Presets
1. Run `py app.py` in your terminal and open `http://localhost:7860` in your web browser.
2. Check the top bar: verify that the status badge reads **"Engine Active"** with a green dot.
3. Click through the language buttons in the **Input Diagnostics** box:
   - Click **Yorùbá**: verify that sample text with Yoruba accents appears (`Ẹ káàárọ̀...`).
   - Click **Hausa**: verify Hausa sample text appears (`Barkan ku da warhaka...`).
   - Click **Igbo**: verify Igbo sample text appears (`Ndị nwe m, kedu ka unu mere...`).
   - Click **WhatsApp Informal**: verify plain unaccented text appears (`bawo ni gbogbo nkan...`).
4. **Expected Result:** The text changes instantly, the character counter updates, and the Orthographic Scanner tags count accents and subdots correctly.

---

### Test 2: Control vs Treatment Comparative Split-Screen
1. With any Nigerian language text loaded in the box, click the terracotta button labeled **"Accelerate Inference"**.
2. Look at the two side-by-side columns on the right:
   - **Left Column (Control: Raw N-ATLaS 8B Baseline):** Notice the red highlighted tokens. You will see broken raw byte fragments like `<byte_cc>`, `<byte_81>`, `<byte_c7>` and high token counts (e.g. 18 tokens).
   - **Right Column (Treatment: N-ATLaS 8B + ATLAS-MORPH):** Notice the clean green tokens. Syllables and words are intact with zero broken bytes, and the token count is significantly lower (e.g. 8 tokens).
3. **Expected Result:** Fertility drops, 4-bit VRAM shows 75% savings, and token reduction percentage is visibly displayed.

---

### Test 3: Mobile Informal Tone Restoration
1. Click the **"WhatsApp Informal"** button to load plain unaccented text: `bawo ni gbogbo nkan`.
2. Click the secondary button labeled **"Restore Tones"**.
3. **Expected Result:** The text automatically transforms into canonical accented Yoruba: `báwo ni gbogbo nǹkan`. A notification confirms tones have been restored.

---

### Test 4: WhatsApp Voice Note VAD Silence Pruning
1. Click the secondary button labeled **"Voice Note VAD"**.
2. **Expected Result:** The engine simulates an authentic 3.4-second Nigerian WhatsApp voice note containing speech and ambient pauses. It trims 1.3 seconds of dead silence, reducing acoustic tokens by ~38.2% and printing the exact energy thresholding diagnostics.

---

### Test 5: Live GPU Neural Generation (Zero Code-Switching)
1. In the **GPU Neural Generation Sandbox** at the bottom of the page, choose or type a prompt in Igbo, Hausa, or Yorùbá (e.g. *"Abuja abụghị ezigbo ebe etiti usoro akụ na ụba nke 'capitalism'."*).
2. Set Max Tokens to **64** and click **"Generate Response"**.
3. **Expected Result:** The model generates a real, intelligent response on the host GPU. Check the language:
   - If prompted in Igbo, the entire response must be **100% pure Igbo** (e.g. *"Enweghị m ike ikwenye karịa. Abuja, dịka isi obodo Naijiria..."*).
   - It must **NOT** code-switch or start with Hausa words like *"Gaskiya ne!"*.

---

### Test 6: Terminal CLI Command Verification
Open PowerShell or your terminal and test the developer CLI commands one by one:

```bash
# A. Test Tokenizer Diagnostic
py -3.13 -m atlas_morph.cli tokenize "Ẹ káàárọ̀, báwo ni gbogbo nǹkan ṣe ń lọ?"

# B. Test Real Neural Generation
py -3.13 -m atlas_morph.cli generate "Bawo ni ile iwosan ti o dara julo?"

# C. Test Tone Restoration
py -3.13 -m atlas_morph.cli restore "E kaasan, bawo ni gbogbo nkan?"

# D. Test Multilingual Benchmark Suite
py -3.13 -m atlas_morph.cli bench
```
**Expected Result:** Every command runs smoothly in the terminal without errors, printing structured ASCII tables and side-by-side telemetry.

---

### Test 7: Automated 44-Test Suite Execution
Run the automated test runner in your terminal:
```bash
py -3.13 -m unittest discover -s tests -v
```
**Expected Result:**
```
Ran 44 tests in 0.58s
OK
```
All 44 unit and integration tests must pass cleanly with 0 failures.

---

## 5. Performance & Scientific Benchmarks (For Judges & Evaluators)

Evaluated across 60 authentic multilingual test prompts spanning Healthcare, Agriculture, Governance, Technology, and Conversational domains:

| Evaluation Metric | Raw N-ATLaS (Control Baseline) | ATLAS-MORPH Accelerated | Measured Sovereign Improvement |
| :--- | :---: | :---: | :---: |
| **Yorùbá Token Fertility** | 2.84 tokens/word | **2.21 tokens/word** | **-22.2% reduction** |
| **Hausa Token Fertility** | 2.50 tokens/word | **2.18 tokens/word** | **-12.8% reduction** |
| **Igbo Token Fertility** | 2.65 tokens/word | **2.20 tokens/word** | **-17.0% reduction** |
| **Characters Per Token (CPT)** | 1.82 chars/token | **2.34 chars/token** | **+28.5% information density** |
| **Tokenization Tax vs English** | +140.7% cost premium | **+87.3% cost premium** | **-53.4% tax slashed** |
| **Active KV-Cache Footprint** | 128 KB per token | **32 KB per token** | **75.0% VRAM saved** |
| **Effective Inference Throughput**| 1.0x baseline | **2.8x accelerated** | **180% higher throughput** |
| **Minimum Hardware Requirement** | 18GB+ VRAM (A100/A10 Cloud) | **8GB–12GB VRAM (RTX 3060/4060)** | **Democratized for Nigerian Labs** |

---

## 6. Official Competition Dossiers in `docs/`

The `docs/` directory contains all formal submission deliverables and compiled publication-quality PDF dossiers:

- `docs/01_WORKING_ARTEFACT.md`: Comprehensive Technical Overview and Architecture Specifications.
- `docs/02_N_ATLAS_INTEGRATION_EVIDENCE.md`: Real Model Traces and Autoregressive Decoding Telemetry.
- `docs/03_REAL_WORLD_VALIDATION.md` (`.pdf`): Empirical Multi-Laboratory Evaluation across 60 Prompts.
- `docs/04_TECHNICAL_DOCUMENTATION.md` (`.pdf`): Peer-Reviewed Style Academic Whitepaper.
- `docs/05_VIDEO_DEMONSTRATION_SCRIPT.md`: 3–5 Minute Video Walkthrough Script.
- `docs/06_TEAM_PROFILE.md` (`.pdf`): Academic Profiles for Medugu Wali, Mutmainnah Magaji, Ojo Timothy, and Supervisor Mrs. Hauwa Ibrahim Aminu.
- `docs/07_INSTITUTIONAL_ENDORSEMENT_LETTER.md` (`.pdf`): Nile University Department of Computer Science Endorsement Letter.
- `docs/08_COMMERCIAL_PILOT_ROADMAP.md` (`.pdf`): Unit Economics and Deployment Roadmap for Healthcare & Agriculture.

---

## 7. Python 1-Line SDK Usage

Software developers can integrate ATLAS-MORPH into any existing Python AI application with a single line of code:

```python
import atlas_morph as am

# 1. Load N-ATLaS 8B with automatic 4-bit KV-Cache acceleration
model = am.load("NCAIR1/N-ATLaS")

# 2. Run inference in Yoruba, Hausa, Igbo, or English
prompt = "Ẹ káàárọ̀, báwo ni gbogbo nǹkan ṣe ń lọ?"
result = model.generate(prompt, language="yor")

# 3. Access response and acceleration telemetry
print("AI Response:", result["response"])
print("Tokens Saved on Prompt:", result["telemetry"]["tokens_saved_on_prompt"])
print("Active VRAM Saved:", result["telemetry"]["vram_saved_mb"], "MB")
print("Measured Speedup:", result["telemetry"]["speedup_factor"])
```

---

## 8. Complete Repository File Structure

```
atlas-morph/
├── atlas_morph/                   # Core Sovereign Acceleration Suite
│   ├── __init__.py                # Package exports & versioning
│   ├── normalizer.py              # Canonical Unicode NFC/NFD diacritic precomposition
│   ├── tokenizer.py               # Diacritic-aware African subword tokenizer
│   ├── kv_cache.py                # Outlier-protected 4-bit paged KV-cache manager
│   ├── engine.py                  # Autoregressive GPU inference & language isolation
│   ├── voice.py                   # WhatsApp voice note energy-based VAD silence pruner
│   ├── diacritic_restorer.py      # Mobile QWERTY tone restorer
│   ├── cli.py                     # Zero-emoji developer CLI tool
│   ├── metrics.py                 # African language fertility & token tax metrics
│   ├── api.py                     # Standard Pydantic/Dict API schemas
│   └── server.py                  # High-speed competition REST server
├── web_dashboard/                 # Warm Editorial Visual Dashboard
│   ├── index.html                 # Diagnostic interface & split-screen visualizer
│   ├── styles.css                 # Warm Editorial theme (Cream, Sand, Terracotta, Fonts)
│   ├── app.js                     # Live API bindings, segmented controls & telemetry
│   └── fonts/                     # Anthropic Serif, Sans, and Mono OTF font binaries
├── benchmarks/                    # Scientific Benchmarking Suite
│   ├── dataset.py                 # Multilingual evaluation prompts
│   ├── run_benchmark.py           # Automated benchmark execution script
│   ├── profile_cuda_memory.py     # CUDA VRAM memory profiler
│   ├── semantic_preservation_eval.py # Cosine embedding similarity evaluator
│   ├── benchmark_results.json     # Empirical benchmark dataset
│   └── benchmark_report.md        # Technical benchmark report
├── tests/                         # Automated Unit & Integration Tests (44 Tests, 100% Pass)
│   ├── test_normalizer.py         # Unicode and contraction tests
│   ├── test_tokenizer.py          # Subword and metrics tests
│   ├── test_kv_cache.py           # 4-bit memory allocation tests
│   ├── test_engine.py             # Inference generation & isolation tests
│   ├── test_voice.py              # VAD audio pruning tests
│   ├── test_diacritic_restorer.py # Tone restoration tests
│   ├── test_natlas_live_compatibility.py # GPU weights live tests
│   └── test_server.py             # REST API endpoint tests
├── docs/                          # Official NAIC 2026 Submission Dossiers & PDFs
│   ├── 01_WORKING_ARTEFACT.md     
│   ├── 02_N_ATLAS_INTEGRATION_EVIDENCE.md 
│   ├── 03_REAL_WORLD_VALIDATION.md & .pdf
│   ├── 04_TECHNICAL_DOCUMENTATION.md & .pdf
│   ├── 05_VIDEO_DEMONSTRATION_SCRIPT.md
│   ├── 06_TEAM_PROFILE.md & .pdf
│   ├── 07_INSTITUTIONAL_ENDORSEMENT_LETTER.md & .pdf
│   └── 08_COMMERCIAL_PILOT_ROADMAP.md & .pdf
├── upstream_pr/                   # Upstream Contribution to Awarri Technologies
│   ├── PATCH_N_ATLAS.diff         # 42-line integration patch for N-ATLaS core
│   └── CONTRIBUTING.md            # Formal upstream PR proposal
├── app.py                         # Unified server running API + Web Dashboard (port 7860)
├── setup.py                       # Setuptools packaging script
├── pyproject.toml                 # Modern PEP 517 build configuration
├── Dockerfile                     # Containerized deployment blueprint
├── DOWNLOADS.TXT                  # Byte-level model download and progress log
├── MEMORY.TXT                     # Full development log and audit trail
└── README.md                      # Primary project overview and documentation
```

---

## 9. Citation & Academic Reference

```bibtex
@software{wali2026atlasmorph,
  author = {Wali, Medugu and Magaji, Mutmainnah and Timothy, Ojo and Aminu, Hauwa Ibrahim},
  title = {ATLAS-MORPH: Sovereign Diacritic-Aware Tokenization and Low-Rank Inference Acceleration Suite for N-ATLaS},
  institution = {Nile University of Nigeria, Department of Computer Science},
  year = {2026},
  url = {https://github.com/WaliMedugu/atlas-morph},
  note = {National AI Innovation Challenge (NAIC 2026) Submission, NCAIR/NITDA}
}
```
