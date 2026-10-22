#!/usr/bin/env python3
"""Validate the GH-MAX documentary DAG; never execute GitHub or change permissions."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = "docs/github-app/GH_MAX_EXECUTION_PLAN.json"
SOURCE = "docs/github-app/GATEWAY_IMPLEMENTATION_GATES.md"
TASK_ID = re.compile(r"GH-MAX-\d{2}")


def validate(plan: dict, documented: str) -> list[dict]:
    assert plan["kind"] == "documentary_execution_projection"
    assert plan["status"] == "DRAFT_NOT_APPROVED_NOT_RUNTIME"
    assert plan["app"]["app_id"] == 5417646
    assert plan["execution_enabled"] is False, "Never enable runtime from a documentary manifest"
    assert plan["mutations_enabled"] is False, "Documentary plans cannot authorize GitHub writes"
    guard = plan["invariant_policy"]
    required_guards = (
        "preserve_existing_github_app", "prohibit_mcp_grt_writes",
        "no_implicit_agent_authority", "no_credentials_in_repo",
        "never_disable_branch_rules_to_pass_ci",
        "never_auto_approve_permission_changes", "never_mark_done_without_verified_proof",
        "never_create_duplicate_agent_mission_issue_or_branch",
        "enforce_live_installation_token_mandate_and_policy",
    )
    assert all(guard.get(key) is True for key in required_guards), "Missing mandatory security invariant"
    assert plan["state_machine"]["on_missing_authorization"] == "AWAITING_APPROVAL"
    assert plan["state_machine"]["on_missing_proof"] == "AWAITING_EVIDENCE"
    assert "approval_denied" in plan["state_machine"]["no_auto_retry_on"]
    sources = plan["source_of_truth"]
    assert sources["intent"] == "docs/github-app/CAHIER_DES_CHARGES_COMPLET.md"
    assert sources["status_and_gates"] == SOURCE
    tasks = plan["tasks"]
    expected = [f"GH-MAX-{number:02d}" for number in range(1, 11)]
    actual = [item["id"] for item in tasks]
    assert actual == expected, "Exactly ten original GH-MAX IDs in chronological order required"
    documented_ids = re.findall(r"^\|\s*\d{2}\s*\|\s*\x60(GH-MAX-\d{2})\x60\s*\|", documented, re.MULTILINE)
    assert documented_ids == expected, "Execution projection disagrees with the canonical GH-MAX table"
    seen: set[str] = set()
    for task in tasks:
        tid = task["id"]
        assert TASK_ID.fullmatch(tid)
        dependencies = task["depends_on"]
        assert len(dependencies) == len(set(dependencies))
        assert all(dep in seen for dep in dependencies), f"Bad DAG/order for {tid}"
        assert task["lifecycle_status"] == "PLANNED", "Runtime state belongs elsewhere"
        assert task["admitted"] is False
        assert task["mutating_actions_authorized"] is False
        assert task["proof_refs"] == []
        assert task["runtime_executor"] is None
        assert task["source_ref"].startswith("GATEWAY_IMPLEMENTATION_GATES.md")
        assert task["proof_types"] and task["requirements"] and task["blocked_if"]
        if task["mode"] == "SENSITIVE_EXTERNAL_WRITE":
            assert tid == "GH-MAX-06"
            assert "owner_approval_each_installation" in task["requirements"]
            assert "approval_absent" in task["blocked_if"]
        seen.add(tid)
    assert plan["evidence_contract"]["proof_refs_required_for_done"] is True
    assert plan["evidence_contract"]["authorities_must_be_reresolved_on_resume"] is True
    return tasks


def preview(tasks: list[dict], completed: set[str]) -> list[str]:
    """Dependency-only simulation, NOT admission, authorization, or runtime state."""
    known = {t["id"] for t in tasks}
    if completed - known:
        raise ValueError(f"Unknown task IDs: {sorted(completed - known)}")
    return [t["id"] for t in tasks if t["id"] not in completed
            and all(dep in completed for dep in t["depends_on"])]


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only GH-MAX plan validator/preview")
    parser.add_argument("--next", action="store_true", help="Preview dependency candidates; never dispatch")
    parser.add_argument("--simulate-completed", nargs="*", default=[], metavar="GH-MAX-NN")
    args = parser.parse_args()
    if args.simulate_completed and not args.next:
        parser.error("--simulate-completed requires --next")
    try:
        plan = json.loads((ROOT / MANIFEST).read_text(encoding="utf-8"))
        doc = (ROOT / SOURCE).read_text(encoding="utf-8")
        tasks = validate(plan, doc)
        if args.next:
            print(json.dumps({"mode": "SIMULATION_ONLY", "runtime_execution": False,
                              "needs_independent_authorization": True,
                              "dependency_candidates": preview(tasks, set(args.simulate_completed))},
                             ensure_ascii=False, indent=2))
        else:
            print("PASS 10 GH-MAX tasks, no duplicates, DAG topological, permissions fail closed")
            print("NO_RUNTIME_EXECUTION / NO_GITHUB_WRITES / NO_PERMISSION_CHANGES")
    except (OSError, KeyError, TypeError, ValueError, AssertionError) as exc:
        print(f"FAIL {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
