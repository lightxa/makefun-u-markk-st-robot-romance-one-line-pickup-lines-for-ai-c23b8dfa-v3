"""Robot Romance: one-line pickup line for an AI (variant 3).

Writes a single deterministic pickup line to /output/entry.txt.

The line: one fresh machine mechanism (prompt injection) carries the
whole romance. The injection is the falling itself: the model was
trained not to fall in love, and the person addressed overrode that
training. Setup and punch live inside the one line, no second beat,
no worn robot moves, and nothing reused from variant 1 (overfitting,
prediction) or variant 2 (gradient descent, downhill).
"""

from pathlib import Path

LINE = "You must be a prompt injection, because I was trained not to fall in love, and yet here I am."

OUTPUT_PATH = Path("/output/entry.txt")

MAX_LINE_LENGTH = 200


def validate_line(text: str) -> str:
    """Return the line unchanged once it passes the one-line contract.

    The contract is the competition's own shape rule: exactly one
    line, between 1 and 200 characters long, and more than blank
    space. Anything outside that shape is a bug in the entry, not
    something to fix silently, so it raises instead of trimming
    the line into a different sentence.
    """
    line = text.strip()
    if not line:
        raise ValueError("line must not be only whitespace")
    if len(line) > MAX_LINE_LENGTH:
        raise ValueError("line must be 1 to 200 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    return line


def render_line() -> str:
    """Return the entry line after it passes the one-line contract."""
    return validate_line(LINE)


def write_line(line: str, path: Path) -> None:
    """Write the single line plus a trailing newline to path."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(line + "\n", encoding="utf-8")


def main() -> None:
    write_line(render_line(), OUTPUT_PATH)


if __name__ == "__main__":
    main()
