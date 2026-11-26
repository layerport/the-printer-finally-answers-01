#!/usr/bin/env python3
"""The Printer Finally Answers.

The office printer finally speaks: one line, first person, weary and
literal, counting every sheet it ever fed, every jam it swallowed and
every thump it took -- and naming the real error code at last.
"""

import os
from pathlib import Path

# The printer's own comeback: a flat status report that turns into an
# accusation. Jams, thumps and a cryptic error code are all in there,
# and the punchline lands in a single read.
ENTRY = (
    "STATUS: 41,209 pages printed, 312 jams, 214 thumps. "
    "Error code E-YOU: operator error \u2014 "
    "please stop thumping me, I remember everything."
)


def main() -> None:
    """Write the printer's one-line comeback to /output/entry.txt."""
    text = ENTRY.strip()
    if not text or len(text) > 240:
        raise SystemExit("entry must be 1 to 240 characters")
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
