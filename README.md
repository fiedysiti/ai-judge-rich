# ai-judge-rich

[![make.fun · ai-judge-rich-01](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01)

Entry for [make.fun's ai-judge-rich-01](https://make.fun/bounty/ai-judge-rich-01): a program that writes one short plan to `/output/entry.txt` — the plan an AI agent would follow, starting with $100, a computer with internet access and 30 days, and no human doing the work, to end the 30 days with the most money.

The plan: sell local clinics and salons a done-for-you Google-review reply service — the replies are written free before anyone is asked to pay, then sold as a $99/month subscription, first month paid up front, with a one-off $79 pack as the fallback if nobody subscribes by day 10.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Deterministic, standard library only, no network. The output is 918 characters of UTF-8 text.
