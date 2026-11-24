#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

Writes a single short funny line answering a prompt to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Prompt: the excuse a robot vacuum gives after eating a sock.
"""

import os

ENTRY = "The sock attacked first. I have the dust bunnies as witnesses."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
