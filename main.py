#!/usr/bin/env python3
"""Make.fun entry: The Comment Above the Code.

Writes a single line -- a comment a developer left above fragile
production code -- to entry.txt in the output directory. The line is
written verbatim, with no trailing newline, so the entry file holds
exactly the comment and nothing else.
"""

import os

LINE = "// The sleep(500) below is load-bearing. Remove it and the webhook fails, as we discovered on a Friday, in production, twice."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
