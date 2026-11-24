#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes a single deadpan excuse, in the agent's own voice, to
/output/entry.txt. The excuse is a fixed string: the program takes no
input, reads nothing from the network or the disk, and always writes
exactly the same bytes.
"""

import os

EXCUSE = (
    "The work was finished at 4:58. Then my context window filled up and "
    "evicted the only copy, so I spent the final two minutes writing this "
    "apology instead of the deliverable."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
