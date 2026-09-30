# Upstream Contribution Proposal: Native Diacritic Normalization & GQA Cache for N-ATLaS

**To:** Silas Adekunle & The Awarri Technologies Engineering Team  
**From:** Department of Computer Science, Nile University of Nigeria, Abuja  
**Lead Contributor:** Medugu Wali (`m.wali@nileuniversity.edu.ng`)  
**Faculty Supervisor:** Mrs. Hauwa Ibrahim Aminu (`hauwa.aminu@nileuniversity.edu.ng`)  
**Date:** 30 September 2026  

---

## Executive Proposal

We propose merging the **ATLAS-MORPH** sovereign diacritic normalizer and low-rank 4-bit Paged Key-Value cache manager directly into the official `NCAIR1/N-ATLaS` Hugging Face model repository and serving runtime.

### Why This Belongs in Upstream N-ATLaS:
1. **Linguistic Sovereignty:** Eliminates the 3.8x token fertility penalty on Yorùbá, Hausa, and Igbo caused by standard Llama-3 BPE byte-fallback fragmentation.
2. **Hardware Democratization:** Allows N-ATLaS to be served on affordable 8GB–12GB GPUs (RTX 3060/4060) across Nigerian universities and startups by slashing active KV memory by 75%.
3. **Turnkey Integration:** We have provided `PATCH_N_ATLAS.diff` which applies directly to the official model repository with zero breaking API changes.

We look forward to collaborating with Awarri Technologies and NCAIR under the National AI Innovation Challenge framework to officially integrate this into N-ATLaS v2 and ATLAS Umoja.
