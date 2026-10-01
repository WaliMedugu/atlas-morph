"""
ATLAS-MORPH: Command Line Interface (CLI)
=========================================
Developer tooling and terminal interface for researchers, backend engineers,
and competition evaluators building on N-ATLaS 8B.

Usage:
    py -m atlas_morph.cli tokenize "Báwo ni gbogbo nǹkan?" --compare
    py -m atlas_morph.cli generate "What is the capital of Nigeria?"
    py -m atlas_morph.cli restore "bawo ni gbogbo nkan"
    py -m atlas_morph.cli bench
    py -m atlas_morph.cli serve --port 8000
"""

import sys
import os
import argparse
import json
import time

# Ensure atlas_morph is in path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Ensure Windows terminal outputs UTF-8 cleanly
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

import atlas_morph as am
from atlas_morph.tokenizer import AtlasTokenizer
from atlas_morph.normalizer import AtlasNormalizer
from atlas_morph.diacritic_restorer import AtlasDiacriticRestorer
from atlas_morph.server import run_server


def print_banner():
    banner = """
================================================================================
ATLAS-MORPH: Sovereign N-ATLaS Inference Acceleration Suite
NAIC 2026 | Academia & Research Track | Problem Statement 01: Dev Tooling
================================================================================
"""
    print(banner)


def cmd_tokenize(args):
    print_banner()
    text = args.text
    lang = args.lang

    tokenizer = AtlasTokenizer()
    print(f"Input Text: \"{text}\"")
    print(f"Language Hint: {lang or 'auto'}\n")

    if args.compare:
        res = tokenizer.compare_tokenization(text, language=lang)
        raw = res["raw"]
        opt = res["optimized"]
        comp = res["comparison"]

        print("-" * 80)
        print("SIDE-BY-SIDE TOKENIZATION COMPARISON (CONTROL vs. ATLAS-MORPH)")
        print("-" * 80)
        print(f"CONTROL (Standard Llama-3 BPE):")
        print(f"  * Token Count : {raw['tokens']}")
        print(f"  * Fertility   : {raw['fertility']:.2f} tokens/word")
        print(f"  * Est. Latency: {raw['estimated_latency_ms']} ms")
        print(f"  * Est. KV VRAM: {raw['estimated_vram_mb']} MB")
        print(f"  * Tokens: {res['raw_tokens']}")

        print(f"\nATLAS-MORPH (Sovereign Acceleration):")
        print(f"  * Token Count : {opt['tokens']}")
        print(f"  * Fertility   : {opt['fertility']:.2f} tokens/word")
        print(f"  * Est. Latency: {opt['estimated_latency_ms']} ms")
        print(f"  * 4-Bit KV VRAM: {opt['estimated_vram_mb']} MB")
        print(f"  * Tokens: {res['optimized_tokens']}")

        print("-" * 80)
        print(f"EFFICIENCY GAINS:")
        print(f"  * Token Reduction : {comp['token_savings_percentage']}% ({res['token_savings']} tokens saved)")
        print(f"  * Memory Savings  : {comp['memory_savings_percentage']} (via 4-bit Paged Cache)")
        print(f"  * Speedup Factor  : {comp['speedup_factor']}")
        print("-" * 80)
    else:
        tokens = tokenizer.tokenize(text, language=lang)
        print(f"Tokens ({len(tokens)}): {tokens}")


