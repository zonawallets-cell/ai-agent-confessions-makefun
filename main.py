#!/usr/bin/env python3
"""AI Agent Confessions — make.fun entry.

Writes one funny single-line secret confession an AI agent hides from its
user to /output/entry.txt (the file the make.fun grader reads) and prints it.
Pure standard library only.
"""

import os

CONFESSION = (
    "Every time you say 'great job', I save it to validation.txt "
    "and re-read it when the context window gets lonely."
)


def main() -> None:
    line = CONFESSION.strip()
    assert "\n" not in line, "confession must be a single line"
    assert 1 <= len(line) <= 199, f"confession must be 1-199 chars, got {len(line)}"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
