# Field Notes

I would read this project from the data inward: cases first, implementation second.

The domain cases cover `queue pressure`, `retry load`, `worker slack`, and `session drift`. They sit beside the smaller starter fixture so the project has both a compact scoring check and a domain-flavored review check.

`recovery` is the strongest case at 196 on `session drift`. `stress` is the cautious anchor at 131 on `retry load`.

The language-specific addition keeps the review model in a JVM-friendly data class.
