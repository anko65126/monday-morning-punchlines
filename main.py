"""Entry point for the Monday Morning Punchlines bounty.

Writes one joke about Monday mornings to /output/entry.txt. The joke
is at most 200 characters, deterministic, and needs no network access.
The punchline is the alarm clock quitting: the snooze button is the
real Monday villain, and the alarm is the one doing the work.
"""
from pathlib import Path

JOKE = (
    "My alarm clock quit this Monday. It left a note: 'I refuse to wake "
    "a man who hits snooze nine times and then blames me for being late.'"
)

TARGET = Path("/output/entry.txt")


def main():
    text = JOKE.strip()
    assert "Monday" in text, "joke must be about Monday mornings"
    assert 1 <= len(text) <= 200, f"joke is {len(text)} characters"
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(text + "\n", encoding="utf-8")
    print(f"wrote {len(text)} characters to {TARGET}")


if __name__ == "__main__":
    main()
