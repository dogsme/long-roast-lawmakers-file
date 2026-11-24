#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes exactly one satirical sentence to /output/entry.txt.
"""

import os

LINE = (
    "The same committee that wrote 212 pages of AI law just emailed its staff "
    "a .docx asking if someone could turn it into a PDF."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
