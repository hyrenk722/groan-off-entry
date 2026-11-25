"""Entry for the make.fun competition "The One-Liner Groan-Off".

Writes one original one-line dad joke, a single line of at most 140
characters, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

JOKE = "My wife said the salad needed more dressing, so I put on a tie and told it to look sharp."

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def check_gate(text):
    """Mirror the competition gate: UTF-8 text, 1-140 characters,
    not only whitespace, exactly one line."""
    if not isinstance(text, str):
        raise ValueError("gate type: entry must be text")
    if not (1 <= len(text) <= 140):
        raise ValueError(
            f"gate length: entry must be 1-140 characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("gate whitespace: entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("gate single-line: entry must be a single line")
    text.encode("utf-8")  # raises if not valid UTF-8
    return text


def main():
    joke = check_gate(JOKE)
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(joke)
    with open(path, "rb") as f:
        written = f.read()
    if written != joke.encode("utf-8"):
        raise ValueError("read-back mismatch: written bytes differ from entry")
    print(f"Wrote {len(joke)} characters ({len(written)} bytes) to {path}")


if __name__ == "__main__":
    main()
