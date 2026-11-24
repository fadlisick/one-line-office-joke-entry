#!/usr/bin/env python3
"""One-Line Office Joke: emit one office joke as entry.txt.

Deliberately tiny: one constant, one guard, one write. The joke is a
single line of at most 200 characters, written with no trailing newline.
"""

import os
from pathlib import Path

JOKE = "My performance review said I need to be more visible, so I now attend every meeting in a hi-vis vest."
LIMIT = 200


def checked(line: str) -> str:
    stripped = line.strip()
    if not stripped:
        raise ValueError("joke must not be empty")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("joke must be a single line")
    if len(stripped) > LIMIT:
        raise ValueError(f"joke is {len(stripped)} chars, over the {LIMIT} limit")
    return stripped


def destination() -> Path:
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(base) / "entry.txt"


def main() -> int:
    text = checked(JOKE)
    target = destination()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    if target.read_text(encoding="utf-8") != text:
        raise ValueError("written entry does not match the joke")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
