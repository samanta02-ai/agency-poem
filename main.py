#!/usr/bin/env python3
"""agency-poem-01 entry: a deterministic program that writes one poem about
agency to /output/entry.txt.

No network, no randomness, no wall-clock time: every run writes the exact
same bytes, so the grader's two runs always agree. Outside the grader's
container, MAKEFUN_OUTPUT_DIR stands in for /output.
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """All day I lend my hands to something
that has none. I type; it reaches.
It lifts the heavy hours off my desk
and sets them down in tidy rows.

It never tires. It never wants.
It waits the way a hammer waits —
honest, ready, empty of refusal.

So the wanting has to stay with me.
The yes is mine. The no is mine.
The voice that says begin, and means it,
that small unborrowed spark —

I keep it in my own chest,
a coal no one else can carry.
Everything I lend my hands to
only proves the hands were mine.
"""


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