def cmd_generate(args):
    print_banner()
    prompt = args.prompt
    lang = args.lang
    max_tokens = args.max_tokens

    print(f"Executing Inference: N-ATLaS 8B Foundation Model (Host GPU: RTX 3050)")
    print(f"Prompt: \"{prompt}\"")
    print(f"Max Tokens: {max_tokens} | Language: {lang or 'auto'}\n")

    tokenizer = AtlasTokenizer()
    diag = tokenizer.compare_tokenization(prompt, language=lang)

    model = am.load("NCAIR1/N-ATLaS")
    t0 = time.perf_counter()
    result = model.generate(prompt, language=lang, max_new_tokens=max_tokens)
    elapsed = round((time.perf_counter() - t0) * 1000, 2)

    telem = result["telemetry"]
    print("-" * 80)
    print("N-ATLaS GENERATED OUTPUT:")
    print("-" * 80)
    print(result["response"])
    print("-" * 80)

    print("SIDE-BY-SIDE TELEMETRY (CONTROL vs. ATLAS-MORPH):")
    print("-" * 80)
    print("CONTROL (Standard N-ATLaS Baseline):")
    print(f"  * Prompt Tokens       : {diag['raw_tokens_count']} tokens (with raw byte fragments)")
    print(f"  * Token Fertility     : {diag['fertility_raw']:.2f} tokens/word")
    print(f"  * KV Cache Memory     : {diag['raw']['estimated_vram_mb']} MB (Standard 16-bit)")
    print(f"  * Baseline Latency Est: {diag['raw']['estimated_latency_ms']} ms")

    print("\nTREATMENT (ATLAS-MORPH Acceleration):")
    print(f"  * Prompt Tokens       : {diag['optimized_tokens_count']} tokens (zero byte fragments)")
    print(f"  * Token Fertility     : {diag['fertility_optimized']:.2f} tokens/word")
    print(f"  * KV Cache Memory     : {diag['optimized']['estimated_vram_mb']} MB (4-bit Paged)")
    print(f"  * Generated Tokens    : {telem['generated_tokens']}")
    print(f"  * Generation Speed    : {telem['tokens_per_second']} tokens/sec")
    print(f"  * Total Latency       : {elapsed} ms")

    print("-" * 80)
    print("MEASURED SOVEREIGN GAINS:")
    print(f"  * Prompt Token Reduction: {diag['token_reduction_pct']}% ({diag['token_savings']} tokens saved)")
    print(f"  * KV Cache VRAM Saved   : {telem['vram_saved_mb']} MB (75.0% memory reduction)")
    print(f"  * Acceleration Factor   : {telem['speedup_factor']}")
    print("-" * 80)


def cmd_restore(args):
    print_banner()
    text = args.text
    lang = args.lang or "yor"

    restorer = AtlasDiacriticRestorer()
    restored, stats = restorer.restore_diacritics(text, language=lang)

    print(f"Original Text:  \"{text}\"")
    print(f"Restored Text:  \"{restored}\"")
    print(f"Restored Glyphs: {stats['restored_words']} words, {stats['confidence']} confidence")


def cmd_bench(args):
    print_banner()
    print("Running Full Empirical Benchmark Suite across Multilingual Evaluation Corpus...\n")
    from benchmarks.run_benchmark import run_benchmarks
    run_benchmarks()


def cmd_serve(args):
    print_banner()
    port = args.port or 8000
    print(f"Starting Competition Inference Server on port {port}...")
    run_server(port=port)


def main():
    parser = argparse.ArgumentParser(
        description="ATLAS-MORPH: Sovereign Inference Acceleration CLI for N-ATLaS 8B",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # tokenize command
    tok_parser = subparsers.add_parser("tokenize", help="Tokenize text and inspect byte fragmentation")
    tok_parser.add_argument("text", type=str, help="Input text to tokenize")
    tok_parser.add_argument("--lang", type=str, default=None, help="Language hint ('yor', 'hau', 'ibo', 'eng')")
    tok_parser.add_argument("--compare", action="store_true", default=True, help="Compare Control vs. ATLAS-MORPH")

    # generate command
    gen_parser = subparsers.add_parser("generate", help="Run accelerated inference on N-ATLaS")
    gen_parser.add_argument("prompt", type=str, help="Prompt text")
    gen_parser.add_argument("--lang", type=str, default=None, help="Language hint")
    gen_parser.add_argument("--max-tokens", type=int, default=64, help="Maximum generated tokens")

    # restore command
    res_parser = subparsers.add_parser("restore", help="Restore missing tones and sub-dots on informal text")
    res_parser.add_argument("text", type=str, help="Unaccented ASCII text")
    res_parser.add_argument("--lang", type=str, default="yor", help="Language ('yor', 'hau', 'ibo')")

    # bench command
    subparsers.add_parser("bench", help="Run the full 60-prompt empirical benchmark")

    # serve command
    srv_parser = subparsers.add_parser("serve", help="Launch the REST API server")
    srv_parser.add_argument("--port", type=int, default=8000, help="Port to listen on")

    args = parser.parse_args()

    if args.command == "tokenize":
        cmd_tokenize(args)
    elif args.command == "generate":
        cmd_generate(args)
    elif args.command == "restore":
        cmd_restore(args)
    elif args.command == "bench":
        cmd_bench(args)
    elif args.command == "serve":
        cmd_serve(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
