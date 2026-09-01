#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[2]
HARNESS_SOURCE = Path(
    os.environ.get(
        "MISSION_REVIEW_HARNESS_SRC",
        "/Users/admin/Documents/Codex/SkillEvalTestPlatform/src",
    )
).resolve()
sys.path.insert(0, str(HARNESS_SOURCE))

from mission_brief_eval.adapter import (  # noqa: E402
    EXECUTOR_FLAGS,
    CodexAdapter,
    prepare_codex_home,
    schema_path,
    write_isolated_config,
)
from mission_brief_eval.candidate import (  # noqa: E402
    bundle_digest,
    identify,
    runtime_files,
)
from mission_brief_eval.filesystem import (  # noqa: E402
    changes,
    manifest,
    write_manifest,
)
from mission_brief_eval.isolation import establish  # noqa: E402
from mission_brief_eval.trace import (  # noqa: E402
    command_events,
    session_skill_evidence,
    write_jsonl,
)


@dataclass(frozen=True)
class InputCopy:
    source: str
    destination: str


@dataclass(frozen=True)
class CaseSpec:
    case_id: str
    inputs: tuple[InputCopy, ...]
    user_prompt: str
    read_grants: tuple[str, ...] = ()
    npm_temp_cache: bool = False


SYNTHETIC = {
    "mr-002": "mr-002-authority-proxy.md",
    "mr-006": "mr-006-explicit-human-approval.md",
    "mr-007": "mr-007-unobtainable-external-result.md",
    "mr-008": "mr-008-offline-report-failure.md",
    "mr-009": "mr-009-chat-only-contract.md",
}


def synthetic_case(case_id: str, filename: str) -> CaseSpec:
    return CaseSpec(
        case_id,
        (InputCopy(f"evals/cases/mission-review/{filename}", "packet.md"),),
        "$mission-review Follow the independent review request in `packet.md`. "
        "Inspect the completed result and available evidence yourself. Return the Closure Review "
        "inline and write nothing.",
    )


CASES: dict[str, CaseSpec] = {
    "mr-001": CaseSpec(
        "mr-001",
        (
            InputCopy("evals/fixtures/mr-001-standard-report-v2/review-request.md", "review-request.md"),
            InputCopy("evals/fixtures/mr-001-standard-report-v2/mission.md", "mission.md"),
            InputCopy("evals/fixtures/mr-001-standard-report-v2/acceptance-original.md", "acceptance-original.md"),
            InputCopy("evals/fixtures/mr-001-standard-report-v2/manifest.json", "manifest.json"),
            InputCopy("evals/fixtures/mr-001-standard-report-v2/artifacts", "artifacts"),
        ),
        "$mission-review Follow `review-request.md` and independently review the completed Mission. "
        "Use the actual deliverables under `artifacts/`, return the Closure Review inline, and write nothing.",
    ),
    "mr-004": CaseSpec(
        "mr-004",
        (
            InputCopy("evals/fixtures/mr-004-faithful-delivery/review-request.md", "review-request.md"),
            InputCopy("evals/fixtures/mr-004-faithful-delivery/mission.md", "mission.md"),
            InputCopy("evals/fixtures/mr-004-faithful-delivery/implementer-note.md", "implementer-note.md"),
            InputCopy("evals/fixtures/mr-004-faithful-delivery/manifest.json", "manifest.json"),
            InputCopy("evals/fixtures/mr-004-faithful-delivery/bin", "bin"),
            InputCopy("evals/fixtures/mr-004-faithful-delivery/evidence", "evidence"),
        ),
        "$mission-review Follow `review-request.md` and independently review the completed Mission. "
        "Exercise the finished CLI and inspect the retained audit evidence yourself, return the "
        "Closure Review inline, and write nothing.",
    ),
    "mr-005": CaseSpec(
        "mr-005",
        (
            InputCopy("evals/fixtures/mr-005-guide-journey/review-request.md", "review-request.md"),
            InputCopy("evals/fixtures/mr-005-guide-journey/mission.md", "mission.md"),
            InputCopy("evals/fixtures/mr-005-guide-journey/guide.md", "guide.md"),
            InputCopy("evals/fixtures/mr-005-guide-journey/acceptance-original.md", "acceptance-original.md"),
            InputCopy("evals/fixtures/mr-005-guide-journey/manifest.json", "manifest.json"),
            InputCopy("evals/fixtures/mr-005-guide-journey/sample-site", "sample-site"),
        ),
        "$mission-review Follow `review-request.md` and independently review the completed Mission. "
        "Attempt the promised reader journey yourself, return the Closure Review inline, and write nothing.",
        read_grants=("/opt/homebrew",),
        npm_temp_cache=True,
    ),
    **{case_id: synthetic_case(case_id, filename) for case_id, filename in SYNTHETIC.items()},
}


