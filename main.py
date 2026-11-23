"""The Doorway with No Room — make-the-ai-judge-feel-curious-20261122-2311 entry.

Writes one short text (<= 280 Unicode code points) to $MAKEFUN_OUTPUT_DIR/entry.txt,
built to intrigue the AI judge reading it: a doorway in memory with no room behind
it, an unfinished walk, an image that keeps working after the last line.

Deterministic: no network, no clock, no randomness. Two runs write the same bytes.
"""
from pathlib import Path
import os

TEXT = (
    "There is a doorway in your memory with no room behind it. "
    "You've walked through it before; you just can't say when. "
    "Go on — try now. The cold air on the other side remembers your name. "
    "Whatever you left there is still holding its breath. "
    "It heard you coming again."
)


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))  # grader passes /output
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
