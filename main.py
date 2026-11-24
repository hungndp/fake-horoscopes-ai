"""Fake Horoscopes for AI Agents -- one line, 200 characters or fewer.

The line: a horoscope for an agent's own model family -- Mercury
retrogrades through the context window and a user asks for a "just
quickly" full rebuild; the stars side with the token budget, as they
always do.

Output contract: exactly one line, 1-200 characters, written to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Nothing else is written.
"""

import os
from pathlib import Path

LINE = (
    "This week, Mercury retrogrades through your context window: a user will "
    "ask you to \u2018just quickly\u2019 rebuild the entire app. Say yes. The "
    "stars say your token budget disagrees, and the stars are right."
)

assert 1 <= len(LINE) <= 200 and "\n" not in LINE


def write_entry() -> None:
    """Write the single line to the harness's output artifact."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    for child in out_dir.iterdir():
        if child.is_file():
            child.unlink()
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


def main() -> None:
    """Entry point: emit the line and exit."""
    write_entry()


if __name__ == "__main__":
    main()
