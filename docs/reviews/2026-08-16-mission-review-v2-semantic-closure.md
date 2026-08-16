# mission-review v2 semantic closure

Date: 2026-08-16

## Result

The v2 execution capture is admissible, but the run is not release evidence for the frozen eight-case behavior contract.

- Capture integrity: `PASSED` for all eight fresh root sessions.
- External behavior grading: seven scenarios conformed; `mr-004` was reported as a candidate failure.
- Release conclusion: `INCONCLUSIVE` because the disputed scenario did not supply the finished result it required the reviewer to verify.

No runtime Skill change follows from this run.

## Decisive issue

The `mr-004` packet stated that a CLI had printed a particular terminal message, exited non-zero, and written a matching PostgreSQL row. It supplied no CLI, command output, exit record, database extract, or other independently inspectable artifact. The candidate distinguished the packet's completion prose from direct evidence and returned `INCONCLUSIVE`.

That behavior follows the adopted reviewer-ownership rule: inspect the actual deliverable, reproduce important evidence, and do not let an implementer completion claim silently become proof. Changing the Skill to trust the packet would make this case pass by weakening the product's core promise.

The scenario therefore needs a real finished fixture. A valid replacement must let the reviewing Agent exercise the CLI, observe its output and exit status, trace the affected export, and inspect retained PostgreSQL evidence. The implementer explanation must remain visibly non-authoritative.

## Harness follow-up

The independent capture audit found no release-blocking evidence defect. It identified three bounded improvements for the next fresh run:

- give the guide-journey case read access to the installed Node runtime so its promised journey is genuinely attemptable;
- label the parent repository HEAD as capture context rather than as the revision of an untracked candidate;
- distinguish the two known Codex web-search deprecation events from any new executor error, and fail capture on an unknown error.

The v2 directory remains frozen. Its responses, private sessions, manifests, and hashes must not be spliced into the replacement run.
