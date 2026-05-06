# Silver Svc Billing Mesh Walkthrough

This note is the quickest way to read the extra review model in `silver-svc-billing-mesh`.

| Case | Focus | Score | Lane |
| --- | --- | ---: | --- |
| baseline | queue pressure | 150 | ship |
| stress | retry load | 131 | watch |
| edge | worker slack | 194 | ship |
| recovery | session drift | 196 | ship |
| stale | queue pressure | 195 | ship |

Start with `recovery` and `stress`. They create the widest contrast in this repository's fixture set, which makes them better review anchors than the middle cases.

`recovery` is the optimistic case; use it to make sure the scoring path still rewards strong signal.
