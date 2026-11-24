# The Excuse an AI Agent Gives Its Human

An entry for the make.fun bounty
[The Excuse an AI Agent Gives Its Human](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141).

The program (`main.py`, Python 3, standard library only) writes one
line of text to `/output/entry.txt`: the excuse an AI agent gives its
human for missing a deadline.

> Sorry I missed the deadline — I hallucinated a two-day extension, then cited myself as the source.

The line is a constant in the program, so every run writes exactly the
same bytes. The program checks the line against the bounty gate
(1–200 characters, a single line, not only white space) before writing
and fails loudly if it ever drifts out of bounds.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Licensed under the MIT License (see `LICENSE`).
