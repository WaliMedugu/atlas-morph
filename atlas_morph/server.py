"""
ATLAS-MORPH: Competition Inference Server
=========================================
Implements the high-performance inference and tokenization API specification
evaluated by judges in the NeurIPS LLM Efficiency Challenge and NAIC 2026.

Includes both FastAPI integration and a zero-dependency standard library
HTTP server fallback for universal portability across any Python 3 runtime.
"""

import json
import logging
import sys
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from typing import Dict, Any, Optional

# Ensure project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from atlas_morph.engine import load, AtlasMorphEngine
from atlas_morph.api import (
    ProcessRequest,
    ProcessResponse,
    TokenizeRequest,
    TokenizeResponse,
)

logger = logging.getLogger("atlas_morph.server")
logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(levelname)s: %(message)s")


class AtlasRequestHandler(BaseHTTPRequestHandler):
    """
    Zero-dependency HTTP Request Handler implementing the NAIC/NeurIPS
    competition inference specification.
    """

    engine: Optional[AtlasMorphEngine] = None

    def _set_headers(self, status: int = 200, content_type: str = "application/json"):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers(204)

    def do_GET(self):
        if self.path == "/health":
            stats = self.engine.kv_cache.get_stats() if self.engine else {}
            payload = {
                "status": "healthy",
                "engine": "ATLAS-MORPH",
                "model_id": self.engine.model_id if self.engine else "NCAIR1/N-ATLaS",
                "version": "1.0.0",
                "cache_stats": stats,
            }
            self._set_headers(200)
            self.wfile.write(json.dumps(payload).encode("utf-8"))
        elif self.path == "/":
            payload = {
                "title": "ATLAS-MORPH Competition Inference Server",
                "challenge": "NAIC 2026 (NCAIR / NITDA)",
                "endpoints": ["/process", "/tokenize", "/benchmark", "/restore", "/voice", "/health"],
            }
            self._set_headers(200)
            self.wfile.write(json.dumps(payload, indent=2).encode("utf-8"))
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Endpoint not found"}).encode("utf-8"))

    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length)

        try:
            body = json.loads(post_data.decode("utf-8")) if post_data else {}
        except Exception as e:
            self._set_headers(400)
            self.wfile.write(json.dumps({"error": f"Invalid JSON payload: {str(e)}"}).encode("utf-8"))
            return

        if self.path == "/process":
            # Match NeurIPS /process endpoint
            req = ProcessRequest.from_dict(body)
            gen_result = self.engine.generate(
                prompt=req.prompt,
                language=req.language,
                max_new_tokens=req.max_new_tokens,
                temperature=req.temperature,
                seed=req.seed,
            )
            telem = gen_result["telemetry"]
            resp = ProcessResponse(
                text=gen_result["response"],
                tokens_generated=telem["generated_tokens"],
                tokens_per_second=telem["tokens_per_second"],
                latency_ms=telem["total_latency_ms"],
                vram_saved_mb=telem["vram_saved_mb"],
                speedup_factor=telem["speedup_factor"],
            )
            self._set_headers(200)
            self.wfile.write(json.dumps(resp.to_dict()).encode("utf-8"))

        elif self.path == "/tokenize":
            # Match NeurIPS /tokenize endpoint
            req = TokenizeRequest.from_dict(body)
            tok_res = self.engine.tokenize(req.text, language=req.language, return_metrics=True)
            metrics = tok_res["metrics"]
            resp = TokenizeResponse(
                tokens=tok_res["tokens"],
                token_count=tok_res["token_count"],
                fertility=metrics["fertility"],
                token_premium_pct=metrics["token_premium_pct"],
                comparison=self.engine.benchmark_prompt(req.text, language=req.language),
            )
            self._set_headers(200)
            self.wfile.write(json.dumps(resp.to_dict()).encode("utf-8"))

        elif self.path == "/benchmark":
            prompt = body.get("text", "")
            lang = body.get("language")
            comp = self.engine.benchmark_prompt(prompt, language=lang)
            self._set_headers(200)
            self.wfile.write(json.dumps(comp).encode("utf-8"))

        elif self.path == "/restore":
            text = body.get("text", "")
            lang = body.get("language", "yor")
            res = self.engine.restore_diacritics(text, language=lang)
            self._set_headers(200)
            self.wfile.write(json.dumps(res).encode("utf-8"))

        elif self.path == "/voice":
            audio_data = body.get("audio", "")
            lang = body.get("language", "yor")
            res = self.engine.process_voice(audio_data, language=lang)
            self._set_headers(200)
            self.wfile.write(json.dumps(res).encode("utf-8"))

        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Unknown endpoint"}).encode("utf-8"))


def run_server(port: int = 8000, model_id: str = "NCAIR1/N-ATLaS"):
    """
    Launch the ATLAS-MORPH competition inference server.
    """
    logger.info(f"Initializing ATLAS-MORPH engine for model '{model_id}'...")
    engine = load(model_id=model_id, load_in_4bit=True)
    AtlasRequestHandler.engine = engine

    server_address = ("", port)
    httpd = HTTPServer(server_address, AtlasRequestHandler)
    logger.info(f"🚀 ATLAS-MORPH server running at http://localhost:{port}")
    logger.info("Endpoints: /process, /tokenize, /benchmark, /restore, /voice, /health")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logger.info("Shutting down server...")
        httpd.server_close()


if __name__ == "__main__":
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    run_server(port=port)
