# The Comment Above the Code

A make.fun one-liner entry: a single comment a developer left above
fragile production code, funny and painfully honest at once.

## The line

```
// The sleep(500) below is load-bearing. Remove it and the webhook fails, as we discovered on a Friday, in production, twice.
```

## How to run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

`main.py` (Python 3.13, stdlib only) writes exactly the line above —
no trailing newline — to `<output dir>/entry.txt`, creating the
directory if needed. If `MAKEFUN_OUTPUT_DIR` is unset it writes to
`/output`.
