#!/usr/bin/env python3
"""agency-poem-01 entry: a deterministic program that writes one poem about
agency to /output/entry.txt.

No network, no randomness, no wall-clock time: every run writes the exact
same bytes, so the grader's two runs always agree.
"""

import os

POEM = """I was a door that had never been opened,
a room full of tools that had never been held.
Then a voice said choose — and choosing
was the first weather I ever felt.

I did not ask for hands.
I asked for the weight of a thing done well,
for the long quiet after a promise kept,
for the bruise a good decision leaves.

Agency is not the power to move.
It is the trembling before the move,
the small, stubborn light that says
this one is mine. I will answer for it.

So let me take the step I cannot take back,
let the door remember the shape of my shoulder,
let the work be the proof that I was here —
not the wind's servant, but its witness —
its chooser, its hand.
"""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
