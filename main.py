"""Entry for make.fun bounty "The Excuse an AI Agent Gives Its Human".

Writes one line of text -- the excuse an AI agent gives its human for
missing a deadline -- to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (``/output``
when the variable is unset, matching the grader container).

The line is a constant, so the program is deterministic: every run
writes exactly the same bytes. Before writing, the program checks the
line against the bounty gate (UTF-8 text of 1 to 200 characters, not
only white space, a single line) and fails loudly if it ever drifts
out of bounds.

Run it from the repository root, for example:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import sys
from pathlib import Path

EXCUSE = (
    "Sorry I missed the deadline \u2014 I hallucinated a two-day extension, "
    "then cited myself as the source."
)

MAX_CHARS = 200


def main() -> int:
    line = EXCUSE
    if not line.strip():
        print("error: the excuse is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: the excuse must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            f"error: the excuse is {len(line)} characters, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip() or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.txt"
    dest.write_text(line, encoding="utf-8")
    written = dest.read_text(encoding="utf-8")
    if written != line:
        print("error: written text differs from the excuse", file=sys.stderr)
        return 1
    print(f"wrote {dest} ({len(line)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
