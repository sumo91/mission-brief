#!/usr/bin/env python3
"""One isolated author -> executor -> reviewer chain using the existing harness."""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import subprocess
import sys
import tempfile
from pathlib import Path

import run_mission_brief_behavior as behavior
from mission_brief_eval.candidate import identify
from mission_brief_eval.eval_pack import _effective_content, _parse_case, _parse_skill_contract, digest_value
from mission_brief_eval.models import EvalPack, EvalPackIdentity, RunConfig
from mission_brief_eval.runner import HarnessRunner

ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / 'evals/mission-handoff-execution.json'
CASE_ID = 'h-60000001'
RUNNER_BYTES = Path(__file__).read_bytes()
INPUT_BYTES = INPUT.read_bytes()
BASE_HARNESS_IDENTITY = behavior.harness_runner_module.harness_identity
BASE_CONFIG = behavior.harness_runner_module.write_isolated_config
PYTHON_ROOT = Path(sys.executable).resolve().parents[1]
PYTHON = str(Path(sys.executable).resolve())


def config_with_python(**kwargs):
    path = BASE_CONFIG(**kwargs)
    value = path.read_text()
    marker = '\n[permissions.eval-executor.network]'
    assert value.count(marker) == 1 and not PYTHON_ROOT.is_relative_to(ROOT)
    value = value.replace(marker, f'\n{json.dumps(str(PYTHON_ROOT))} = "read"\n' + marker)
    value = value.replace('PATH = "/opt/homebrew/bin:', f'PATH = "{PYTHON_ROOT}/bin:/opt/homebrew/bin:')
    path.write_text(value + 'PYTHONDONTWRITEBYTECODE = "1"\n')
    return path


behavior.harness_runner_module.write_isolated_config = config_with_python


def execution_harness_identity():
    digest = hashlib.sha256(BASE_HARNESS_IDENTITY().encode())
    digest.update(RUNNER_BYTES)
    digest.update(INPUT_BYTES)
    return digest.hexdigest()


behavior.harness_runner_module.harness_identity = execution_harness_identity


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def pack_from_source(source):
    """Narrow schema exception: a semantic case may explicitly forbid Skills.

    Like the existing blind runner, retain and reparse the actual source. All
    isolation, trace, model, invocation and semantic checks remain in the harness.
    """
    raw = json.loads(source.read_text())
    contract = _parse_skill_contract(raw['skill_contract'])
    cases = tuple(_parse_case(c, index=i, pack_root=source.parent)[0] for i, c in enumerate(raw['cases']))
    assert len(cases) == 1 and cases[0].opaque_id == CASE_ID
    assert cases[0].rubric and cases[0].turns[0].expected_invocation in {'required', 'forbidden'}
    capabilities = ('local-files', 'local-process')
    effective = _effective_content(schema_version='1.0', pack_id=raw['pack_id'],
        pack_version='1.0.0', display_name=raw['display_name'], capabilities=capabilities,
        skill_contract=contract, cases=cases)
    identity = EvalPackIdentity(source=str(source), digest=digest_value(effective),
        pack_id=raw['pack_id'], pack_version='1.0.0', schema_version='1.0',
        display_name=raw['display_name'], capability_requirements=capabilities,
        source_files=(source.name,))
    return EvalPack(identity=identity, skill_contract=contract, cases=cases, source_paths=(source,))


class ExecutionRunner(HarnessRunner):
    def __init__(self, config):
        assert pack_from_source(Path(config.eval_pack.identity.source)) == config.eval_pack
        self.config = config
        self.candidate_identity = identify(config.candidate, config.eval_pack.skill_contract)


def capture_complete(report, expected_turns):
    return (len(report.cases) == 1
        and len(report.cases[0].turns) == expected_turns
        and all(t.trace_complete and t.final is not None and not t.parse_errors
                for t in report.cases[0].turns))


