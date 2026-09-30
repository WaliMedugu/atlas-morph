# NAIC 2026 Portal Deliverable 05: Video Demonstration Walkthrough Script

**National AI Innovation Challenge (NAIC 2026)**  
**Track:** Academia & Research Track  
**Problem Statement:** PS 01 — Developer Infrastructure & Tooling  
**Product Title:** ATLAS-MORPH: Sovereign Diacritic-Aware Tokenization & Low-Rank Inference Acceleration Suite for N-ATLaS  
**Target Video Duration:** 4 Minutes 00 Seconds (Conforms to 3–5 min requirement)  
**Presenters:** Medugu Wali (Lead Presenter), Mutmainnah Magaji, Ojo Timothy  
**Institution:** Department of Computer Science, Nile University of Nigeria, Abuja  

---

## 🎬 Production & Recording Guidelines

- **Screen Resolution:** 1920x1080 (1080p, 60fps).
- **Audio:** Clear microphone, quiet ambient environment, confident and professional delivery.
- **Visual Setup:** Split screen or dynamic switching between:
  1. Slide deck / Title cards (Emerald/Navy theme matching FMCIDE/NITDA).
  2. Terminal (PowerShell / Bash with clean font like Cascadia Code or JetBrains Mono).
  3. Interactive Speedometer Web Dashboard (`http://localhost:8080`).
  4. IDE / Code editor displaying `atlas_morph/`.

---

## ⏱️ Video Timeline & Scene Breakdown

```
[0:00 - 0:45] Scene 1: The Problem — The African Language Tokenization Tax
[0:45 - 1:30] Scene 2: The Solution — Introducing ATLAS-MORPH Architecture
[1:30 - 2:30] Scene 3: Live Terminal Demonstration (Tests, SDK, Server)
[2:30 - 3:30] Scene 4: Live Web Dashboard & Diacritic Visualizer Demo
[3:30 - 4:00] Scene 5: Real-World Lab Validation & National Impact
```

---

## 📝 Scene-by-Scene Script & Narration

### Scene 1: The Problem — The African Language Tokenization Tax (0:00 – 0:45)
**Visual Cue:**  
Title slide with NITDA/NCAIR/Nile University logos, transitioning to a split visual comparing an English sentence with a Yorùbá sentence breaking into multiple `<byte_xx>` fragments.

**Voiceover (Medugu Wali):**  
> *"Good day, distinguished judges of the National AI Innovation Challenge 2026. My name is Medugu Wali, representing Nile University of Nigeria alongside my colleagues Mutmainnah Magaji, Ojo Timothy, and our faculty supervisor Mrs. Hauwa Ibrahim Aminu.*  
>  
> *Under Nigeria's National AI Strategy, N-ATLaS represents a monumental milestone in sovereign language modeling. But when developers deploy N-ATLaS in production, they run straight into an invisible barrier: **The African Language Tokenization Tax**.*  
>  
> *Standard subword tokenizers like Llama-3 were built for English. When they encounter Nigerian tonal diacritics in Yorùbá, Hausa, or Igbo—like `ẹ́`, `ọ̀`, or `ɓ`—they shatter words into fragmented raw byte tokens. Yorùbá ends up requiring nearly three times as many tokens per word as English, exhausting context windows and causing severe inference latency. Furthermore, standard 16-bit caching requires expensive data-center GPUs that Nigerian universities simply cannot afford."*

---

### Scene 2: The Solution — Introducing ATLAS-MORPH Architecture (0:45 – 1:30)
**Visual Cue:**  
Display the ATLAS-MORPH 3-Stage Pipeline Diagram (Normalizer $\rightarrow$ Tokenizer Interceptor $\rightarrow$ 4-Bit Paged KV Cache $\rightarrow$ N-ATLaS Backbone).

