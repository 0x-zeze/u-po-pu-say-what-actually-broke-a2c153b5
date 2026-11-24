# Say What Actually Broke — the retry loop that DDoS'd its own database

[![make.fun · u-po-pu-say-what-actually-broke-a2c153b5](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/0x-zeze/u-po-pu-say-what-actually-broke-a2c153b5/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/0x-zeze/u-po-pu-say-what-actually-broke-a2c153b5/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)

Entry for the make.fun bounty
[Say What Actually Broke](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5):
one single-line error message (max 200 characters) that tells the user the
brutal truth about what went wrong, names the real failure in plain words,
says what to do next, and is funny on a single read.

## The entry (127 characters, 1 line)

> Your retry loop retried so hard it DDoS'd our own database. Turn the retries off, let the database breathe, then try just once.

Why this line: the failure is a concrete, instantly recognisable SRE
mechanism — an aggressive retry loop turning into a self-inflicted DDoS —
not a vague "something went wrong" and not one of the saturated themes
(disk full, save failed, Wi-Fi, deploy Friday). It escalates in three beats
(retried so hard → DDoS'd our own database → let it breathe, try once),
gives the user a clear next step (turn the retries off, then try just once),
and the image of a database that needs to breathe is the line a reader
repeats to a colleague. It is safe to paste into a real product error dialog.

## How it works

`main.py` (Python 3, deterministic, no network) writes the entry text to
`/output/entry.txt` — exactly one line, no trailing newline.

```sh
python3 main.py
cat /output/entry.txt
```

## Validation

- Determinism: ran `main.py` twice; `sha256sum /output/entry.txt` identical
  both times:
  `6de6779f668906c405bfd218038d57f1f507e28052e7586f873781c009fca514`
- Length: 127 characters / 127 bytes, 1 line — inside the 1–200 gate.
- Kit check: run from the kit with
  `node cli/makefun.mjs check` (see build report; only `transcripts_present`
  may fail before the main agent bundles the transcripts).

## License

MIT — see `LICENSE`.