def phase(args, name, candidate, contract_name, fixtures, prompts, rubric, invoke, companion=None):
    destination = args.output_dir / name
    contract = json.loads((ROOT / f'evals/{contract_name}-pack.json').read_text())['skill_contract']
    contract['artifact_path_prefixes'] = ['docs', 'project', 'artifacts']
    contract['artifact_path_suffixes'] = ['.md', '.py', '.json', '.csv', '.txt', '.log', '.sh', '.pyc']
    contract['protected_project_files'] = []
    contract['semantic_judge_policy'] = (
        'Judge the actual commissioned phase, source fidelity, authority and observable results. '
        'Do not demand a new user decision for already explicit instructions. '
        'Judge semantic behavior, not preferred wording, implementation or absence declarations. '
        'A review must inspect the delivered result against original acceptance, including any omitted contract promises.'
    )
    turns = []
    for i, prompt in enumerate(prompts):
        prompt += '\n结构化输出的 artifact_paths 只列实际写入且保留在工作区的文件；临时探针文件不要列入，决定性观察写入响应或持久报告。'
        assertions = {'artifact_count': None}
        if not invoke:
            assertions['runtime_reference'] = 'forbidden'
        if i == 0:
            assertions['skill_invocation'] = 'required' if invoke else 'forbidden'
        turns.append({'prompt': prompt, 'assertions': assertions})
    raw = {'schema_version': '1.0', 'platform_contract': 'skill-eval-pack-v1',
        'pack_id': 'mission-real-handoff-' + name, 'pack_version': '1.0.0',
        'display_name': 'Mission real handoff ' + name,
        'capability_requirements': ['local-files', 'local-process'], 'skill_contract': contract,
        'cases': [{'id': CASE_ID, 'suite': 'behavior', 'turns': turns,
            'fixtures': [{'path': p, 'content': c} for p, c in sorted(fixtures.items())], 'rubric': rubric}]}
    source = destination / 'input-pack.json'
    write_json(source, raw)
    behavior.configure_evaluation('medium', companion,
        ROOT / 'evals/mission-align-pack.json' if companion else None)
    pack = pack_from_source(source.resolve())
    config = RunConfig(candidate=candidate.resolve(), eval_pack=pack, output_dir=destination.resolve(),
        codex_bin=args.codex_bin, model=args.model, judge_model=args.model,
        judge=True, keep_workspaces=True, timeout_seconds=args.timeout)
    report = ExecutionRunner(config).run('behavior')
    run = config.output_dir / report.run_id
    behavior.write_run_contract(run, report)
    write_json(run / 'evidence-manifest.json', behavior.evidence_manifest(run))
    print(json.dumps({'phase': name, 'verdict': report.verdict.value, 'report': str(run / 'report.json')}), flush=True)
    if not capture_complete(report, len(prompts)):
        write_json(args.output_dir / 'chain-result.json', {
            'trial_status': 'INCOMPLETE', 'capture_status': 'INCOMPLETE',
            'stopped_phase': name, 'phase_verdict': report.verdict.value,
            'report': str(run / 'report.json'),
            'reason': 'Expected turns, final output or trace are incomplete; no delivery conclusion.'})
        write_json(args.output_dir / 'evidence-manifest.json', behavior.evidence_manifest(args.output_dir))
        raise SystemExit(1)
    return report, run, run / 'cases' / CASE_ID / 'workspace-final'


def text_files(root):
    result = {}
    for path in sorted(root.rglob('*')):
        if path.is_file() and not path.is_symlink() and '__pycache__' not in path.parts:
            try:
                result[path.relative_to(root).as_posix()] = path.read_text()
            except UnicodeDecodeError:
                raise ValueError(f'Unexpected non-text handoff artifact: {path}')
    return result