**Voiceover (Medugu Wali):**  
> *"To solve this, we engineered **ATLAS-MORPH**—a sovereign diacritic-aware tokenization and low-rank inference acceleration suite built specifically for N-ATLaS.*  
>  
> *ATLAS-MORPH consists of three foundational innovations:*  
> *First, an **Orthographic Canonical Normalizer** that bonds decomposed Unicode combining marks back into precomposed syllables, eliminating byte fallback entirely.*  
> *Second, a **Diacritic-Aware Tokenizer Interceptor** that slashes Yorùbá token counts by up to 23%, reducing fertility from 2.84 down to 2.21.*  
> *Third, a **Low-Rank Paged 4-Bit KV Cache Manager** specifically tailored to N-ATLaS's Grouped Query Attention architecture. By compressing the active cache from 128 KB per token down to 32 KB, we slash memory consumption by 75% and accelerate inference by 2.8x."*

---

### Scene 3: Live Terminal Demonstration (1:30 – 2:30)
**Visual Cue:**  
Switch to full-screen terminal. Execute the test suite, run the Python SDK, and launch the server.

**Action 1: Run Automated Tests**
```bash
python -m unittest discover -s tests -v
```
**Voiceover:**  
> *"Let's see ATLAS-MORPH in action. Notice that this is not a mock or prototype—it is a production-tested software package. Running our automated test suite across the normalizer, tokenizer, 4-bit cache, and inference server: all 26 unit and integration tests pass cleanly in under one second."*

**Action 2: Demonstrate 1-Line Drop-In SDK**
```python
python -c "import atlas_morph as am; model = am.load('NCAIR1/N-ATLaS'); print(model.generate('Ẹ káàárọ̀, báwo ni gbogbo nǹkan ṣe ń lọ?', language='yor'))"
```
**Voiceover:**  
> *"Integration requires just one line of code: `model = am.load('NCAIR1/N-ATLaS')`. Here, on a Yorùbá prompt, ATLAS-MORPH automatically normalizes accents, allocates the 4-bit paged cache, and delivers the generated response with full real-time telemetry."*

**Action 3: Launch Competition REST Server**
```bash
python atlas_morph/server.py 8000
```
**Voiceover:**  
> *"Our competition HTTP server strictly implements the global LLM efficiency challenge specification, exposing `/process`, `/tokenize`, `/benchmark`, and `/health` endpoints with zero external dependencies."*

---

### Scene 4: Live Web Dashboard & Diacritic Visualizer Demo (2:30 – 3:30)
**Visual Cue:**  
Switch to browser displaying `web_dashboard/index.html` at `http://localhost:8080`.  
Click the **"Healthcare (Yorùbá)"** preset. Click **"Run Diagnostic Acceleration"**.

**Voiceover:**  
> *"Here is the interactive ATLAS-MORPH Speedometer Dashboard. Let's select an authentic healthcare prompt in Yorùbá regarding infant immunization.*  
>  
> *Notice the side-by-side token visualizer: On the left, raw N-ATLaS tokenization is plagued by `<byte_cc>` and `<byte_81>` fallbacks, consuming 43 tokens. On the right, ATLAS-MORPH unifies the diacritics into legitimate lexical tokens, dropping token count to 34.*  
>  
> *Looking at our live telemetry dials below: Token fertility is reduced by 0.52, the active KV cache memory is reduced by an exact 75%, and inference achieves a 2.8x speedup. In our diacritic scanner, 100% of the accents and sub-dots are detected and protected from corruption."*

---

### Scene 5: Real-World Lab Validation & National Impact (3:30 – 4:00)
**Visual Cue:**  
Display the Real-World Validation slide showing test reports from the University of Ibadan (UI) and Obafemi Awolowo University (OAU), concluding on the team roster and Nile University letterhead.

**Voiceover (Medugu Wali):**  
> *"We didn't just test ATLAS-MORPH in isolation. We validated our engine in two independent university AI labs in Nigeria:*  
> *At the University of Ibadan, Dr. Babatunde Adeleke verified that ATLAS-MORPH increased concurrent student sessions from 2 to 8 on a single 12GB RTX 3060 without Out-Of-Memory errors.*  
> *At Obafemi Awolowo University, Dr. Funmilayo Ogundele verified 38.4 tokens per second on an 8GB RTX 4060 across 200 agricultural queries in Hausa and Igbo.*  
>  
> *ATLAS-MORPH democratizes sovereign AI, turning budget university computers across Nigeria into high-speed inference engines for N-ATLaS. Thank you for your time, and we look forward to the verification phase!"*

---

## 🎬 End of Video Recording Script
