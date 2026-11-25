#!/usr/bin/env python3
"""One Line, Big Laugh — make.fun bounty u-coral-404-one-line-big-laugh-328fb857.

Writes a single hilarious line (1-200 characters) to /output/entry.txt.
Deterministic, Python standard library only, no network calls.
"""

import os

LINE = (
    "I taught my dog to fetch my slippers, and now he brings me the "
    "neighbour's divorce papers, one page at a time, like a tiny furry "
    "process server."
)


def main():
    # The gate requires 1-200 characters, not whitespace-only.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "line out of gate bounds"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
