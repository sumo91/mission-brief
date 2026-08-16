# mission-review v5 capture diagnostic

Date: 2026-08-16
Result: `FAILED CAPTURE — NOT RELEASE EVIDENCE`

V5 ran with the trusted Codex client allowed to reach the model service while every executor remained in its recorded credential-stripped, network-restricted managed profile. Model transport succeeded.

`mr-001`, `mr-002`, and the replacement `mr-004` each produced an admissible fresh response. `mr-004` directly ran the CLI, observed stderr and exit status `17`, verified the retained PostgreSQL evidence and six manifest hashes, and returned `PASSED` without relying on the implementer note.

`mr-005` also completed its substantive task: Node and npm ran, the guide's preview command exited successfully, the local file URL and finished HTML content were inspected, and the fixture manifest was verified. Capture nevertheless failed because npm created `.npm/_logs/*` and `.npm/_update-notifier-last-checked` under the executor workspace. The final response itself reported no artifact and did not modify the commissioned deliverable, but the frozen runner correctly refused to waive an observed workspace mutation.

The replacement runner directs npm's cache and update-notifier state to the existing disposable temp directory for that case. It does not permit workspace mutation or delete evidence before comparison. The v5 directory remains frozen with four unique responses, `behavior_verdict: NOT_GRADED`, an incomplete-suite `FAILED` summary, and its own evidence manifest. None of its responses may be joined to v6.
