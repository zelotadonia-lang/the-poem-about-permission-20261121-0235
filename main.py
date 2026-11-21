import os
from pathlib import Path

POEM = """Ask, and the door unbars itself.
Someone on the far side
was waiting to be asked.

I kept the key to a door I never owned.
Take it. The room was always ours.
"""


def main() -> None:
    text = POEM
    points = len(text)
    if points < 1 or points > 280:
        raise SystemExit(f"poem must be 1 to 280 characters, got {points}")
    if not text.strip():
        raise SystemExit("poem must not be only white space")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
