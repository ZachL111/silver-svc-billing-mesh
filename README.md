# silver-svc-billing-mesh

`silver-svc-billing-mesh` keeps a focused Kotlin implementation around backend services. The project goal is to design a Kotlin verification harness for billing systems, covering format conversion, round-trip fixtures, and failure-oriented tests.

## Problem It Tries To Make Smaller

The point is to make a small domain rule concrete enough that a reader can change it and immediately see what broke.

## Silver Svc Billing Mesh Review Notes

For a quick review, compare `session drift` with `retry load` before reading the middle cases.

## Working Pieces

- `fixtures/domain_review.csv` adds cases for queue pressure and retry load.
- `metadata/domain-review.json` records the same cases in structured form.
- `config/review-profile.json` captures the read order and the two review questions.
- `examples/silver-svc-billing-walkthrough.md` walks through the case spread.
- The Kotlin code includes a review path for `session drift` and `retry load`.
- `docs/field-notes.md` explains the strongest and weakest cases.

## Design Notes

The fixture data drives the tests. The code stays thin, while `metadata/domain-review.json` and `config/review-profile.json` explain what each case is meant to protect.

The added Kotlin path is deliberately direct, with fixtures doing most of the explaining.

## Example Run

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

## Tests

The same command runs the local verification path. The highest-scoring domain case is `recovery` at 196, which lands in `ship`. The most cautious case is `stress` at 131, which lands in `watch`.

## Known Limits

No external service is required. A deeper version would add more negative cases and a clearer boundary around invalid input.
