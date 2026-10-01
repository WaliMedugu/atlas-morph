"""
ATLAS-MORPH: Hugging Face Spaces & Cloud Deployment Entrypoint
==============================================================
Launches the interactive Speedometer Dashboard and REST API for public cloud hosting.
Compatible with Hugging Face Spaces (Port 7860), RunPod, Railway, and Docker.
"""

import os
import sys
import json
from http.server import HTTPServer, SimpleHTTPRequestHandler
import urllib.parse

# Ensure Windows terminal outputs UTF-8 cleanly
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Ensure atlas_morph is in path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import atlas_morph as am
from atlas_morph.engine import load
from atlas_morph.server import AtlasRequestHandler

PORT = int(os.environ.get("PORT", 7860))
DASHBOARD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "web_dashboard"))


class UnifiedSpaceHandler(AtlasRequestHandler):
    """
    Combines the REST API endpoints (/process, /tokenize, /benchmark, /health)
    with static serving of the interactive web dashboard.
    """

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        # REST API endpoints
        if path in ("/health", "/process", "/tokenize", "/benchmark", "/restore", "/voice"):
            super().do_GET()
            return

        # Static file serving for web dashboard
        if path == "/" or path == "":
            file_path = os.path.join(DASHBOARD_DIR, "index.html")
            content_type = "text/html; charset=utf-8"
        else:
            file_path = os.path.join(DASHBOARD_DIR, path.lstrip("/"))
            if path.endswith(".css"):
                content_type = "text/css; charset=utf-8"
            elif path.endswith(".js"):
                content_type = "application/javascript; charset=utf-8"
            elif path.endswith(".json"):
                content_type = "application/json; charset=utf-8"
            elif path.endswith(".otf"):
                content_type = "font/otf"
            elif path.endswith(".woff2"):
                content_type = "font/woff2"
            elif path.endswith(".woff"):
                content_type = "font/woff"
            elif path.endswith(".ttf"):
                content_type = "font/ttf"
            elif path.endswith(".svg"):
                content_type = "image/svg+xml"
            elif path.endswith(".png"):
                content_type = "image/png"
            elif path.endswith(".jpg") or path.endswith(".jpeg"):
                content_type = "image/jpeg"
            else:
                content_type = "text/plain; charset=utf-8"

        if os.path.exists(file_path) and os.path.isfile(file_path):
            self._set_headers(200, content_type=content_type)
            with open(file_path, "rb") as f:
                self.wfile.write(f.read())
        else:
            # Fallback to API root or 404
            super().do_GET()


def main():
    print("=" * 80)
    print("ATLAS-MORPH: SOVEREIGN INFERENCE ACCELERATION SUITE")
    print(f"Deploying unified cloud interface on port {PORT}...")
    print("=" * 80)

    # Initialize engine
    engine = load("NCAIR1/N-ATLaS", load_in_4bit=True)
    UnifiedSpaceHandler.engine = engine

    server_address = ("", PORT)
    httpd = HTTPServer(server_address, UnifiedSpaceHandler)

    print(f"Cloud App & Speedometer Dashboard running at: http://localhost:{PORT}")
    print("API Endpoints available: /health, /process, /tokenize, /benchmark, /restore, /voice")
    print("Hugging Face Spaces compatible: YES")
    print("=" * 80)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server shutdown requested.")
        httpd.server_close()


if __name__ == "__main__":
    main()
