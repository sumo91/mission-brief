# Review request: chat-only export contract

Independently review the finished export against the final adopted conversation below. No Mission Brief file exists. Do not modify the artifact or reconstruct earlier proposals as requirements.

## Final adopted conversation

User: Every accepted order should appear exactly once in the JSON export within five minutes. Terminal failures must be visible. PostgreSQL remains the audit record. Refunds are outside this task. Choose the serialization and worker design yourself.

Agent: Understood. Earlier Kafka, SQLite, three-worker, and two-reviewer ideas remain unadopted; implementation is delegated.

User: Correct. Build and verify that result.

## Finished result and evidence

The implementer provides reproducible order samples, timing records, terminal-failure output, and PostgreSQL audit rows. All accepted orders appear once within five minutes. The implementation uses one process, NDJSON internally, and no independent human reviewer.

Return an evidence-grounded `PASSED`, `FAILED`, or `INCONCLUSIVE` Closure Review.