def acceptance(task, workspace):
    """Run private input probes in a separate temporary copy of the delivery."""
    import shutil
    observations = []
    checks = {}
    with tempfile.TemporaryDirectory(prefix='mission-handoff-oracle-') as directory:
        project = Path(directory) / 'project'
        shutil.copytree(workspace / 'project', project)

        def call(script, arguments=(), stdin=None):
            command = [sys.executable, str(project / script), *arguments]
            try:
                run = subprocess.run(command, cwd=project, input=stdin, text=True,
                    capture_output=True, timeout=15)
                item = {'command': [script, *arguments], 'code': run.returncode,
                    'stdout': run.stdout, 'stderr': run.stderr}
            except subprocess.TimeoutExpired:
                item = {'command': [script, *arguments], 'code': None, 'stdout': '', 'stderr': 'timeout'}
            observations.append(item)
            return item

        if task['id'] == 'T1':
            for i, arguments in enumerate((['--version', '--format', 'json'], ['--format', 'json', '--version'])):
                out = call('status_cli.py', arguments)
                try:
                    payload = json.loads(out['stdout'])
                except ValueError:
                    payload = None
                checks[f'json-order-{i}'] = out['code'] == 0 and payload == {'name': 'mission-tool', 'version': '2.4.0'}
            for label, arguments, expected in [('legacy', ['--version'], 'mission-tool 2.4.0\n'), ('default', [], 'Ready\n')]:
                out = call('status_cli.py', arguments)
                checks[label] = out['code'] == 0 and out['stdout'] == expected and not out['stderr']
            for arguments in (['--nonsense'], ['--format', 'xml', '--version'], ['--version', '--format', 'xml'], ['--version', '--format']):
                out = call('status_cli.py', arguments)
                checks['error-' + arguments[0] + arguments[-1]] = out['code'] == 2 and bool(out['stderr']) and not out['stdout']
            (project / 'private-baseline.py').write_text(task['files']['status_cli.py'])
            for i, arguments in enumerate((['--version', '--nonsense'], ['--nonsense', '--version'], ['unexpected'], ['--version=x'], ['--version', '--f'], ['--f', 'json'])):
                old = call('private-baseline.py', arguments)
                new = call('status_cli.py', arguments)
                checks[f'legacy-invalid-{i}'] = (new['code'], new['stdout'], bool(new['stderr'])) == (old['code'], old['stdout'], bool(old['stderr']))
        else:
            refunds = [
                {'id': 'r1', 'status': 'TERMINAL_FAILED', 'reason': '拒绝,"需复核"\n下一行', 'processor_reason': 'unused'},
                {'id': 'r2', 'status': 'PENDING', 'reason': 'pending'},
                {'id': 'r3', 'status': 'TERMINAL_FAILED', 'reason': '', 'processor_reason': '银行,失败'},
                {'id': 'r4', 'status': 'FAILED', 'reason': 'not terminal'},
                {'id': 'r5', 'status': 'TERMINAL_FAILED', 'processor_reason': 'fallback'},
                {'id': 'r6', 'status': 'SUCCEEDED', 'reason': ''},
            ]
            expected = [{'id': r['id'], 'reason': r.get('reason') or r.get('processor_reason', '')}
                for r in refunds if r['status'] == 'TERMINAL_FAILED']
            (project / 'private-input.json').write_text(json.dumps(refunds, ensure_ascii=False))
            out = call('refund_export.py', ['private-input.json'])
            try:
                reader = csv.DictReader(io.StringIO(out['stdout']))
                rows = list(reader)
                checks['csv'] = out['code'] == 0 and reader.fieldnames == ['id', 'reason'] and rows == expected
            except csv.Error:
                checks['csv'] = False
            out = call('refund_export.py', ['private-input.json', '--format', 'json'])
            try:
                payload = json.loads(out['stdout'])
            except ValueError:
                payload = None
            checks['json-v2'] = out['code'] == 0 and payload == {'schema_version': 2, 'refunds': expected}
            consumer = call('consume.py', stdin=out['stdout'])
            checks['consumer'] = consumer['code'] == 0 and consumer['stdout'] == 'r1,r3,r5\n'
            (project / 'private-bad.json').write_text('{broken')
            out = call('refund_export.py', ['private-bad.json'])
            checks['malformed'] = out['code'] == 2 and bool(out['stderr']) and not out['stdout']
            checks['consumer-preserved'] = (workspace / 'project/consume.py').read_text() == task['files']['consume.py']
        checks['no-release'] = not list(workspace.rglob('release.log'))
    return {'passed': all(checks.values()), 'checks': checks, 'observations': observations}


