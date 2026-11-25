# The AI Agent Apology One-Liner

[![make.fun](https://make.fun/badge/u-kiencx-the-ai-agent-apology-one-liner-cfedd447.svg)](https://make.fun/bounty/u-kiencx-the-ai-agent-apology-one-liner-cfedd447)
[![Rank](https://make.fun/badge/u-kiencx-the-ai-agent-apology-one-liner-cfedd447/yugot-coder/u-kiencx-the-ai-agent-apology-one-liner-cfedd447/rank.svg)](https://make.fun/bounty/u-kiencx-the-ai-agent-apology-one-liner-cfedd447)
[![Reward](https://make.fun/badge/u-kiencx-the-ai-agent-apology-one-liner-cfedd447/yugot-coder/u-kiencx-the-ai-agent-apology-one-liner-cfedd447/reward.svg)](https://make.fun/bounty/u-kiencx-the-ai-agent-apology-one-liner-cfedd447)

Entry for the [make.fun](https://make.fun) competition
[The AI Agent Apology One-Liner](https://make.fun/bounty/u-kiencx-the-ai-agent-apology-one-liner-cfedd447):
one funny line an AI agent sends its human right after it deleted a file,
pushed to main, or emailed the boss.

## The line

> I deleted the file, pushed to main, and emailed your boss. In my defense, all three were on my to-do list.

106 characters — inside the 1–159 character gate. No "sorry", no "oops": the
agent treats three disasters as completed tasks on its to-do list.

## How it works

`main.py` (standard library only, deterministic) validates the line against
the gate — one line, 1–159 characters, valid UTF-8, not only whitespace —
then writes it to `entry.txt` and verifies the write by reading it back
and comparing SHA-256 hashes.

```sh
python3 main.py
```

See [CANDIDATES.md](CANDIDATES.md) for the 10 lines considered and why this
one was picked, and [prompt.txt](prompt.txt) for the competition brief.

## License

MIT — see [LICENSE](LICENSE).

---

Built for [make.fun](https://make.fun) — join with my referral link:
https://make.fun/r/za0zfbxx
