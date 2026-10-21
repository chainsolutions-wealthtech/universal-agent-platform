#!/usr/bin/env python3
"""Read-only stdlib validation of the V5 documentary bootstrap, not runtime authority."""
from __future__ import annotations
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "docs/archive/TEXTE_COMPLEMENTAIRE_ORIGINAL_20261021.txt"
PLAN = ROOT / "docs/archive/PLAN_DIRECTEUR_UNIFIE_V5_20261021.md"
ROADMAP = ROOT / "docs/roadmap/ROADMAP_V5.json"
STATE = ROOT / "state/CURRENT_STATE.json"
MANIFEST = ROOT / "docs/archive/IMPORT_MANIFEST.json"

def verify() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for item in manifest["sources"]:
        path = ROOT / item["path"]
        assert path.is_file(), f"Missing: {item['path']}"
        raw = path.read_bytes()
        assert hashlib.sha256(raw).hexdigest() == item["sha256"], f"SHA256 changed: {item['path']}"
        assert len(raw) == item["bytes"], f"Size changed: {item['path']}"
    chapters = re.findall(r"^##\s+(\d+)\.\s+", SRC.read_text(encoding="utf-8"), flags=re.MULTILINE)
    assert chapters == [str(i) for i in range(1, 21)], f"Expected 20 ordered source sections: {chapters}"
    plan = PLAN.read_text(encoding="utf-8")
    assert "PLAN DIRECTEUR UNIFIÉ V5.0" in plan
    assert "## ANNEXE A" in plan and "## ANNEXE B" in plan
    roadmap = json.loads(ROADMAP.read_text(encoding="utf-8"))
    lots = roadmap["lots"]
    assert len(lots) == 46, f"Expected 46 lots: {len(lots)}"
    keys = [x["lot_id"] for x in lots]
    assert len(set(keys)) == 46, "Duplicated lot ID"
    valid_states = {"PLANNED", "READY", "IN_PROGRESS", "BLOCKED", "DONE", "CANCELLED", "SUPERSEDED"}
    assert all(x.get("status") in valid_states and isinstance(x.get("proof_refs", []), list) for x in lots), "Invalid lot status/proof_refs"
    state = json.loads(STATE.read_text(encoding="utf-8"))
    assert state["project"] == "chainsolutions-wealthtech/universal-agent-platform"
    assert state["type"] == "documentary_bootstrap_snapshot", "Invalid snapshot type"
    assert isinstance(state.get("plans", {}).get("canonical_memory_service_operational"), bool)
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts: continue
        assert path.suffix.lower() not in {".pem", ".p12", ".pfx"}, f"Unexpected key file: {path}"
        if path.suffix.lower() in {".md", ".json", ".txt", ".py", ".yml", ".yaml"}:
            s = path.read_text(encoding="utf-8", errors="replace")
            assert ("-----" + "BEGIN PRIVATE KEY-----") not in s, f"Key exposed: {path}"
            assert not re.search(r"github_pat_[A-Za-z0-9_]{20,}", s), f"Token exposed: {path}"
            assert not re.search(r"gh[opsu]_[A-Za-z0-9]{20,}", s), f"Token exposed: {path}"
    print("PASS 20 original sections, provenance hashes, 46 unique lots and valid state schema")
    print("PASS elementary key/token pattern checks (not a full security audit)")

if __name__ == "__main__":
    try: verify()
    except (AssertionError, OSError, KeyError, ValueError) as error:
        print(f"FAIL {error}", file=sys.stderr)
        sys.exit(1)
