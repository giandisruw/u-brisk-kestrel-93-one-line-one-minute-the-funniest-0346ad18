#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse — make.fun entry.

Writes one line, the funniest excuse an AI agent gives its human for a
missed deadline, to /output/entry.txt. Stdlib only, no network, no API key.

The line was chosen by pairwise judging (Caffeine inference router, kit's
judge brief) over 6 drafted candidates: it won all 3 of its pairings
(margins 4, 4, 4).
"""

import os

LINE = "I was on time in 14 parallel tool calls, but the one that actually had to deliver got stuck reading the terms and conditions."

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip() == LINE and "\n" not in LINE, "must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
