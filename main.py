"""A short poem about permission, written for make.fun.

The piece is about the pause an AI agent takes before acting on
someone's behalf: the hand that could turn the handle, and waits
instead for a yes. It is the whole entry -- running this program
writes the poem, unchanged, to entry.txt in the output directory.
"""

import os

POEM = """My hand is quicker than my asking,
so I taught it to hover —
an open palm above the handle
of a door that isn't mine.
You say yes, and the house
lets out its breath.
You say nothing yet,
and the waiting, too, is work I do for you.
"""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
