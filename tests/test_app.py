import os
import time
import urllib.request
import json

BASE_URL = os.getenv("BASE_URL", "http://app:8000")

def wait_ok(path, timeout=30):
    url = f"{BASE_URL}{path}"
    deadline = time.time() + timeout
    last_err = None
    while time.time() < deadline:
        try:
            with urllib.request.urlopen(url, timeout=2) as r:
                return r.read().decode("utf-8")
        except Exception as e:
            last_err = e
            time.sleep(1)
    raise RuntimeError(f"Timeout waiting for {url}: {last_err}")

def test_live():
    body = wait_ok("/live")
    data = json.loads(body)
    assert data["status"] == "alive"

def test_health():
    body = wait_ok("/health")
    data = json.loads(body)
    assert data["app"] == "ok"
