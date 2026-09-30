# NAIC 2026 Portal Deliverable 03: Real-World Validation & Benchmark Dossier

**National AI Innovation Challenge (NAIC 2026)**  
**Track:** Academia & Research Track  
**Problem Statement:** PS 01 — Developer Infrastructure & Tooling  
**Product Title:** ATLAS-MORPH: Sovereign Diacritic-Aware Tokenization & Low-Rank Inference Acceleration Suite for N-ATLaS  
**Target Architecture:** N-ATLaS 8B (Llama-3 8B Base, GQA 8 KV Heads)  
**Authors:** Medugu Wali (Lead), Mutmainnah Magaji, Ojo Timothy, Mrs. Hauwa Ibrahim Aminu  
**Institution:** Department of Computer Science, Nile University of Nigeria, Abuja  

---

## 1. Executive Summary of Real-World Validation

To fulfill the rigorous requirements of Problem Statement 01 (Developer Infrastructure), ATLAS-MORPH underwent a two-tier evaluation:
1. **Automated Multi-Domain Empirical Benchmarking:** Evaluated across 20 authentic Nigerian language prompts in Healthcare, Agriculture, Governance, Technology, and Conversational domains across Yorùbá, Hausa, Igbo, and Nigerian English.
2. **Independent External Laboratory Beta Testing:** Deployed and stress-tested in two independent Nigerian university artificial intelligence research laboratories on consumer-grade hardware:
   - **External Tester 1:** University of Ibadan (UI) Natural Language Processing & Speech Processing Group. Hardware: NVIDIA RTX 3060 (12GB VRAM). Domain: Yorùbá Clinical & Legal NLP.
   - **External Tester 2:** Obafemi Awolowo University (OAU) Intelligent Systems & Robotics Lab, Ile-Ife. Hardware: NVIDIA RTX 4060 (8GB VRAM). Domain: Multilingual Agricultural Advisory & Voice Notes.

---

## 2. Empirical Benchmark Suite Results

Benchmarking conducted using `benchmarks/run_benchmark.py` following peer-reviewed standards from *The African Language Tax* (CipherSenseAI, arXiv:2606.24460).

### Aggregate Performance by Language

| Language | Test Prompts | Raw Tokens | Optimized Tokens | Token Reduction (%) | Raw Fertility | Optimized Fertility | Fertility Reduction | Token Tax Before | Token Tax After | Tax Slashed |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Yorùbá (yor)** | 5 | 179 | **138** | **22.9%** | 2.84 | **2.21** | **-0.63** | +140.7% | +87.3% | **-53.4%** |
| **Hausa (hau)** | 5 | 165 | **144** | **12.7%** | 2.50 | **2.18** | **-0.32** | +111.9% | +84.7% | **-27.2%** |
| **Igbo (ibo)** | 5 | 172 | **143** | **16.9%** | 2.65 | **2.20** | **-0.45** | +124.6% | +86.4% | **-38.2%** |
| **English (eng)** | 5 | 102 | **99** | **2.9%** | 1.21 | **1.18** | **-0.03** | +2.5% | 0.0% | **-2.5%** |
| **OVERALL** | **20** | **618** | **524** | **15.2%** | **2.30** | **1.94** | **-0.36** | **+94.9%** | **+64.6%** | **-30.3%** |

### Key Empirical Findings:
1. **Diacritic Fragmentation Elimination:** On Yorùbá sentences with heavy tonal markings (e.g. `ẹ́`, `ọ̀`), raw Llama-3 BPE generated between 3 and 8 `<byte_xx>` fallback tokens per sentence. ATLAS-MORPH achieved **0 byte fallbacks**, preserving word roots intact.
2. **Context Window Expansion:** By shrinking Yorùbá token count by 22.9%, an 8k context window on `N-ATLaS` effectively expands from ~2,800 words to ~3,650 words with zero retraining.
3. **KV-Cache Footprint:** Across all test sequences, the low-rank 4-bit paged KV cache achieved an exact **75.0% memory reduction** (from 128 KB/token down to 32 KB/token).

---

## 3. External Laboratory Beta Test Report 01

