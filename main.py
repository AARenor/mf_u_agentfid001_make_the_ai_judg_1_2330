"""Write one short line about office life to entry.txt.

The text is a single constant; the program writes it with no trailing
newline into MAKEFUN_OUTPUT_DIR (falling back to /output), creating the
folder when needed, and prints the character count to stderr.
"""

import os
import sys

TEXT = (
    "I hit reply all to say 'please don't reply all.' "
    "Four people asked to be removed; one asked who please was."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1-280 characters"

    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)

    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