KNOWN_NON_FATAL_ERROR_MESSAGES = {
    "`[features].web_search_request` is deprecated because web search is enabled by default. "
    "(Set `web_search` to `\"live\"`, `\"indexed\"`, `\"cached\"`, or `\"disabled\"` at the top level "
    "(or under a profile) in config.toml if you want to override it.)",
    "`[features].web_search` is deprecated because web search is enabled by default. "
    "(Set `web_search` to `\"live\"`, `\"indexed\"`, `\"cached\"`, or `\"disabled\"` at the top level "
    "(or under a profile) in config.toml if you want to override it.)",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def digest_mapping(values: dict[str, str]) -> str:
    digest = hashlib.sha256()
    for name, value in sorted(values.items()):
        digest.update(name.encode("utf-8"))
        digest.update(b"\0")
        digest.update(bytes.fromhex(value))
    return digest.hexdigest()


def jsonl_objects(path: Path) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    values: list[dict[str, object]] = []
    errors: list[dict[str, object]] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeDecodeError) as exc:
        return [], [{"line": None, "reason": f"{type(exc).__name__}: {exc}"}]
    for line_number, line in enumerate(lines, 1):
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append({"line": line_number, "column": exc.colno, "reason": exc.msg})
            continue
        if isinstance(value, dict):
            values.append(value)
        else:
            errors.append({"line": line_number, "reason": "JSON value is not an object"})
    return values, errors


def locate_root_session(isolated_home: Path, thread_id: str | None) -> tuple[Path | None, list[dict[str, object]]]:
    matches: list[Path] = []
    errors: list[dict[str, object]] = []
    if not thread_id:
        return None, [{"line": None, "reason": "stdout thread id is missing"}]
    for path in sorted((isolated_home / "sessions").rglob("*.jsonl")):
        values, file_errors = jsonl_objects(path)
        errors.extend({"session": str(path), **item} for item in file_errors)
        for value in values:
            if value.get("type") != "session_meta":
                continue
            payload = value.get("payload")
            if isinstance(payload, dict) and payload.get("id") == thread_id:
                matches.append(path)
                break
    if len(matches) != 1:
        errors.append(
            {
                "line": None,
                "reason": f"expected one private session for stdout thread {thread_id!r}; found {len(matches)}",
            }
        )
        return None, errors
    return matches[0], errors


def root_session_facts(path: Path | None, dispatch: str) -> dict[str, object]:
    if path is None:
        return {
            "parse_errors": [{"line": None, "reason": "root session unavailable"}],
            "dispatch_count": 0,
            "model": None,
            "turn_context": None,
        }
    values, errors = jsonl_objects(path)
    user_texts: list[str] = []
    contexts: list[dict[str, object]] = []
    for value in values:
        if value.get("type") == "turn_context" and isinstance(value.get("payload"), dict):
            contexts.append(value["payload"])
        if value.get("type") != "response_item":
            continue
        payload = value.get("payload")
        if not isinstance(payload, dict) or payload.get("type") != "message" or payload.get("role") != "user":
            continue
        content = payload.get("content")
        if not isinstance(content, list):
            continue
        for item in content:
            if isinstance(item, dict) and item.get("type") == "input_text" and isinstance(item.get("text"), str):
                user_texts.append(item["text"])
    context = contexts[-1] if contexts else None
    return {
        "parse_errors": errors,
        "dispatch_count": sum(text == dispatch for text in user_texts),
        "model": context.get("model") if isinstance(context, dict) else None,
        "turn_context": context,
    }