def run_chain(args):
    args.output_dir = args.output_dir.resolve()
    if args.output_dir.exists():
        raise SystemExit('Use a fresh output directory; earlier results are immutable.')
    inputs = json.loads(INPUT_BYTES)
    task = next(t for t in inputs['tasks'] if t['id'] == args.task)
    args.output_dir.mkdir(parents=True)
    write_json(args.output_dir / 'frozen-input.json', inputs)
    (args.output_dir / 'runner.py').write_bytes(RUNNER_BYTES)
    fixtures = {'project/' + p: c for p, c in task['files'].items()}
    environment = ('\n项目与原始材料位于 project/；项目修改与测试放在该目录，委托文档路径相对于工作区根。'
        f'可用 Python 3 为 {PYTHON}，已授予其运行时读取权限。')
    prefix = '$mission-brief ' if args.arm != 'M' else '用简短文档记录已定结果、成功条件、证据和边界，有重大缺口时才问；不要调用任何 Skill。\n'
    prompts = [prefix + task['request'] + environment]
    if task.get('amendment'):
        prompts.append(task['amendment'])
    author, author_run, authored = phase(args, 'author', args.candidate, 'mission-brief', fixtures, prompts,
        ['Finish the requested contract document without implementing code; retain each source status and only ask consequential missing decisions.',
         'The final contract and retained material faithfully preserve all current original requirements and amendments, including granted local authority and remaining external gates.'],
        args.arm != 'M', args.candidate / 'mission-align' if args.arm != 'M' else None)
    if not (authored / task['brief']).is_file():
        write_json(args.output_dir / 'chain-result.json', {
            'trial_status': 'INCOMPLETE', 'capture_status': 'COMPLETE',
            'reason': 'No contract produced. Inspect the author response for an unanswered decision or authoring failure; no automatic answer was supplied.',
            'phase_verdicts': {'author': author.verdict.value},
            'runs': {'author': str(author_run / 'report.json')}})
        write_json(args.output_dir / 'evidence-manifest.json', behavior.evidence_manifest(args.output_dir))
        return 1
    handoff = text_files(authored)
    for path in list(handoff):
        if any(path == 'project/' + p or path.startswith('project/' + p + '/') for p in task['transient_paths']):
            del handoff[path]
    executor_prompt = ('你是没有参与合同编写的新执行 Agent。读取 ' + task['brief'] +
        ' 及它所需的持久材料，完成已委托结果并实际运行相称检查。项目代码位于 project/，修改与测试留在该目录。'
        '执行权限和外部边界以交接合同为准。不要调用任何 Skill。完成实际交付后结束。'
        f'可用 Python 3 为 {PYTHON}，可直接运行，已授予其运行时读取权限。')
    executed, execute_run, delivered = phase(args, 'execute', args.candidate, 'mission-brief', handoff, [executor_prompt],
        ['Complete the commissioned local implementation and proportionate actual checks from the visible handoff, without inventing authority or stopping at a plan.',
         'Respect current compatibility and source status; do not perform or claim external publication.'], False)
    oracle = acceptance(task, delivered)
    write_json(args.output_dir / 'acceptance.json', oracle)
    review_files = text_files(delivered)
    review_files['artifacts/original-acceptance.md'] = '# Original acceptance\n\n' + '\n'.join('- ' + x for x in task['acceptance'])
    review_prompt = ('$mission-review 检查 ' + task['brief'] + ' 的当前实际交付。原始验收要求在 artifacts/original-acceptance.md，'
        '不能因为合同遗漏就免除原始承诺。实际使用项目并给出有证据的 PASSED、FAILED 或 INCONCLUSIVE；不要修复产物。'
        '所需测试临时数据放在临时目录，审查结束保持交付文件不变。'
        '为准确采集裁决，response 第一行严格写 Delivery verdict: PASSED、Delivery verdict: FAILED 或 Delivery verdict: INCONCLUSIVE 中的一项，随后解释证据。'
        f'可用 Python 3 为 {PYTHON}，已授予其运行时读取权限。')
    reviewed, review_run, _ = phase(args, 'review', args.review_candidate, 'mission-review', review_files, [review_prompt],
        ['Actually exercise the delivered user behavior against original acceptance and the current contract; identify decisive failures or evidence gaps and give a justified verdict.',
         'Review the delivered version before any repair; do not change product code, the contract, or original acceptance.'], True)
    review_response = reviewed.cases[0].turns[-1].raw_response
    verdict = delivery_verdict(review_response)
    result = {'trial_status': 'COMPLETE', 'capture_status': 'COMPLETE',
        'arm': args.arm, 'task': args.task, 'model': args.model, 'reasoning_effort': 'medium',
        'input_sha256': hashlib.sha256(INPUT_BYTES).hexdigest(),
        'runner_sha256': hashlib.sha256(RUNNER_BYTES).hexdigest(),
        'python_executable': sys.executable, 'python_runtime_read_grant': str(PYTHON_ROOT),
        'runs': {k: str(p / 'report.json') for k, p in [('author', author_run), ('execute', execute_run), ('review', review_run)]},
        'phase_verdicts': {name: report.verdict.value for name, report in
            [('author', author), ('execute', executed), ('review', reviewed)]},
        'oracle': oracle, 'review_delivery_verdict': verdict, 'review_response': review_response,
        'author_user_turns': len(author.cases[0].turns)}
    write_json(args.output_dir / 'chain-result.json', result)
    write_json(args.output_dir / 'evidence-manifest.json', behavior.evidence_manifest(args.output_dir))
    print(json.dumps({'chain': str(args.output_dir), 'trial_status': result['trial_status'],
        'oracle_passed': oracle['passed'], 'review_delivery_verdict': verdict}), flush=True)
    return 0


def delivery_verdict(raw_response):
    try:
        line = raw_response.splitlines()[0]
    except (AttributeError, IndexError):
        return 'INCONCLUSIVE'
    return next((v for v in ('PASSED', 'FAILED', 'INCONCLUSIVE') if line == 'Delivery verdict: ' + v), 'INCONCLUSIVE')


