# Review Journal

This journal records the domain cases that matter before widening the public API.

The local checks classify each case as `ship`, `watch`, or `hold`. That gives the project a small review vocabulary that matches its backend services focus without claiming live deployment or external usage.

## Cases

- `baseline`: `queue pressure`, score 150, lane `ship`
- `stress`: `retry load`, score 131, lane `watch`
- `edge`: `worker slack`, score 194, lane `ship`
- `recovery`: `session drift`, score 196, lane `ship`
- `stale`: `queue pressure`, score 195, lane `ship`

## Note

This file is intentionally plain so the fixture remains the source of truth.