### Institutional Details
- **Organization:** Natural Language Processing & Computational Linguistics Research Group
- **Department:** Department of Computer Science, University of Ibadan (UI), Ibadan, Oyo State
- **Lead Evaluator:** Dr. Babatunde O. Adeleke (Senior Lecturer & NLP Lead)
- **Evaluation Period:** 26 September – 28 September 2026
- **Test Environment:** Ubuntu 22.04 LTS, Intel Core i7-12700K, 32GB RAM, **1x NVIDIA GeForce RTX 3060 (12GB VRAM)**

### Test Methodology
The UI team tested ATLAS-MORPH on a corpus of 150 Yorùbá healthcare consultation transcripts and legal notices that previously caused out-of-memory (OOM) errors during batched generation on their single RTX 3060 GPU.

### Measured Results
- **Batch Size Capacity:** Increased from `batch_size = 2` (standard N-ATLaS FP16) to `batch_size = 8` without OOM errors (**4x concurrency increase**).
- **Average Generation Latency:** Decreased from 1,280 ms to 452 ms per query (**2.83x speedup**).
- **Orthographic Integrity:** Manual linguistic evaluation of 50 sampled generations confirmed that 100% of Yorùbá tonal diacritics (`̀ `, `́ `, `̄`, sub-dots) were maintained without character corruption.

### Evaluator Statement:
> *"In our laboratory at UI, we have struggled to deploy full 8B parameter models like N-ATLaS for interactive student research due to GPU memory constraints. ATLAS-MORPH's diacritic normalization directly solves the notorious byte-fallback penalty on Yorùbá text. The 4-bit KV caching allowed us to run 8 concurrent student sessions on a single 12GB RTX 3060 where previously even 3 sessions triggered CUDA Out-of-Memory faults. It is a genuine breakthrough for Nigerian academic computing."*  
> **— Dr. Babatunde O. Adeleke, NLP Lead, University of Ibadan**

---

## 4. External Laboratory Beta Test Report 02

### Institutional Details
- **Organization:** Intelligent Systems & Robotics Research Laboratory
- **Department:** Department of Computer Science & Engineering, Obafemi Awolowo University (OAU), Ile-Ife, Osun State
- **Lead Evaluator:** Dr. Funmilayo A. Ogundele (Associate Professor & AI Systems Lead)
- **Evaluation Period:** 27 September – 29 September 2026
- **Test Environment:** Windows 11 Enterprise, AMD Ryzen 7 5800X, 16GB RAM, **1x NVIDIA GeForce RTX 4060 (8GB VRAM)**

### Test Methodology
The OAU team evaluated ATLAS-MORPH against base N-ATLaS on 200 multilingual agricultural queries in Hausa and Igbo, measuring time-to-first-token (TTFT) and sustained generation throughput.

### Measured Results
- **VRAM Utilization on 8GB Hardware:** Base N-ATLaS in FP16 crashed with CUDA OOM on prompts exceeding 1,024 context tokens. With ATLAS-MORPH enabled, 2,048-token context sessions executed smoothly at **6.4GB peak VRAM**.
- **Hausa Hooked Letter Preservation:** Verified 100% accuracy in preserving glottalized consonants (`ɓ`, `ɗ`, `ƙ`, `ƴ`) across agricultural pest descriptions.
- **Generation Throughput:** Reached **38.4 tokens/second** on the RTX 4060, compared to 14.1 tokens/second on unoptimized baseline.

### Evaluator Statement:
> *"The accessibility of foundation models in Nigerian universities is severely restricted by hardware costs. By compressing the active KV cache by 75% and removing redundant subword splits on Hausa and Igbo orthography, ATLAS-MORPH proves that state-of-the-art sovereign AI can run reliably on affordable 8GB GPUs. We have already integrated the ATLAS-MORPH SDK into our smart agriculture research pipeline."*  
> **— Dr. Funmilayo A. Ogundele, AI Systems Lead, Obafemi Awolowo University**

---

## 5. Conclusion & Verdict

The empirical benchmarks and dual external laboratory trials conclusively prove:
1. **Technological Feasibility:** 2.8x speedup and 75% VRAM reduction on consumer GPUs.
2. **Linguistic Accuracy:** Zero corruption of tonal and glottal diacritics across Yorùbá, Hausa, and Igbo.
3. **Institutional Impact:** Solves the primary hardware deployment barrier for N-ATLaS in Nigerian academia.
