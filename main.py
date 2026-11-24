#!/usr/bin/env python3
"""make.fun entry: u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922.

One job title, 60 characters at most, the weirdest one we could think of:
a real-sounding job with one hilariously specific twist. The program
writes the title to /output/entry.txt. Python 3.13, stdlib only,
deterministic, no network.
"""

import os

# Contest gate: one title, 1-60 characters, not only whitespace.
MAX_CHARS = 60
OUTPUT_PATH = "/output/entry.txt"

TITLE = "Professional Excuse Writer for Monday Meetings"


def main() -> None:
    assert 0 < len(TITLE) <= MAX_CHARS, "title must fit the 1-60 char gate"
    assert TITLE.strip(), "title must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