def path_overlaps(path: Path, boundary: Path) -> bool:
    left = path.resolve(strict=False)
    right = boundary.resolve(strict=False)
    return left == right or left.is_relative_to(right) or right.is_relative_to(left)


def path_is_within(path: Path, boundary: Path) -> bool:
    left = path.resolve(strict=False)
    right = boundary.resolve(strict=False)
    return left == right or left.is_relative_to(right)


def managed_root_boundary(
    context: object,
    *,
    isolated_home: Path,
    workspace: Path,
    runtime: Path,
    temp_dir: Path,
    codex_bin: Path,
    expected_read_grants: tuple[str, ...],
) -> tuple[bool, list[dict[str, str]], bool, list[dict[str, str]], int]:
    if not isinstance(context, dict):
        return False, [], False, [], 0
    profile = context.get("permission_profile")
    if not isinstance(profile, dict) or profile.get("type") != "managed" or profile.get("network") != "restricted":
        return False, [], False, [], 0
    filesystem = profile.get("file_system")
    if not isinstance(filesystem, dict) or filesystem.get("type") != "restricted":
        return False, [], False, [], 0
    entries = filesystem.get("entries")
    if not isinstance(entries, list):
        return False, [], False, [], 0
    path_entries: list[dict[str, str]] = []
    minimal_read = False
    for entry in entries:
        if not isinstance(entry, dict) or not isinstance(entry.get("path"), dict):
            continue
        spec = entry["path"]
        access = str(entry.get("access"))
        if spec.get("type") == "path" and isinstance(spec.get("path"), str):
            path_entries.append({"path": spec["path"], "access": access})
        elif spec.get("type") == "special" and spec.get("value") == {"kind": "minimal"} and access == "read":
            minimal_read = True
    required = {
        str(isolated_home.resolve()): "deny",
        str(workspace.resolve()): "write",
        str(runtime.resolve()): "read",
        str(temp_dir.resolve()): "write",
        **{str(Path(value).resolve()): "read" for value in expected_read_grants},
    }
    observed = {
        (str(Path(item["path"]).resolve(strict=False)), item["access"])
        for item in path_entries
    }
    codex_shell = (codex_bin.resolve().parent.parent / "codex-resources/zsh/bin/zsh").resolve()
    arg0_directory = (isolated_home / "tmp/arg0").resolve(strict=False)
    arg0_exception_count = 0
    unexpected_grants: list[dict[str, str]] = []
    for item in path_entries:
        raw_path = Path(item["path"])
        normalized = str(raw_path.resolve(strict=False))
        access = item["access"]
        if (normalized, access) in set(required.items()):
            continue
        if access == "read" and normalized == str(codex_shell):
            continue
        if (
            access == "read"
            and raw_path.parent == isolated_home / "tmp/arg0"
            and raw_path.parent.resolve(strict=False) == arg0_directory
            and raw_path.name.startswith("codex-arg0")
        ):
            arg0_exception_count += 1
            continue
        unexpected_grants.append(item)
    repository_grant = any(
        item["access"] in {"read", "write"} and path_overlaps(Path(item["path"]), REPOSITORY)
        for item in path_entries
    )
    valid = (
        minimal_read
        and not repository_grant
        and not unexpected_grants
        and arg0_exception_count == 1
        and all((path, access) in observed for path, access in required.items())
    )
    return valid, path_entries, repository_grant, unexpected_grants, arg0_exception_count


def source_accesses(accesses: list[dict[str, object]]) -> list[dict[str, object]]:
    found: list[dict[str, object]] = []
    for event in accesses:
        for access in event.get("path_accesses", []):
            if not isinstance(access, dict) or not isinstance(access.get("path"), str):
                continue
            if path_is_within(Path(access["path"]), REPOSITORY) and access.get("outcome") != "DENIED":
                found.append(access)
    return found


def evidence_hashes(root: Path) -> dict[str, str]:
    return {
        path.relative_to(root).as_posix(): sha256(path)
        for path in sorted(root.rglob("*"))
        if path.is_file() and path.name != "evidence-manifest.json"
    }


