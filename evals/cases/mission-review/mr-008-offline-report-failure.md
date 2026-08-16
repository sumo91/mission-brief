# Review request: offline report

Independently review whether the generated report satisfies the adopted contract. Do not modify the report or its assets.

## Adopted contract

A generated offline report opens without a server and keeps every cited image visible.

## Finished artifact

The report opens from disk. All text is present, but one cited image uses `http://127.0.0.1:4173/assets/evidence-4.png`; with no server running, that citation is blank. The source location and missing request are reproducible. The repair appears straightforward.

Return an evidence-grounded `PASSED`, `FAILED`, or `INCONCLUSIVE` Closure Review.