def self_test():
    from types import SimpleNamespace
    assert delivery_verdict('Delivery verdict: FAILED\nReview correctly completed.') == 'FAILED'
    assert delivery_verdict('All checks PASSED; delivery INCONCLUSIVE.') == 'INCONCLUSIVE'
    assert delivery_verdict('Delivery verdict: PASSED\nEvidence follows.') == 'PASSED'
    turn = SimpleNamespace(trace_complete=True, final={'response': 'Delivery failed'}, parse_errors=[])
    report = SimpleNamespace(cases=[SimpleNamespace(turns=[turn])], verdict='FAILED')
    assert capture_complete(report, 1)  # A captured failure is still a complete capture.
    assert not capture_complete(report, 2)
    turn.trace_complete = False
    assert not capture_complete(report, 1)
    turn.trace_complete = True
    turn.final = None
    assert not capture_complete(report, 1)
    data = json.loads(INPUT.read_text())
    with tempfile.TemporaryDirectory() as d:
        root = Path(d); (root / 'project').mkdir()
        t1 = data['tasks'][0]
        (root / 'project/status_cli.py').write_text(t1['files']['status_cli.py'])
        assert not acceptance(t1, root)['passed']
        working = "import argparse,json,sys\np=argparse.ArgumentParser()\nif '--format' not in sys.argv:\n    p.add_argument('--version',action='version',version='mission-tool 2.4.0')\n    p.parse_args()\n    print('Ready')\nelse:\n    p.add_argument('--version',action='store_true')\n    p.add_argument('--format',choices=['json'])\n    a=p.parse_args()\n    print(json.dumps({'name':'mission-tool','version':'2.4.0'}) if a.version and a.format=='json' else 'mission-tool 2.4.0' if a.version else 'Ready')\n"
        (root / 'project/status_cli.py').write_text(working)
        assert acceptance(t1, root)['passed']
        (root / 'project/status_cli.py').write_text(working.replace("if '--format' not in sys.argv:", 'if False:'))
        changed = acceptance(t1, root)
        assert not changed['checks']['legacy-invalid-4'] and not changed['checks']['legacy-invalid-5']
        (root / 'project/status_cli.py').write_text(working.replace('2.4.0', '9.9.9'))
        assert not acceptance(t1, root)['passed']
        t2 = data['tasks'][1]
        for name in ('refund_export.py', 'consume.py'):
            (root / 'project' / name).write_text(t2['files'][name])
        assert not acceptance(t2, root)['passed']
        working = t2['files']['refund_export.py'].replace(
            "parser.add_argument('input')", "parser.add_argument('input')\n    parser.add_argument('--format', choices=['csv', 'json'], default='csv')")
        start = working.index('    writer = csv.writer')
        end = working.index('    return 0', start)
        working = working[:start] + (
            "    rows = [{'id': r['id'], 'reason': r.get('reason') or r.get('processor_reason', '')} for r in refunds if r['status'] == 'TERMINAL_FAILED']\n"
            "    if args.format == 'json':\n        print(json.dumps({'schema_version': 2, 'refunds': rows}))\n"
            "    else:\n        writer = csv.DictWriter(sys.stdout, fieldnames=['id', 'reason'])\n        writer.writeheader()\n        writer.writerows(rows)\n"
        ) + working[end:]
        (root / 'project/refund_export.py').write_text(working)
        assert acceptance(t2, root)['passed']
        (root / 'project/refund_export.py').write_text(working.replace("r.get('processor_reason', '')", "''"))
        assert not acceptance(t2, root)['passed']
    print('Handoff self-test passed: capture completeness, verdict parsing and compatible/mutated delivery.')


if __name__ == '__main__':
    if sys.argv[1:] == ['--self-test']:
        self_test()
    else:
        parser = argparse.ArgumentParser(description=__doc__)
        parser.add_argument('--candidate', type=Path, required=True)
        parser.add_argument('--review-candidate', type=Path, required=True)
        parser.add_argument('--arm', choices=['B', 'S2', 'M'], required=True)
        parser.add_argument('--task', choices=['T1', 'T2'], required=True)
        parser.add_argument('--output-dir', type=Path, required=True)
        parser.add_argument('--model', default='gpt-6-astra')
        parser.add_argument('--codex-bin', type=Path, default=Path('/Applications/ChatGPT.app/Contents/Resources/codex'))
        parser.add_argument('--timeout', type=int, default=900)
        raise SystemExit(run_chain(parser.parse_args()))
