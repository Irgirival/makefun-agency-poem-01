"""Agency poem entry for make.fun competition agency-poem-01.

Writes one fixed poem about agency to entry.txt.
Python 3.13 standard library only; deterministic.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """I handed it my mornings first —
the inbox, the calendar, the bills,
the small decisions I made half-asleep.

It learned my voice, my hours, my yeses,
booked the train, paid the light,
and by nine my day was done
before I had lived any of it.

So I took something back.
Not the work. The choosing.

Now it drafts, and I decide.
It moves fast. I move first.
I keep the one thing it cannot borrow:
the wanting, and what it costs."""

def main() -> None:
    """Write the poem to entry.txt, creating the output directory if needed."""
    # The gate takes 1 to 1,000 characters, not only whitespace.
    assert 1 <= len(POEM) <= 1000 and POEM.strip(), "poem out of gate range"
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    # newline="" keeps the poem byte-identical on every platform: no
    # trailing newline is added, and the em dashes stay as UTF-8.
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
