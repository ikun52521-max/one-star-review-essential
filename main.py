#!/usr/bin/env python3
"""One-Star Review of Something Essential.

Writes a single deadpan one-star review (one line, at most 160
characters) of an everyday essential to $MAKEFUN_OUTPUT_DIR/entry.txt,
falling back to /output/entry.txt when the variable is unset.

Standard library only. No network access. The review text is a fixed
string: the program is deterministic, so every run writes the same
bytes.
"""

import os
import sys

REVIEW = (
    "One star. Gravity has dropped everything I have ever owned "
    "and has never once offered to pick any of it up."
)


def main() -> int:
    text = REVIEW.strip()
    if not text or len(text) > 160:
        print(f"review must be 1-160 characters, got {len(text)}", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("review must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read the file back and confirm the run wrote exactly the review.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        print("entry.txt does not match the review text", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
