#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

Writes a single short funny line answering a prompt to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Prompt: the excuse a robot vacuum gives after eating a sock.
"""

import os

ENTRY = "The sock attacked first. I have the dust bunnies as witnesses."


def check_gate(text: str) -> None:
    """Gate self-check: the entry must be one non-blank line of 1-200 chars.

    The bounty gate rejects blank or over-long output, so catch a bad
    entry locally instead of at submission time.
    """
    if not text.strip():
        raise ValueError("entry must not be blank")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text.encode("utf-8")) <= 200:
        raise ValueError("entry must be 1-200 UTF-8 characters")


def main() -> None:
    # Fail fast on a gate violation before writing anything.
    check_gate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Round-trip check: read back what was written and re-run the gate,
    # so an encoding or filesystem surprise shows up locally, not at submit.
    with open(path, "r", encoding="utf-8") as f:
        check_gate(f.read())
    print(f"wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
