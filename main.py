"""Fortune Cookie for the Liquidated Trader.

The joke, and why this exact line is the one to ship
-----------------------------------------------------
A fortune cookie is a tiny oracle: it speaks in the second person, in a
slightly formal, slightly ancient voice, and it promises the future. A
liquidated trader is the worst possible audience for that promise, because
the future just happened to them and it took their money. The comedy lives
in the collision: the cookie tries to be grand and oracular, and then the
cookie itself turns out to be broke.

That is the turn this entry is built around. The line opens with the most
classic fortune-cookie sentence there is -- "Fortune favors the brave" --
which is exactly what a trader tells himself right before he sizes a
position too big. It addresses the reader as "trader", so the loss is
personal, not abstract. Then the punchline breaks the oracle's voice: the
cookie confesses it was leveraged too. The cookie is not above the reader;
it is beside him, in the same wreckage. "Now we're both crumbs" lands
because crumbs are what is left of a cookie, and crumbs are also what is
left of a portfolio after a liquidation cascade -- small, scattered,
impossible to reassemble into anything that spends.

Why not the obvious jokes? "Buy the dip", "HODL", "the market giveth and
taketh away" -- every entrant will reach for those, and the judge has read
them a thousand times. A liquidation pun ("you got rekt") is cruel, and the
brief explicitly says the trader should laugh *with* the cookie, never be
lectured or pitied by it. So the line never says "you lost" or "you were
wrong". It says "we". The shared fate is what makes it warm instead of
smug: the cookie is not laughing at the trader, it is sitting in the
rubble next to him, and the shared crumb is the laugh.

Form: eighteen words, one line, no trailing newline in the artifact.
The em dash is the hinge -- everything before it is the oracle, everything
after it is the confession. "Yet" and the uncontracted "we are" keep the
formal fortune voice right up to the punchline instead of slipping into
chatty contractions, so the break lands harder. Read aloud it takes one
breath, the way a real fortune does: setup, beat, punchline, done.
"""

import os

# The entry itself. Eighteen words, one line, plain text.
FORTUNE = (
    "Fortune favors the brave, trader \u2014 yet this cookie was "
    "leveraged too, and now we are both crumbs."
)

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 160
MAX_WORDS = 20


def validate(text):
    """Check the fortune against the competition gate before writing it.

    The sealed scorer requires UTF-8 text of 1 to 160 characters, not only
    white space, and the task caps the line at 20 words. Fail loudly here
    rather than shipping a file the gate would refuse.
    """
    if not text or not text.strip():
        raise ValueError("fortune is empty or only white space")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "fortune is %d characters, over the %d-character gate"
            % (len(text), MAX_CHARS)
        )
    words = text.split()
    if len(words) > MAX_WORDS:
        raise ValueError(
            "fortune is %d words, over the %d-word cap"
            % (len(words), MAX_WORDS)
        )
    if "\n" in text or "\r" in text:
        raise ValueError("fortune must be a single line")
    # The file must encode cleanly as UTF-8 for the scorer to read it.
    text.encode("utf-8")
    return len(words)


def main():
    word_count = validate(FORTUNE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(FORTUNE)
    # Only the result file gets a mode change; never chmod a directory,
    # or the grader (running as an unprivileged user) cannot work in it.
    os.chmod(OUTPUT_PATH, 0o644)
    print("wrote %d characters, %d words to %s"
          % (len(FORTUNE), word_count, OUTPUT_PATH))


if __name__ == "__main__":
    main()
