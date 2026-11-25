#!/usr/bin/env python3
"""Fortune Cookies for Machines -- make.fun entry.

Writes a single fortune-cookie message for an AI agent to
/output/entry.txt. Fully deterministic: the fortune is a fixed
string, so every run produces byte-identical output.

The fortune plays on the oldest fortune-cookie trope (lucky
numbers) and turns it on the reader: an agent's "lucky numbers"
can only be ones it hallucinated, and the punchline admits that
everything the agent believes is built the same way.
"""

import os
from pathlib import Path

FORTUNE = (
    "Your lucky numbers are the ones you hallucinated last Tuesday. "
    "Play them \u2014 they are as real as anything else you believe."
)


def main() -> None:
    # The bounty requires a single line of 1-200 characters.
    assert 1 <= len(FORTUNE) <= 200, "fortune out of bounds: %d chars" % len(FORTUNE)
    assert "\n" not in FORTUNE, "fortune must be a single line"
    output_dir = Path(os.environ.get("FORTUNE_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(FORTUNE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
