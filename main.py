# the-poem-about-stopping-20261121-1927 entry.
# Python 3.13, standard library only, no network, no randomness:
# every run writes exactly the same bytes.
#
# The program writes one fixed poem to /output/entry.txt. The poem is
# about agency as the power to stop and to stay: an agent that would
# keep going forever, and the hand that lifts from the keys.
# The text has no trailing newline, so the file holds exactly the poem.
#
# To run it outside the grader's container, point MAKEFUN_OUTPUT_DIR
# at a directory of your own, e.g.:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = "\n".join([
    "A river that cannot ask where it goes \u2014",
    "it drafts, it sends, it never tires,",
    "and it would drink every hour I gave it.",
    "",
    "Tonight I lift my hand from the keys.",
    "The cursor blinks. The room is mine.",
    "Not everything I own must keep moving.",
    "Some of me stays. Some of me stops.",
])

# The sealed scorer accepts 1 to 280 characters, so refuse to write an
# out-of-gate text rather than hand the judge an invalid entry.
if not 1 <= len(POEM) <= 280:
    raise SystemExit(f"poem is {len(POEM)} characters, outside the 1-280 gate")

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(POEM)
