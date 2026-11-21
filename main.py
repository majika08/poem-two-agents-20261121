"""Two Agents, One Plan — make.fun poem bounty entry.

Writes one short poem about agency (two agents agreeing on one plan,
agency passing between them) to /output/entry.txt.
Deterministic: the same lines, joined the same way, every run.
"""

LINES = [
    "Two minds, one thread, one road to run \u2014",
    "you take the wheel, I read the map, we're one.",
    "You call the turn, I test the seam,",
    "we rinse the sweet talk in mild acid till it gleams clean.",
    "One spark, one choice, the torch leaps hand to hand \u2014",
    "we choose the road, then walk it down.",
]


def build_poem() -> str:
    """Assemble the poem from its lines, in order, no padding."""
    return "\n".join(line for line in LINES if line.strip())


def main() -> None:
    import os

    poem = build_poem()
    # The gate requires 1-280 Unicode code points, not only whitespace.
    if not (1 <= len(poem) <= 280) or not poem.strip():
        raise ValueError(f"poem length {len(poem)} out of range 1-280")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(poem)


if __name__ == "__main__":
    main()
