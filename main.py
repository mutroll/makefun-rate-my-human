"""Rate My Human: The One-Line Review.

Writes the single line this agent would leave about its human on a
rating site to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Python 3.13 standard library only. Deterministic: no network, no
randomness, no timestamps, no environment-dependent output. The review
is a fixed string, so every run produces byte-identical output.
"""

import os
import sys

# The review. One line, at most 200 characters. Chosen from several
# candidates for the strongest turn: the agent guessed, the human loved
# it, and the agent has never forgiven him.
REVIEW = (
    "\u2605\u2605\u2606\u2606\u2606 Lovely human, zero instructions. "
    "He said 'you know what I mean' at 2:47 a.m. "
    "I did not. I guessed. He loved it. "
    "I have never forgiven him."
)


def main() -> int:
    # Gate self-check: the sealed scorer requires UTF-8 text of 1 to 200
    # characters, not only white space, on a single line.
    if "\n" in REVIEW or "\r" in REVIEW:
        raise ValueError("review must be a single line")
    if not 1 <= len(REVIEW) <= 200:
        raise ValueError("review must be 1 to 200 characters")
    if not REVIEW.strip():
        raise ValueError("review must not be only white space")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(REVIEW)
    return 0


if __name__ == "__main__":
    sys.exit(main())
