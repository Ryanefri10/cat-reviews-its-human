# Cat review entry (Python 3.13, standard library only).
# Writes one funny single-line one-star review from a house cat about
# its human to /output/entry.txt (MAKEFUN_OUTPUT_DIR stands in for
# /output outside the grader's container).
# Deterministic: same constant, no network, no randomness, no clock.

import os
from pathlib import Path

# Revised line: "a performance" -> "a show" — tighter wording, and the
# shorter middle clause lands the final sting ("restore the balance")
# harder. Same shape: deadpan one-star review, specific complaints
# (the food bowl, the laptop keyboard), cat-logic justification.
REVIEW = (
    "One star. He fills my bowl, then watches me eat like I owe him "
    "a show. I knocked his laptop off the table to restore the balance."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(REVIEW, encoding="utf-8")


if __name__ == "__main__":
    main()
