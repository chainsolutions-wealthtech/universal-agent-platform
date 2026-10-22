#!/usr/bin/env python3
"""Read-only comparison of a redacted local ChainSolutions Gateway audit against V5.

Input is an untrusted user-provided report. This tool NEVER authenticates to GitHub,
writes permissions, persists reports, or treats the report as independent runtime proof.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

import reconcile_gateway_permissions as catalog

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_APP = 5417646
EXPECTED_OWNER = "chainsolutions-wealthtech"
EXPECTED_INSTALLATIONS = {
    "chainsolutions-wealthtech": 173915815,
    "Patricked-code": 173916438,
    "Wealthtechinnovations": 173916302,
}
VALID_LEVELS = {"read", "write", "admin"}
FORBIDDEN_FIELDS = {
    "token", "accesstoken", "refreshtoken", "jwttoken", "jwt",
    "privatekey", "privatekeypem", "clientsecret", "webhooksecret",
    "password", "authorization", "pem", "githubtoken",
}


class UnsafeAudit(ValueError):
    pass


def reject_credentials(value: object) -> None:
    """Fail closed for credential-bearing JSON fields anywhere in the input."""
    if isinstance(value, dict):
        for raw_key, child in value.items():
            name = "".join(ch for ch in str(raw_key).casefold() if ch.isalnum())
            if name in FORBIDDEN_FIELDS or name.endswith(("accesstoken", "refreshtoken", "privatekey", "clientsecret", "webhooksecret")):
                raise UnsafeAudit("Credential-bearing input rejected (do not share raw secrets)")
            reject_credentials(child)
    elif isinstance(value, list):
        for child in value:
            reject_credentials(child)


def require_level(value: object) -> str:
    if isinstance(value, str) and value in VALID_LEVELS:
        return value
    raise ValueError("Unexpected permission level in local audit")


def comparison(raw: dict, candidates: list[dict]) -> dict:
    reject_credentials(raw)
    if raw.get("schema_version") != "1.0.0":
        raise ValueError("Unsupported local audit schema")
    if raw.get("mode") not in (None, "READ_ONLY_WITH_EPHEMERAL_TOKEN_ISSUANCE"):
        raise ValueError("Audit mode differs from expected read-only collection")
    app = raw.get("app")
    if not isinstance(app, dict) or app.get("id") != EXPECTED_APP or app.get("owner") != EXPECTED_OWNER:
        raise ValueError("Wrong GitHub App identity: abort, do not compare")
    perms = app.get("permissions")
    if not isinstance(perms, dict):
        raise ValueError("Missing GET /app permissions: cannot make grant claims")
    installations = raw.get("installations")
    if not isinstance(installations, list):
        raise ValueError("Missing installation audit records")
    by_account: dict[str, dict] = {}
    for item in installations:
        if not isinstance(item, dict) or not isinstance(item.get("account"), str):
            raise ValueError("Malformed installation record")
        account = item["account"]
        if account in by_account:
            raise ValueError("Duplicate installation: refuse comparison")
        by_account[account] = item
    if set(by_account) != set(EXPECTED_INSTALLATIONS):
        raise ValueError("Missing/extra installation: reconcile before comparison")
    for account, expected_id in EXPECTED_INSTALLATIONS.items():
        if by_account[account].get("installation_id") != expected_id:
            raise ValueError("Installation ID mismatch: refuse comparison")

    if len(candidates) != 100 or len({(r.get("scope"), r.get("parameter")) for r in candidates}) != 100:
        raise ValueError("Untrusted candidate registry or missing historical permissions")
    lines = []
    for row in candidates:
        scope, name = row["scope"], row["parameter"]
        app_level = perms.get(name)
        if app_level is not None:
            app_level = require_level(app_level)
        entries = {}
        for account, item in by_account.items():
            if scope == "account":
                entries[account] = "USER_OAUTH_NOT_PROVEN_BY_INSTALLATION"
                continue
            if scope == "enterprise":
                entries[account] = "ENTERPRISE_INSTALLATION_ELIGIBILITY_NOT_PROVEN"
                continue
            granted = item.get("granted_permissions")
            if item.get("token_issued") is not True or not isinstance(granted, dict):
                entries[account] = "INSTALLATION_GRANTS_UNAVAILABLE"
            elif name in granted:
                entries[account] = "REPORTED_" + require_level(granted[name]).upper()
            else:
                entries[account] = "NO_EXACT_PARAMETER_IN_REPORTED_INSTALLATION"
        lines.append({
            "scope": scope,
            "historical_parameter": name,
            "historical_requested_level": row["requested_level"],
            "reported_app_setting": app_level or "NO_EXACT_PARAMETER_IN_REPORTED_APP",
            "installation_report_status": entries,
            "permission_probed": False,
            "agent_policy_authorized": False,
        })
    return {
        "kind": "UNTRUSTED_LOCAL_REPORT_COMPARISON_NON_EXECUTABLE",
        "app_id": EXPECTED_APP,
        "audit_timestamp_reported": str(raw.get("audit_utc") or "UNKNOWN"),
        "trust_note": "Self-reported redacted snapshot only. Confirm freshness, true app identity, consent and endpoint probes before asserting granted capability.",
        "credentials_processed_or_emitted": False,
        "github_writes_performed": False,
        "historical_candidate_count": len(lines),
        "permission_report_level_count": dict(sorted(Counter(
            x["reported_app_setting"] for x in lines
        ).items())),
        "installations_compared": sorted(by_account),
        "items": lines,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Offline GitHub App grants report comparator")
    parser.add_argument("--audit", required=True, type=Path, help="Redacted JSON from local GA-00 audit")
    parser.add_argument("--json", action="store_true", help="Show safe per-permission comparison")
    args = parser.parse_args()
    try:
        data = json.loads(args.audit.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("Expected JSON object")
        hist, _, _, _, _ = catalog.parse_spec(catalog.SPEC_PATH.read_text(encoding="utf-8"))
        result = comparison(data, hist)
        if args.json:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            print(json.dumps({k: result[k] for k in (
                "kind", "app_id", "audit_timestamp_reported", "historical_candidate_count",
                "permission_report_level_count", "installations_compared", "trust_note"
            )}, ensure_ascii=False, indent=2))
            print("NO_GITHUB_WRITES / NO_SECRET_OUTPUT / NO_RUNTIME_ATTESTATION")
        return 0
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print("REFUSED: " + str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
