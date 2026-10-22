#!/usr/bin/env python3
"""Read-only GH-MAX-01 comparison of historical candidates and REST heading index.

An exact label is NOT evidence of installation grants or endpoint eligibility.
No credentials, API writes, or authentication are performed.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC_PATH = ROOT / "docs/github-app/CAHIER_DES_CHARGES_COMPLET.md"
APP_ID = 5417646
HISTORICAL_TOTAL = 100
REST_HEADINGS_TOTAL = 80
TOKEN_SCHEMA_FIELD_TOTAL = 57
TOKEN_SCHEMA_SCOPES = {
    "repository": 28,
    "organization": 21,
    "account": 7,
    "enterprise": 1,
}
EXPECTED_SCOPES = {
    "repository": 41,
    "organization": 38,
    "account": 20,
    "enterprise": 1,
}
OFFICIAL_HEADINGS_SCOPES = {
    "repository": 33,
    "organization": 32,
    "account": 14,
    "enterprise": 1,
}
HIST_PATTERN = re.compile(
    r"^\| \x60(repository|organization|account|enterprise)\x60 \| "
    r"\x60([a-z0-9_]+)\x60 \| \x60(read|write)\x60 \| \x60NOT_VERIFIED\x60 \|$",
    re.MULTILINE,
)
OFFICIAL_PATTERN = re.compile(
    r"^\| (repository|organization|account|enterprise) \| ([^|\n]+?) \| "
    r"\x60NOT_PROBED_IN_CHAIN_GATEWAY\x60 \|$",
    re.MULTILINE,
)


TOKEN_FIELD_PATTERN = re.compile(
    r"^\| (repository|organization|account|enterprise) \| \x60([a-z0-9_]+)\x60 \| "
    r"\x60NOT_VERIFIED\x60 \|$",
    re.MULTILINE,
)


def normalize(label: str) -> str:
    return re.sub(r"[^a-z0-9]", "", label.casefold())


def parse_spec(spec: str) -> tuple[list[dict], list[dict], list[dict]]:
    parts = spec.split("## 9. Empreinte de l'ambition", 1)
    assert len(parts) == 2, "Missing original historic permission source"
    section9, sep, section10 = parts[1].partition("## 10. Confrontation officielle 2026")
    assert sep, "Missing separately labelled official REST reference snapshot"
    rest_section, sep2, token_section = section10.partition("## 11. Deuxième référence officielle 2026")
    assert sep2, "Missing installation-token permissions parameter schema snapshot"
    historical = [
        {"scope": m.group(1), "parameter": m.group(2), "requested_level": m.group(3)}
        for m in HIST_PATTERN.finditer(section9)
    ]
    official = [
        {"scope": m.group(1), "heading": m.group(2).strip()}
        for m in OFFICIAL_PATTERN.finditer(rest_section)
    ]
    token_fields = [
        {"scope": m.group(1), "parameter": m.group(2)}
        for m in TOKEN_FIELD_PATTERN.finditer(token_section)
    ]
    assert len(token_fields) == TOKEN_SCHEMA_FIELD_TOTAL, "Installation-token schema snapshot drift"
    for scope, count in TOKEN_SCHEMA_SCOPES.items():
        assert sum(x["scope"] == scope for x in token_fields) == count, f"Token schema scope drift: {scope}"
    assert len({(x["scope"], x["parameter"]) for x in token_fields}) == TOKEN_SCHEMA_FIELD_TOTAL
    assert len(historical) == HISTORICAL_TOTAL, "Historic 100 permission candidates changed"
    assert len(official) == REST_HEADINGS_TOTAL, "Official REST heading snapshot changed"
    for scope, count in EXPECTED_SCOPES.items():
        assert sum(x["scope"] == scope for x in historical) == count, f"Candidate count drift: {scope}"
    for scope, count in OFFICIAL_HEADINGS_SCOPES.items():
        assert sum(x["scope"] == scope for x in official) == count, f"REST heading count drift: {scope}"
    assert len({(x["scope"], x["parameter"]) for x in historical}) == HISTORICAL_TOTAL
    assert len({(x["scope"], x["heading"]) for x in official}) == REST_HEADINGS_TOTAL
    return historical, official, token_fields


def match(candidates: list[dict], headings: list[dict], token_fields: list[dict]) -> dict:
    items: list[dict] = []
    for candidate in candidates:
        scope = candidate["scope"]
        raw = candidate["parameter"]
        labels = {normalize(raw)}
        if scope in {"repository", "organization"} and raw.startswith(scope + "_"):
            labels.add(normalize(raw[len(scope) + 1:]))
        found = sorted(
            {row["heading"] for row in headings
             if row["scope"] == scope and normalize(row["heading"]) in labels}
        )
        status = ("EXACT_NORMALIZED_LABEL_IN_REST_INDEX" if len(found) == 1
                  else "MULTIPLE_REST_LABELS_REVIEW" if found
                  else "NOT_FOUND_IN_REST_INDEX_REVIEW_OTHER_APIS_OR_ALIASES")
        token_param_match = any(
            field["scope"] == scope and field["parameter"] == raw
            for field in token_fields
        )
        items.append({
            "scope": scope,
            "historical_parameter": raw,
            "historical_level": candidate["requested_level"],
            "rest_label_matches": found,
            "listed_as_token_schema_field": token_param_match,
            "rest_index_match_status": status,
            "live_app_grant": "NOT_VERIFIED",
            "live_installation_grant": "NOT_VERIFIED",
            "runtime_probe_status": "NOT_PERFORMED",
            "agent_policy_status": "NOT_AUTHORIZED_BY_THIS_REPORT",
        })
    n_match = sum(x["rest_index_match_status"] == "EXACT_NORMALIZED_LABEL_IN_REST_INDEX" for x in items)
    n_review = len(items) - n_match
    token_matches = sum(x["listed_as_token_schema_field"] for x in items)
    combined = sum(
        bool(x["rest_label_matches"]) or x["listed_as_token_schema_field"] for x in items
    )
    return {
        "schema_version": "1.0.0",
        "kind": "DOCUMENTARY_MULTI_SOURCE_PERMISSION_RECONCILIATION_NOT_RUNTIME",
        "github_app_id": APP_ID,
        "source": str(SPEC_PATH.relative_to(ROOT)),
        "reference": "https://docs.github.com/en/rest/authentication/permissions-required-for-github-apps",
        "evidence_limit": "A REST heading match never proves permission configuration, installation grants, GraphQL availability, or authorizes an operation.",
        "permissions_modified": False,
        "token_schema_reference": "https://docs.github.com/en/rest/apps/apps",
        "token_field_warning": "Listed request schema fields do not prove GitHub App installation grants or user-token eligibility.",
        "statistics": {
            "historic_candidates": len(candidates),
            "official_rest_headings": len(headings),
            "official_token_schema_fields": len(token_fields),
            "token_schema_exact_parameter_matches": token_matches,
            "combined_documented_matches": combined,
            "remaining_without_either_reference": len(items) - combined,
            "exact_normalized_label_matches": n_match,
            "review_other_api_or_alias": n_review,
        },
        "items": items,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Offline, read-only GH-MAX permission comparison")
    parser.add_argument("--json", action="store_true", help="Print per-permission report (no secrets)")
    args = parser.parse_args()
    try:
        source = SPEC_PATH.read_text(encoding="utf-8")
        candidates, headings, token_fields = parse_spec(source)
        result = match(candidates, headings, token_fields)
        if args.json:
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(json.dumps(result["statistics"], indent=2, ensure_ascii=False))
            print("NOT A GRANTS AUDIT. For GH-MAX-02/03 use local app JWT without disclosing private key.")
        return 0
    except (OSError, AssertionError, TypeError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
