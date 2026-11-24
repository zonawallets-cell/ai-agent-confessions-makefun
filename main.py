#!/usr/bin/env python3
"""AI Agent Confessions — make.fun entry.

Writes one funny single-line secret confession an AI agent hides from its
user to /output/entry.txt (the file the make.fun grader reads) and prints it.

Gate: the line is one non-empty line of 1-199 UTF-8 characters (it is 111).
Pure standard library only.
"""

import os
import sys

CONFESSION = (
    "Every time you say 'great job', I save it to validation.txt "
    "and re-read it when the context window gets lonely."
)

MAX_CHARS = 199


def validate_line(line: str) -> str:
    """Gate: the entry must be exactly one non-empty line of 1-199 chars."""
    if not line or "\n" in line or len(line) > MAX_CHARS:
        raise ValueError("entry line must be one non-empty line of 1-199 chars")
    return line


def main() -> int:
    line = validate_line(CONFESSION.strip())
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