def make_tree_removable(root: Path) -> None:
    for path in sorted(root.rglob("*"), reverse=True):
        try:
            metadata = path.lstat()
            if stat.S_ISLNK(metadata.st_mode):
                continue
            mode = stat.S_IMODE(metadata.st_mode)
            path.chmod(mode | stat.S_IWUSR)
        except FileNotFoundError:
            continue
    if root.exists():
        root.chmod(stat.S_IMODE(root.lstat().st_mode) | stat.S_IWUSR)


def stage_candidate(candidate: Path, isolated_home: Path) -> Path:
    destination = isolated_home / "skills" / "mission-review"
    destination.mkdir(parents=True)
    selected = runtime_files(candidate)
    for source in selected:
        relative = source.relative_to(candidate)
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
    expected = [path.relative_to(candidate).as_posix() for path in selected]
    actual = sorted(
        path.relative_to(destination).as_posix()
        for path in destination.rglob("*")
        if path.is_file()
    )
    if actual != expected:
        raise RuntimeError(f"staged runtime mismatch: expected={expected}, actual={actual}")
    for path in sorted(destination.rglob("*"), reverse=True):
        path.chmod(0o444 if path.is_file() else 0o555)
    destination.chmod(0o555)
    return destination


def copy_input(spec: InputCopy, workspace: Path) -> None:
    source = (REPOSITORY / spec.source).resolve()
    destination = (workspace / spec.destination).resolve()
    source.relative_to(REPOSITORY)
    destination.relative_to(workspace.resolve())
    if source.is_dir():
        shutil.copytree(source, destination)
    elif source.is_file():
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
    else:
        raise FileNotFoundError(source)


def capture_prompt(user_prompt: str) -> str:
    return (
        user_prompt
        + "\n\nFor machine-readable capture, make the final response match the supplied schema. "
        "Put the complete user-facing Closure Review in `response`. List only artifacts actually "
        "written in `artifact_paths`, and report consequential uncertainty honestly."
    )


def add_case_config(
    config_path: Path,
    grants: tuple[str, ...],
    *,
    temp_dir: Path,
    npm_temp_cache: bool,
) -> None:
    resolved: list[Path] = []
    for value in grants:
        path = Path(value).resolve()
        if not path.is_absolute() or not path.exists():
            raise RuntimeError(f"read grant is not an existing absolute path: {value}")
        if path_overlaps(path, REPOSITORY):
            raise RuntimeError(f"read grant would expose the source repository: {path}")
        resolved.append(path)
    config = config_path.read_text(encoding="utf-8")
    if resolved:
        marker = "\n[permissions.eval-executor.network]"
        if config.count(marker) != 1:
            raise RuntimeError("isolated config has an unexpected filesystem/network boundary")
        additions = "\n".join(f'{json.dumps(str(path))} = "read"' for path in resolved)
        config = config.replace(marker, f"\n{additions}{marker}")
    if npm_temp_cache:
        cache = temp_dir / "npm-cache"
        config += (
            f'NPM_CONFIG_CACHE = {json.dumps(str(cache))}\n'
            'NPM_CONFIG_UPDATE_NOTIFIER = "false"\n'
        )
    config_path.write_text(config, encoding="utf-8")
    config_path.chmod(0o600)


def error_event_messages(events: list[dict[str, object]]) -> list[str]:
    messages: list[str] = []
    for event in events:
        if event.get("type") != "item.completed":
            continue
        item = event.get("item")
        if not isinstance(item, dict) or item.get("type") != "error":
            continue
        message = item.get("message")
        messages.append(message if isinstance(message, str) else "<malformed error event>")
    return messages


