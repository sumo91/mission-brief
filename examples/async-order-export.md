# Mission Brief: Accepted orders appear exactly once in an asynchronous JSON export

## Intent

Operators need a reliable export of accepted orders without waiting on a synchronous download, while the existing audit trail stays trustworthy.

## Desired Outcome

Every accepted order appears exactly once in a JSON export within five minutes of acceptance. Terminal failures are visible to operators at the system boundary.

## Success

- Every accepted order appears in the export exactly once.
- The export is available within five minutes of acceptance.
- Terminal failures are visible to operators without inspecting internal logs.
- Existing human-readable export behavior remains compatible.

## Evidence Required

- Representative accepted-order paths that support exactly-once appearance within the latency bound.
- Retry, duplicate, and failure-path evidence that would falsify exactly-once delivery or operator visibility.
- A compatibility check against the existing human-readable export.
- Missing required evidence, a violated boundary, or unexplained counterevidence blocks `PASSED` and may yield `FAILED` or `INCONCLUSIVE`.

## Boundaries

- PostgreSQL remains the audit store, as required by the existing audit contract.
- Repository payment, export, and audit contracts remain authoritative for current system facts unless an authorized decision supersedes them.
- Serialization format details, storage internals, and processing topology remain delegated.

## Non-goals

- Refunds, invoices, and subscriptions are out of scope for this commission.

## Context

- Locate the existing export and audit contracts in the target repository; do not copy them into this Brief.

## Execution Authority

- Investigation, planning, implementation, correction, and validation inside the authorized local repository are granted.
- External storage, production writes, destructive data changes, and scope expansion require confirmation.
