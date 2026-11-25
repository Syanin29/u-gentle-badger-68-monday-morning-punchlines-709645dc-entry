import os

LINE = "Monday morning: the microwave beeped 4 times, sparked once, and Kevin's leftover fish curry exploded into a Jackson Pollock spelling \"Q1 Targets\" in cumin."


def main():
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read-back verification: the written file must be exactly LINE,
    # one line, and within the 200-char limit of the bounty.
    with open(path, encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match LINE"
    assert 1 <= len(written) <= 200, f"line length out of range: {len(written)} chars"
    assert written.count("\n") == 0, "entry.txt must be a single line"
    assert written.strip() != "", "entry.txt must not be only whitespace"
    assert "Q1 Targets" in written and "Kevin's" in written, "entry.txt must keep the Q1 Targets punchline and Kevin"


if __name__ == "__main__":
    main()
