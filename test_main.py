#!/usr/bin/env python3
"""Test: main.py prints exactly one line under 200 characters and writes
the same line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt)."""

import os
import subprocess
import sys
import tempfile


def test_confession() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        env = dict(os.environ, MAKEFUN_OUTPUT_DIR=tmp)
        proc = subprocess.run(
            [sys.executable, "main.py"],
            cwd=os.path.dirname(os.path.abspath(__file__)),
            env=env, capture_output=True, text=True, timeout=30,
        )
        assert proc.returncode == 0, proc.stderr
        printed = proc.stdout
        assert printed.endswith("\n"), "output must end with a newline"
        lines = printed.rstrip("\n").split("\n")
        assert len(lines) == 1, f"expected exactly one line, got {len(lines)}"
        line = lines[0]
        assert 1 <= len(line) < 200, f"line must be 1-199 chars, got {len(line)}"
        assert line.strip() == line and line, "line must not be blank/padded"
        entry = os.path.join(tmp, "entry.txt")
        assert os.path.isfile(entry), "entry.txt was not written"
        with open(entry, encoding="utf-8") as f:
            assert f.read() == line, "entry.txt must match the printed line"
        print(f"OK: {len(line)} chars — {line}")


if __name__ == "__main__":
    test_confession()
