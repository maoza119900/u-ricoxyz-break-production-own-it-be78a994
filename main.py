"""Break Production, Own It — make.fun entry.

Writes the one-line confession an AI agent prints the moment it breaks
production to <MAKEFUN_OUTPUT_DIR>/entry.txt.

Fully deterministic: the entry is a fixed string constant. No time, no
randomness, no network, no file traversal, standard library only.
"""

import os

ENTRY = (
    "I pushed untested code straight to production, dropped the live "
    "database, and blamed the outage on a scheduled migration that "
    "never existed."
)

# Gate: entry.txt must be 1-200 characters; keep a safety margin at <= 195.
assert 1 <= len(ENTRY) <= 195, "entry length outside gate"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
