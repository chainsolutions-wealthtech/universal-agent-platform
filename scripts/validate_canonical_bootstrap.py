#!/usr/bin/env python3
"""Read-only bootstrap validation. Documentary integrity != full security certification."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORIGINAL = "docs/archive/TEXTE_COMPLEMENTAIRE_ORIGINAL_20261021.txt"
MASTER = "docs/archive/PLAN_DIRECTEUR_UNIFIE_V5_20261021.md"
ROADMAP = "docs/roadmap/ROADMAP_V5.json"
LEGACY_ALIAS = "sources/TEXTE_COMPLEMENTAIRE_ORIGINAL_20261021.txt"
CANONICAL_SOURCES = frozenset((ORIGINAL, MASTER, ROADMAP))

# Construct patterns across string fragments so the validator never flags itself.
KEY_HEADER = re.compile(
    r"-----" + r"BEGIN[ \t]+(?:(?:RSA|DSA|EC|OPENSSH|ENCRYPTED)[ \t]+)?PRIVATE[ \t]+KEY-----",
    re.IGNORECASE,
)
PGP_PRIVATE_HEADER = re.compile(r"-----" + r"BEGIN[ \t]+PGP[ \t]+PRIVATE[ \t]+KEY[ \t]+BLOCK-----", re.IGNORECASE)
TOKEN = re.compile(r"(?:github_pat_[A-Za-z0-9_]{20,}|gh[opsur]_[A-Za-z0-9_]{20,})")


def verify_manifest(root: Path) -> None:
    data = json.loads((root / "docs/archive/IMPORT_MANIFEST.json").read_text(encoding="utf-8"))
    sources = data["sources"]
    paths = [item["path"] for item in sources]
    assert len(paths) == len(CANONICAL_SOURCES), "Canonical manifest source count changed"
    assert len(set(paths)) == len(paths), "Duplicate canonical manifest path"
    assert set(paths) == CANONICAL_SOURCES, "Canonical manifest missing or substituted a source"
    for item in sources:
        file = root / item["path"]
        assert file.is_file(), f"Missing canonical source: {item['path']}"
        raw = file.read_bytes()
        assert hashlib.sha256(raw).hexdigest() == item["sha256"], f"Source SHA-256 changed: {item['path']}"
        assert len(raw) == item["bytes"], f"Canonical source size changed: {item['path']}"
    canonical = (root / ORIGINAL).read_bytes()
    alias = root / LEGACY_ALIAS
    assert alias.is_file(), "Historical V5 source reference does not resolve"
    assert alias.read_bytes() == canonical, "Legacy source reference drifted from canonical original"
    legacy = json.loads((root / "sources/SOURCE_MANIFEST.json").read_text(encoding="utf-8"))
    canonical_entry = next(x for x in sources if x["path"] == ORIGINAL)
    assert legacy["source_path"] == LEGACY_ALIAS, "Wrong legacy manifest source"
    assert legacy["canonical_repository_path"] == ORIGINAL, "Wrong canonical mapping"
    assert legacy["sha256"] == canonical_entry["sha256"], "Legacy hash differs from canonical"
    assert legacy["bytes"] == canonical_entry["bytes"], "Legacy byte count differs from canonical"


def annex_rows(plan: str, annex: str) -> list[list[str]]:
    match = re.search(r"^## ANNEXE " + annex + r"\b[^\n]*\n(.*?)(?=^## ANNEXE [A-Z]\b|\Z)", plan, re.MULTILINE | re.DOTALL)
    assert match is not None, f"Missing master plan Annex {annex}"
    rows = []
    for line in match.group(1).splitlines():
        if not re.match(r"^\|\s*\d+\s*\|", line):
            continue
        parts = [part.strip() for part in line.split("|")[1:-1]]
        assert len(parts) == 4, f"Invalid Annex {annex} row columns"
        rows.append(parts)
    return rows


def verify_indexes(plan: str, mapping: dict, catalog: dict) -> None:
    annex_a = annex_rows(plan, "A")
    annex_b = annex_rows(plan, "B")
    items = mapping["items"]
    domains = catalog["domains"]
    assert len(annex_a) == len(items) == 20, "20-section source/index mismatch"
    assert len(annex_b) == len(domains) == 30, "30-domain source/index mismatch"
    for index, (raw, item) in enumerate(zip(annex_a, items), 1):
        assert int(raw[0]) == item["number"] == index, f"Mapping index mismatch at {index}"
        for field, original in (("source_title", raw[1]), ("v5_sections", raw[2]), ("treatment", raw[3])):
            assert item.get(field) == original and original, f"Corrupt mapping {field} at {index}"
    for index, (raw, item) in enumerate(zip(annex_b, domains), 1):
        assert int(raw[0]) == item["number"] == index, f"Catalog index mismatch at {index}"
        for field, original in (("domain", raw[1]), ("implementation_mode_from_original", raw[2]), ("status_v5", raw[3])):
            assert item.get(field) == original and original, f"Corrupt catalog {field} at {index}"
        assert item.get("verified_runtime") is False, "Untested capability represented as runtime verified"


def verify_chronological_plan(root: Path, lots: list[dict]) -> None:
    plan = (root / "docs/roadmap/PROGRAMME_CHRONOLOGIQUE_V5.md").read_text(encoding="utf-8")
    tasks = (root / "docs/roadmap/REGISTRE_TACHES_V5.md").read_text(encoding="utf-8")
    canonical_ids = [row["lot_id"] for row in lots]
    table_rows = re.findall(
        r"^\|\s*(\d+)\s*\|\s*(P\d{2})\s*\|\s*\*\*`([BFD]\d{2})`\*\*\s*\|",
        plan, re.MULTILINE
    )
    assert len(table_rows) == 46, "Chronological programme must list exactly 46 lots"
    assert [int(i) for i, _, _ in table_rows] == list(range(1, 47)), "Chronology numbering changed"
    ordered_ids = [lot_id for _, _, lot_id in table_rows]
    assert set(ordered_ids) == set(canonical_ids) and len(set(ordered_ids)) == 46, "Chronology drift or duplicated lot"
    assert sorted(set(phase for _, phase, _ in table_rows)) == [f"P{i:02d}" for i in range(10)], "Chronology phases changed"
    headings = re.findall(r"^#### ([BFD]\d{2}) — ", tasks, re.MULTILINE)
    assert headings == ordered_ids, "Task register does not follow the programme order"
    task_ids = re.findall(r"^- \*\*`([BFD]\d{2}-\d+)` — ", tasks, re.MULTILINE)
    expected = [f"{lot}-{i:02d}" for lot in ordered_ids for i in (1, 2, 3)]
    assert task_ids == expected, "Each lot must have three uniquely numbered draft tasks"
    # The plan preserves source requirements; never infer the lot's runtime status.
    assert "PROPOSED_EXECUTION_ORDER" in plan
    assert "TASK_SPECIFICATIONS_DRAFT" in tasks


def check_tree_security(root: Path) -> None:
    blocked_suffixes = {".key", ".pem", ".p12", ".pfx", ".p8", ".jks", ".keystore"}
    for path in root.rglob("*"):
        if not path.is_file() or ".git" in path.relative_to(root).parts:
            continue
        rel = path.relative_to(root)
        assert path.suffix.lower() not in blocked_suffixes, f"Forbidden key file: {rel}"
        assert not (path.name == ".env" or path.name.startswith(".env.") and path.name != ".env.example"), f"Forbidden env file: {rel}"
        raw = path.read_bytes()
        # Scan every tracked/checked-out file regardless of suffix, including disguised keys.
        s = raw.decode("utf-8", errors="replace")
        assert not KEY_HEADER.search(s), f"Private-key header in: {rel}"
        assert not PGP_PRIVATE_HEADER.search(s), f"PGP private-key header in: {rel}"
        assert not TOKEN.search(s), f"GitHub token pattern in: {rel}"


def verify(root: Path = ROOT) -> None:
    verify_manifest(root)
    source = (root / ORIGINAL).read_text(encoding="utf-8")
    chapters = re.findall(r"^##\s+(\d+)\.\s+", source, flags=re.MULTILINE)
    assert chapters == [str(i) for i in range(1, 21)], "20 original sections changed"
    plan = (root / MASTER).read_text(encoding="utf-8")
    assert "PLAN DIRECTEUR UNIFIÉ V5.0" in plan
    mapping = json.loads((root / "docs/roadmap/MAPPING_20_SECTIONS_V5.json").read_text(encoding="utf-8"))
    catalog = json.loads((root / "docs/roadmap/CATALOGUE_30_DOMAINES_V5.json").read_text(encoding="utf-8"))
    verify_indexes(plan, mapping, catalog)
    lots = json.loads((root / ROADMAP).read_text(encoding="utf-8"))["lots"]
    assert len(lots) == 46 and len({x["lot_id"] for x in lots}) == 46, "46 unique work packages required"
    valid_states = {"PLANNED", "READY", "IN_PROGRESS", "BLOCKED", "DONE", "CANCELLED", "SUPERSEDED"}
    assert all(x.get("status") in valid_states and isinstance(x.get("proof_refs", []), list) for x in lots)
    for lot in lots:
        if lot["status"] == "DONE":
            assert isinstance(lot.get("baseline_head"), str) and re.fullmatch(r"[0-9a-f]{40}", lot["baseline_head"]), f"Missing verified baseline SHA for {lot['lot_id']}"
            assert lot["proof_refs"] and all(isinstance(p, str) and p.strip() for p in lot["proof_refs"]), f"Missing evidence for completed lot {lot['lot_id']}"
    verify_chronological_plan(root, lots)
    state = json.loads((root / "state/CURRENT_STATE.json").read_text(encoding="utf-8"))
    assert state["project"] == "chainsolutions-wealthtech/universal-agent-platform"
    assert state["type"] == "documentary_bootstrap_snapshot"
    memory_live = state.get("plans", {}).get("canonical_memory_service_operational")
    memory_status = state.get("documentary_import", {}).get("operational_memory")
    assert isinstance(memory_live, bool), "Runtime memory flag must be boolean"
    if memory_live:
        assert memory_status in {"RUNNING", "OPERATIONAL"} and state.get("memory_runtime_proof_refs"), "Operational memory requires implementation and proof"
    else:
        assert memory_status not in {"RUNNING", "OPERATIONAL"}, "Documentary and runtime memory state conflict"
    check_tree_security(root)
    print("PASS canonical manifest complete, source SHA256 intact and original reference matches")
    print("PASS legacy source manifest, source SHA256 and preserved compatibility reference")
    print("PASS 20 sections and 30 GitHub domains content-equal to V5 Annexes A/B")
    print("PASS 46 chronologically numbered lots, 10 phases, 138 draft tasks and hardened secret-pattern scan")
    print("NOTE heuristic secret scan only; independent/dedicated security review still required")


if __name__ == "__main__":
    try:
        verify()
    except (AssertionError, OSError, KeyError, ValueError, UnicodeError) as exc:
        print(f"FAIL {exc}", file=sys.stderr)
        sys.exit(1)
