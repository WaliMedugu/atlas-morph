"""
Integration tests for ATLAS-MORPH HTTP Server
"""
import unittest
import threading
import json
import http.client
from http.server import HTTPServer
from atlas_morph.server import AtlasRequestHandler
from atlas_morph.engine import load


class TestAtlasServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Pick a dedicated test port
        cls.port = 8765
        cls.engine = load("NCAIR1/N-ATLaS")
        AtlasRequestHandler.engine = cls.engine

        cls.httpd = HTTPServer(("127.0.0.1", cls.port), AtlasRequestHandler)
        cls.server_thread = threading.Thread(target=cls.httpd.serve_forever, daemon=True)
        cls.server_thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()
        cls.httpd.server_close()

    def _request(self, method: str, path: str, body: dict = None):
        conn = http.client.HTTPConnection("127.0.0.1", self.port, timeout=5)
        headers = {"Content-Type": "application/json"}
        payload = json.dumps(body) if body else None
        conn.request(method, path, body=payload, headers=headers)
        res = conn.getresponse()
        data = res.read().decode("utf-8")
        conn.close()
        return res.status, json.loads(data)

    def test_health_endpoint(self):
        status, data = self._request("GET", "/health")
        self.assertEqual(status, 200)
        self.assertEqual(data["status"], "healthy")
        self.assertEqual(data["engine"], "ATLAS-MORPH")

    def test_root_endpoint(self):
        status, data = self._request("GET", "/")
        self.assertEqual(status, 200)
        self.assertIn("endpoints", data)

    def test_process_endpoint(self):
        payload = {
            "prompt": "Ẹ káàárọ̀, báwo ni?",
            "language": "yor",
            "max_new_tokens": 30,
        }
        status, data = self._request("POST", "/process", payload)
        self.assertEqual(status, 200)
        self.assertIn("text", data)
        self.assertIn("tokens_generated", data)
        self.assertIn("speedup_factor", data)

    def test_tokenize_endpoint(self):
        payload = {
            "text": "Báwo ni gbogbo nǹkan?",
            "language": "yor",
        }
        status, data = self._request("POST", "/tokenize", payload)
        self.assertEqual(status, 200)
        self.assertIn("tokens", data)
        self.assertIn("token_count", data)
        self.assertIn("fertility", data)

    def test_benchmark_endpoint(self):
        payload = {
            "text": "Ina kwana, yaya aiki?",
            "language": "hau",
        }
        status, data = self._request("POST", "/benchmark", payload)
        self.assertEqual(status, 200)
        self.assertIn("token_reduction_pct", data)


if __name__ == "__main__":
    unittest.main()