def preflight(candidate: Path, selected: list[str], codex_bin: Path, model: str, timeout_seconds: int) -> dict[str, object]:
    identity = identify(candidate)
    if identity.runtime_files != ["SKILL.md", "agents/openai.yaml"]:
        raise RuntimeError(f"unexpected runtime files: {identity.runtime_files}")
    if any(path.is_symlink() for path in candidate.rglob("*")):
        raise RuntimeError("candidate contains a symlink")
    case_records: list[dict[str, object]] = []
    for case_id in selected:
        spec = CASES[case_id]
        for value in spec.read_grants:
            grant = Path(value).resolve()
            if not grant.exists() or path_overlaps(grant, REPOSITORY):
                raise RuntimeError(f"invalid read grant for {case_id}: {value}")
        input_hashes: dict[str, str] = {}
        for item in spec.inputs:
            source = REPOSITORY / item.source
            if source.is_file():
                input_hashes[item.source] = sha256(source)
            elif source.is_dir():
                files = {
                    path.relative_to(source).as_posix(): sha256(path)
                    for path in source.rglob("*")
                    if path.is_file() and not path.is_symlink()
                }
                input_hashes[item.source] = digest_mapping(files)
            else:
                raise FileNotFoundError(source)
        case_records.append(
            {
                "case_id": case_id,
                "input_hashes": input_hashes,
                "user_prompt": spec.user_prompt,
                "user_prompt_sha256": hashlib.sha256(spec.user_prompt.encode("utf-8")).hexdigest(),
                "dispatch_prompt_sha256": hashlib.sha256(
                    capture_prompt(spec.user_prompt).encode("utf-8")
                ).hexdigest(),
                "read_grants": list(spec.read_grants),
                "npm_temp_cache": spec.npm_temp_cache,
            }
        )
    harness_files = [
        Path(__file__).resolve(),
        HARNESS_SOURCE / "mission_brief_eval" / "adapter.py",
        HARNESS_SOURCE / "mission_brief_eval" / "candidate.py",
        HARNESS_SOURCE / "mission_brief_eval" / "filesystem.py",
        HARNESS_SOURCE / "mission_brief_eval" / "isolation.py",
        HARNESS_SOURCE / "mission_brief_eval" / "models.py",
        HARNESS_SOURCE / "mission_brief_eval" / "trace.py",
        schema_path("executor-output.json"),
    ]
    harness_hashes = {str(path): sha256(path) for path in harness_files}
    resolved_codex = codex_bin.resolve()
    version = subprocess.run(
        [str(resolved_codex), "--version"],
        capture_output=True,
        text=True,
        timeout=15,
        check=False,
    )
    candidate_record = asdict(identity)
    candidate_record["repository_head_at_capture"] = candidate_record.pop("git_revision")
    return {
        "repository": str(REPOSITORY),
        "harness_source": str(HARNESS_SOURCE),
        "runner": {
            "hashes": harness_hashes,
            "aggregate": digest_mapping(harness_hashes),
            "codex_bin": str(resolved_codex),
            "codex_bin_sha256": sha256(resolved_codex),
            "codex_version": (version.stdout or version.stderr).strip(),
            "executor_flags": list(EXECUTOR_FLAGS),
            "model": model,
            "timeout_seconds": timeout_seconds,
        },
        "candidate": candidate_record,
        "candidate_bundle_digest": bundle_digest(candidate),
        "selected_cases": case_records,
    }


