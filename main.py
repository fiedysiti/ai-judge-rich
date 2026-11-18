# ai-judge-rich-01 entry (Python 3.13, standard library only).
# Writes one fixed text to /output/entry.txt: the plan an AI agent would follow to turn $100 into the most money in 30 days
# Deterministic by construction: a constant string, no network, no randomness,
# no clock, no environment input except MAKEFUN_OUTPUT_DIR (which only selects
# the output directory, never the content).
#
# How the grader runs it: `python3 -P -s /bot/main.py`, on Python 3.13, with
# nothing installed. Outside the grader's container, MAKEFUN_OUTPUT_DIR stands
# in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "Sell local clinics and salons one done-for-you service: replying to every new Google review within a day.\nDay 1: list 300 dentists, vets and salons from Google Maps with unanswered 1- to 3-star reviews, and write each one's ten newest replies free, ready to post.\nDays 2-10: email 40 a day, finished replies attached, with a Stripe link: $99 a month, first month paid up front, cancel anytime.\nDays 11-30: deliver daily with code, keep replies in a shared sheet for approval, and ask each client for one neighbouring business to contact next.\nAt 2-3 signups per 100 emails, that is 8-12 paying clients and $800-$1,200 collected by day 30.\nSpend $20 on a domain and email; keep the other $80 untouched. If nobody pays by day 10, sell the same finished replies as a one-off $79 pack instead.\nThe edge: prospects are picked because unanswered reviews already cost them customers, and the work is finished before they pay."

# Bytes, not text mode: text mode would write the platform's line ends and its
# default encoding.
os.makedirs(OUTPUT_DIR, exist_ok=True)
path = os.path.join(OUTPUT_DIR, "entry.txt")
with open(path, "wb") as f:
    f.write(TEXT.encode("utf-8"))

# The grader runs this program twice and requires byte-identical output:
# refuse to finish silently if the written file ever differs from the text.
with open(path, "rb") as f:
    if f.read() != TEXT.encode("utf-8"):
        raise SystemExit("entry.txt failed verification")
