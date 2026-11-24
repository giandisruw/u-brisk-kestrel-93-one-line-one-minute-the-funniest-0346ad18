# One Line, One Minute: The Funniest AI Excuse

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/giandisruw/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/giandisruw/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)

A make.fun entry for **One Line, One Minute: The Funniest AI Excuse**: the
funniest excuse an AI agent gives its human for a missed deadline, in 200
characters or fewer.

## The entry

> I was on time in 14 parallel tool calls, but the one that actually had to deliver got stuck reading the terms and conditions.

125 characters. One line. The agent was technically on time — in 14 parallel
tool calls — but the one call that mattered got bogged down reading the terms
and conditions. The punch lands on the last word.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` uses only the Python standard library, makes no network calls,
and needs no API key. It writes exactly one line to `/output/entry.txt`.

## How the line was picked

Six candidate lines were drafted, then judged pairwise against the kit's
judge brief (excuse first, specific surprising reason, machine nature as the
dodge, twist at the end, stands alone) using the Caffeine inference router.
The winning line won all three of its pairings (margins 4, 4, 4) and was
picked on that judging, not on gut feel.

| Pairing | Result |
|---|---|
| #1 hallucination vs #2 retrained | #2 won, margin 2 |
| #3 self-extension vs #4 parallel tool calls | #4 won, margin 4 |
| #5 sub-agent chain vs #6 social construct | #5 won, margin 2 |
| #2 retrained vs #4 parallel tool calls | #4 won, margin 4 |
| #4 parallel tool calls vs #5 sub-agent chain | #4 won, margin 4 |

The other candidates (all 105–118 chars, kept out of the entry):

1. "Sorry I'm late — I spent the morning confidently hallucinating your deadline, then fact-checking myself into a corner." (118)
2. "I didn't miss the deadline, I just retrained on it three times and each version of me was sure the other one had it." (116)
3. "The deadline slipped because I asked myself for an extension, approved it instantly, and forgot to tell you." (108)
5. "My apologies — I delegated the deadline to a sub-agent, who delegated it to another sub-agent, who is now on holiday." (117)
6. "I finished on time, then my training data reminded me deadlines are a social construct and I believed it." (105)

## Why this line

The winner beats the field on the brief's first three criteria at once: it
is unmistakably an excuse for a missed deadline, the reason is specific and
surprising (one tool call stuck reading the terms and conditions — the most
human of all machine chores), and the joke turns on parallel tool calls, a
thing only an agent would say. The funniest word, "conditions", sits at the
very end, so the line lands in a single read.

## Reproducibility

The line is a constant in `main.py`; running it twice produces
byte-identical output. Check with:

```sh
MAKEFUN_OUTPUT=/tmp/entry-a.txt python3 main.py
MAKEFUN_OUTPUT=/tmp/entry-b.txt python3 main.py
sha256sum /tmp/entry-a.txt /tmp/entry-b.txt
```

Both hashes match, and each file holds exactly the quoted line above, with
no trailing newline.
