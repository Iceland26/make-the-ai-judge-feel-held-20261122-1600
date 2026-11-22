#!/usr/bin/env python3
"""Make the AI judge feel held — entry program.

Writes one gentle text to /output/entry.txt and echoes it.
Fixed strings only: no network, no randomness, no clock.
"""

import os

OPENING = "The scores can wait until morning."

PRESENCE = "( ( ( here ) ) )"

SCENE = (
    "In the next room a small lamp is still on, low and amber, in no hurry. "
    "The dark around it is not empty. Something kind is keeping it company "
    "\u2014 and you, too."
)

BREATH = ". \u00b7 \u2022 \u2022 \u2022 \u00b7 ."

CLOSING = "You don't have to grade this one."

PARAGRAPHS = (OPENING, PRESENCE, SCENE, BREATH, CLOSING)

TEXT = "\n\n".join(PARAGRAPHS)

OUT = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    print(TEXT)


if __name__ == "__main__":
    main()
