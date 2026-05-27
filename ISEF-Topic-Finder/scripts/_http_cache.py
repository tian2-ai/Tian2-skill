"""Shared HTTP + cache utilities. stdlib only, no external deps.

HTTP layer uses curl via subprocess. We tried urllib first but Python 3.14
on macOS hits SSL UNEXPECTED_EOF_WHILE_READING against some endpoints
(OpenAlex, NCBI). curl uses system OpenSSL and works reliably.
"""
import hashlib
import json
import os
import shutil
import subprocess
import time
from pathlib import Path


CACHE_ROOT = Path.home() / ".claude/skills/isef-topic-finder/data/cache"
USER_AGENT = "isef-topic-finder/0.1 (mailto:noreply@example.com)"
CURL = shutil.which("curl") or "/usr/bin/curl"


def cache_path(source: str, key: str) -> Path:
    h = hashlib.sha256(key.encode("utf-8")).hexdigest()
    return CACHE_ROOT / source / f"{h}.json"


def read_cache(source: str, key: str, ttl_seconds: int) -> dict | None:
    p = cache_path(source, key)
    if not p.exists():
        return None
    age = time.time() - p.stat().st_mtime
    if age > ttl_seconds:
        return None
    try:
        return json.loads(p.read_text())
    except (json.JSONDecodeError, OSError):
        return None


def write_cache(source: str, key: str, value: dict) -> None:
    p = cache_path(source, key)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, indent=2))


def http_get(url: str, accept: str = "application/json", timeout: int = 20) -> tuple[int, bytes]:
    """Return (status, body). Returns (0, b'') on network error or non-2xx."""
    try:
        proc = subprocess.run(
            [
                CURL, "-sSL", "--max-time", str(timeout),
                "-A", USER_AGENT,
                "-H", f"Accept: {accept}",
                "-w", "\n__HTTP_CODE__:%{http_code}",
                url,
            ],
            capture_output=True,
            timeout=timeout + 5,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError, OSError):
        return 0, b""
    out = proc.stdout
    sep = b"\n__HTTP_CODE__:"
    idx = out.rfind(sep)
    if idx < 0:
        return 0, out
    body = out[:idx]
    code_str = out[idx + len(sep):].strip().decode("ascii", errors="ignore")
    try:
        code = int(code_str)
    except ValueError:
        code = 0
    if 200 <= code < 300:
        return code, body
    return code, b""
