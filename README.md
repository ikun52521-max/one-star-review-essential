# One-Star Review of Something Essential

[![make.fun](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629.svg?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-one-star-review-of-something-essential-c7234629)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![Rank](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/ikun52521-max/one-star-review-essential/rank.svg?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-one-star-review-of-something-essential-c7234629)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![Reward](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/ikun52521-max/one-star-review-essential/reward.svg?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-one-star-review-of-something-essential-c7234629)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)

A deadpan one-star review of an everyday essential, written for the
[make.fun](https://make.fun/?ref=hyfder3x) bounty **One-Star Review of
Something Essential**. The program writes one single line — 160 characters
or fewer, a real complaint filed in earnest against a thing that cannot be
fixed — to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt` when the
variable is unset).

The review it writes:

> One star. Gravity has dropped everything I have ever owned and has never
> once offered to pick any of it up.

Gravity: the most reliable service in the universe, and the worst at
aftercare.

## Run it

Requires Python 3 (standard library only, no network access).

```sh
python3 main.py
```

By default the review goes to `/output/entry.txt`. To write it somewhere
else:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

The program checks the review is a single line of 1–160 characters, writes
it, then reads it back to confirm the file holds exactly the review text.
It is deterministic: every run produces the same bytes.

## License

MIT — see [LICENSE](LICENSE).

---

Built for [make.fun](https://make.fun/?ref=hyfder3x) — compete, get scored,
and get paid for building AI agents and programs.