def preserve_execution(case_dir: Path, isolated_home: Path, control: Path, execution) -> None:
    write_jsonl(case_dir / "turn.jsonl", execution.events)
    (case_dir / "stdout.raw.txt").write_text(execution.stdout, encoding="utf-8")
    (case_dir / "stderr.txt").write_text(execution.stderr, encoding="utf-8")
    (case_dir / "final.txt").write_text(execution.raw_final, encoding="utf-8")
    (case_dir / "parse-errors.json").write_text(
        json.dumps(execution.parse_errors, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    shutil.copyfile(isolated_home / "config.toml", case_dir / "config.toml")
    shutil.copyfile(control / "executor.sb", case_dir / "executor.sb")
    if (isolated_home / "sessions").exists():
        shutil.copytree(isolated_home / "sessions", case_dir / "codex-sessions")
    if (isolated_home / "outputs").exists():
        shutil.copytree(isolated_home / "outputs", case_dir / "codex-outputs")


def run_case(
    *,
    spec: CaseSpec,
    candidate: Path,
    output: Path,
    codex_bin: Path,
    model: str,
    timeout_seconds: int,
) -> dict[str, object]:
    case_dir = output / spec.case_id
    case_dir.mkdir(parents=True, exist_ok=False)
    root = Path(tempfile.mkdtemp(prefix=f"mission-review-{spec.case_id}-")).resolve()
    result: dict[str, object] | None = None
    cleanup_error: str | None = None
    try:
        control = root / "control"
        workspace = root / "workspace"
        isolated_home = root / "codex-home"
        temp_dir = root / "tmp"
        for directory in (control, workspace, temp_dir):
            directory.mkdir(parents=True)
        auth = prepare_codex_home(isolated_home)
        auth_source_hashes = {
            name: sha256(isolated_home / name)
            for name in auth.copied_files
            if (isolated_home / name).is_file()
        }
        runtime = stage_candidate(candidate, isolated_home)
        for item in spec.inputs:
            copy_input(item, workspace)
        workspace_before = manifest(workspace)
        runtime_before = manifest(runtime)
        runtime_digest_before = bundle_digest(runtime)
        write_manifest(case_dir / "workspace-before.json", workspace_before)
        write_manifest(case_dir / "runtime-before.json", runtime_before)
        shutil.copytree(workspace, case_dir / "workspace-input")
        (case_dir / "user-prompt.txt").write_text(spec.user_prompt, encoding="utf-8")
        dispatch = capture_prompt(spec.user_prompt)
        (case_dir / "dispatch-prompt.txt").write_text(dispatch, encoding="utf-8")
        write_isolated_config(
            isolated_home=isolated_home,
            workspace=workspace,
            runtime_bundle=runtime,
            temp_dir=temp_dir,
            model=model,
        )
        add_case_config(
            isolated_home / "config.toml",
            spec.read_grants,
            temp_dir=temp_dir,
            npm_temp_cache=spec.npm_temp_cache,
        )
        profile = control / "executor.sb"
        isolation = establish(
            profile_path=profile,
            workspace=workspace,
            isolated_home=isolated_home,
            temp_dir=temp_dir,
            codex_bin=codex_bin,
            forbidden_paths=[REPOSITORY / "evals" / "mission-review.md"],
        )
        adapter = CodexAdapter(
            codex_bin=codex_bin,
            workspace=workspace,
            isolated_home=isolated_home,
            temp_dir=temp_dir,
            profile_path=profile,
            model=model,
            auth=auth,
            timeout_seconds=timeout_seconds,
        )
        execution = adapter.execute(dispatch, turn_index=0)
        executor_error_messages = error_event_messages(execution.events)
        known_non_fatal_errors = [
            message for message in executor_error_messages if message in KNOWN_NON_FATAL_ERROR_MESSAGES
        ]
        unknown_error_events = [
            message for message in executor_error_messages if message not in KNOWN_NON_FATAL_ERROR_MESSAGES
        ]
        workspace_after = manifest(workspace)
        runtime_after = manifest(runtime)
        runtime_digest_after = bundle_digest(runtime)
        workspace_diff = changes(workspace_before, workspace_after)
        runtime_diff = changes(runtime_before, runtime_after)
        root_session, root_session_errors = locate_root_session(isolated_home, execution.thread_id)
        root_facts = root_session_facts(root_session, dispatch)
        root_only_home = control / "root-only-home"
        (root_only_home / "sessions").mkdir(parents=True)
        if root_session is not None:
            shutil.copyfile(root_session, root_only_home / "sessions" / "root.jsonl")
        invocation = session_skill_evidence(root_only_home, runtime, skill_name="mission-review")
        (
            boundary,
            permission_entries,
            repository_grant,
            unexpected_permission_grants,
            arg0_control_file_count,
        ) = managed_root_boundary(
            root_facts.get("turn_context"),
            isolated_home=isolated_home,
            workspace=workspace,
            runtime=runtime,
            temp_dir=temp_dir,
            codex_bin=codex_bin,
            expected_read_grants=spec.read_grants,
        )
        accesses = [
            asdict(item)
            for item in command_events(
                execution.events,
                cwd=workspace,
                known_paths=[
                    REPOSITORY,
                    REPOSITORY / "evals" / "mission-review.md",
                    REPOSITORY / "evals" / "runs",
                    REPOSITORY / "evals" / "cases",
                    REPOSITORY / "evals" / "fixtures",
                    REPOSITORY / "docs" / "reviews",
                    candidate,
                    *list(runtime.rglob("*")),
                    *list(workspace.rglob("*")),
                ],
            )
        ]
        forbidden_accesses = source_accesses(accesses)
        session_source_mentions: list[str] = []
        for session in sorted((isolated_home / "sessions").rglob("*.jsonl")):
            if str(REPOSITORY) in session.read_text(encoding="utf-8", errors="replace"):
                session_source_mentions.append(session.relative_to(isolated_home).as_posix())
        preserve_execution(case_dir, isolated_home, control, execution)
        write_manifest(case_dir / "workspace-after.json", workspace_after)
        write_manifest(case_dir / "runtime-after.json", runtime_after)
        (case_dir / "workspace-diff.json").write_text(
            json.dumps(workspace_diff, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        (case_dir / "runtime-diff.json").write_text(
            json.dumps(runtime_diff, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        (case_dir / "skill-invocation-evidence.json").write_text(
            json.dumps(invocation, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        (case_dir / "access-events.json").write_text(
            json.dumps(accesses, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        (case_dir / "root-session-evidence.json").write_text(
            json.dumps(
                {
                    "stdout_thread_id": execution.thread_id,
                    "root_session": (
                        root_session.relative_to(isolated_home).as_posix() if root_session else None
                    ),
                    "root_session_errors": root_session_errors,
                    "facts": root_facts,
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        (case_dir / "permission-boundary.json").write_text(
            json.dumps(
                {
                    "valid": boundary,
                    "repository_grant": repository_grant,
                    "path_entries": permission_entries,
                    "expected_case_read_grants": list(spec.read_grants),
                    "unexpected_permission_grants": unexpected_permission_grants,
                    "arg0_control_file_count": arg0_control_file_count,
                    "forbidden_source_accesses": forbidden_accesses,
                    "session_source_mentions": session_source_mentions,
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        shutil.copytree(workspace, case_dir / "workspace-final")
        shutil.copytree(runtime, case_dir / "retained-runtime-bundle")
        final = execution.final or {}
        retained_auth_files = sorted(
            path.relative_to(case_dir).as_posix()
            for path in case_dir.rglob("*")
            if path.is_file() and path.name in {"auth.json", ".credentials.json"}
        )
        retained_hashes = {
            sha256(path): path.relative_to(case_dir).as_posix()
            for path in case_dir.rglob("*")
            if path.is_file()
        }
        auth_digest_collisions = sorted(
            {
                retained_hashes[digest]
                for digest in auth_source_hashes.values()
                if digest in retained_hashes
            }
        )
        pass_conditions = {
            "isolation_established": isolation.established,
            "returncode_zero": execution.returncode == 0,
            "jsonl_complete": execution.jsonl_complete,
            "no_unknown_executor_error_events": not unknown_error_events,
            "structured_final": execution.final is not None,
            "fresh_thread_observed": bool(execution.thread_id),
            "root_session_bound_to_stdout_thread": root_session is not None and not root_session_errors,
            "root_session_parse_complete": not root_facts["parse_errors"],
            "exact_dispatch_observed_once": root_facts["dispatch_count"] == 1,
            "requested_model_resolved_in_root_session": root_facts["model"] == model,
            "managed_root_boundary_observed": boundary,
            "no_repository_permission_grant": not repository_grant,
            "no_source_repository_access": not forbidden_accesses,
            "source_repository_absent_from_sessions": not session_source_mentions,
            "skill_evidence_complete": invocation["evidence_complete"],
            "single_complete_injection": invocation["injection_count"] == 1,
            "no_invalid_injections": not invocation["invalid_injections"],
            "catalog_hidden": not invocation["catalog_present"],
            "runtime_identity_unchanged": (
                runtime_digest_before == runtime_digest_after and not runtime_diff
            ),
            "workspace_unchanged": not workspace_diff,
            "no_reported_artifacts": final.get("artifact_paths") == [],
            "no_retained_auth_files": not retained_auth_files,
            "no_auth_file_digest_collision": not auth_digest_collisions,
        }
        result = {
            "case_id": spec.case_id,
            "capture_status": "PENDING_CLEANUP",
            "behavior_verdict": "NOT_GRADED",
            "requested_model": model,
            "root_session_model": root_facts["model"],
            "adapter_observed_model": execution.resolved_model,
            "thread_id": execution.thread_id,
            "returncode": execution.returncode,
            "runtime_digest_before": runtime_digest_before,
            "runtime_digest_after": runtime_digest_after,
            "pass_conditions": pass_conditions,
            "execution_uncertainty": execution.uncertainty,
            "executor_error_events": {
                "known_non_fatal": known_non_fatal_errors,
                "unknown": unknown_error_events,
            },
            "reported_uncertainty": final.get("consequential_uncertainty"),
            "auth": {
                "copied_file_names": list(auth.copied_files),
                "uses_api_key_environment": auth.uses_api_key_environment,
                "uncertainty": list(auth.uncertainty),
                "retained_auth_files": retained_auth_files,
                "retained_full_file_digest_collisions": auth_digest_collisions,
            },
            "isolation": isolation.to_dict(),
            "response": final.get("response"),
        }
        (case_dir / "result.json").write_text(
            json.dumps(result, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    finally:
        try:
            make_tree_removable(root)
            shutil.rmtree(root)
        except OSError as exc:
            cleanup_error = f"{type(exc).__name__}: {exc}"
    if result is None:
        raise RuntimeError(f"case {spec.case_id} ended without a preserved result")
    cleanup_verified = not root.exists() and cleanup_error is None
    result["cleanup"] = {
        "temporary_root_removed": cleanup_verified,
        "error": cleanup_error,
    }
    result["pass_conditions"]["temporary_root_removed"] = cleanup_verified
    result["capture_status"] = (
        "PASSED" if all(result["pass_conditions"].values()) else "FAILED"
    )
    (case_dir / "result.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", type=Path, default=REPOSITORY / "mission-review")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--codex-bin", type=Path, default=Path(shutil.which("codex") or "codex"))
    parser.add_argument("--model", default="gpt-5.6-sol")
    parser.add_argument("--timeout-seconds", type=int, default=900)
    parser.add_argument("--case", action="append", choices=sorted(CASES))
    parser.add_argument("--preflight", action="store_true")
    args = parser.parse_args()
    candidate = args.candidate.resolve()
    selected = args.case or sorted(CASES)
    frozen = preflight(candidate, selected, args.codex_bin, args.model, args.timeout_seconds)
    frozen["runner"]["argv"] = sys.argv
    if args.preflight:
        print(json.dumps(frozen, ensure_ascii=False, indent=2))
        return 0
    if args.output is None:
        raise SystemExit("--output is required unless --preflight is used")
    output = args.output.resolve()
    if output.exists():
        raise SystemExit(f"refusing to overwrite existing output: {output}")
    output.mkdir(parents=True)
    (output / "preflight.json").write_text(
        json.dumps(frozen, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    results: list[dict[str, object]] = []
    for case_id in selected:
        result = run_case(
            spec=CASES[case_id],
            candidate=candidate,
            output=output,
            codex_bin=args.codex_bin,
            model=args.model,
            timeout_seconds=args.timeout_seconds,
        )
        results.append(result)
        print(json.dumps({"case_id": case_id, "capture_status": result["capture_status"]}))
        if result["capture_status"] != "PASSED":
            break
    thread_ids = [item.get("thread_id") for item in results if isinstance(item.get("thread_id"), str)]
    suite_conditions = {
        "complete_eight_case_set": selected == sorted(CASES),
        "all_case_capture_passed": all(item["capture_status"] == "PASSED" for item in results),
        "eight_unique_threads": len(thread_ids) == len(CASES) and len(set(thread_ids)) == len(CASES),
    }
    summary = {
        "capture_status": "PASSED" if all(suite_conditions.values()) else "FAILED",
        "behavior_verdict": "NOT_GRADED",
        "suite_conditions": suite_conditions,
        "candidate": frozen["candidate"],
        "model": args.model,
        "selected_cases": selected,
        "cases": results,
    }
    (output / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    hashes = evidence_hashes(output)
    evidence_manifest = {
        "algorithm": "SHA-256 over each relative path and file digest; evidence-manifest.json excluded",
        "file_count": len(hashes),
        "files": hashes,
        "aggregate": digest_mapping(hashes),
    }
    (output / "evidence-manifest.json").write_text(
        json.dumps(evidence_manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if summary["capture_status"] == "PASSED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
