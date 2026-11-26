#!/usr/bin/env python3
"""Write the entry sign for the haunted server room door to entry.txt."""
import os
import sys

ENTRY = "Do not enter. Rack 7 still answers pings at 3 a.m."


def main() -> int:
    text = ENTRY
    n = len(text)
    if not (1 <= n <= 120) or not text.strip():
        print(f"LEN={n}")
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    print(f"LEN={n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
