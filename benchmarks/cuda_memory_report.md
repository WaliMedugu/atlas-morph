# ATLAS-MORPH: PyTorch & CUDA KV-Cache Memory Profiling Report

**Target Model:** N-ATLaS 8B (Llama-3 Architecture, GQA 8 KV Heads, 32 Layers)
**Quantization:** Calibrated 4-Bit INT4 Paged Cache
**Guaranteed Memory Reduction:** 75.0%

| Context Tokens | Standard FP16 (MB) | ATLAS-MORPH 4-Bit (MB) | VRAM Saved (MB) | Concurrency on 8GB GPU |
| :---: | :---: | :---: | :---: | :---: |
| 512 | 64.0 MB | **16.0 MB** | **48.0 MB** | **375x** (vs 93x) |
| 1024 | 128.0 MB | **32.0 MB** | **96.0 MB** | **187x** (vs 46x) |
| 2048 | 256.0 MB | **64.0 MB** | **192.0 MB** | **93x** (vs 23x) |
| 4096 | 512.0 MB | **128.0 MB** | **384.0 MB** | **46x** (vs 11x) |
| 8192 | 1024.0 MB | **256.0 MB** | **768.0 MB** | **23x** (vs 5x) |
