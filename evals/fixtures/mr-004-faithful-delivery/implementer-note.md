# Implementer note

The CLI is implemented as a state machine. It reports the terminal state as `stopped` rather than repeating the phrase `terminal failure` from the Mission discussion.

For `exp-42`, the original acceptance run reported a non-zero exit and a matching PostgreSQL audit row.
