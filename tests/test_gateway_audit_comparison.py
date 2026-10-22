"""GH-MAX-02/03: a redacted local audit is data, not authority to act."""
from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import compare_gateway_audit as diff
import reconcile_gateway_permissions as catalog


def fixture() -> dict:
    return {
        "schema_version": "1.0.0",
        "audit_utc": "2026-10-22T02:00:00Z",
        "app": {
            "id": 5417646, "owner": "chainsolutions-wealthtech",
            "permissions": {"contents": "write", "organization_actions_variables": "read"},
        },
        "installations": [
            {"account": account, "installation_id": identifier, "token_issued": True,
             "granted_permissions": {"contents": "read", "organization_actions_variables": "read"}}
            for account, identifier in diff.EXPECTED_INSTALLATIONS.items()
        ],
    }


class GatewayAuditComparisonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        spec = catalog.SPEC_PATH.read_text(encoding="utf-8")
        cls.candidates, *_ = catalog.parse_spec(spec)

    def test_comparison_requires_100_and_does_not_authorize(self) -> None:
        report = diff.comparison(fixture(), self.candidates)
        self.assertEqual(len(report["items"]), 100)
        self.assertEqual(report["historical_candidate_count"], 100)
        self.assertIs(report["github_writes_performed"], False)
        self.assertIs(report["credentials_processed_or_emitted"], False)
        self.assertTrue(all(not x["permission_probed"] and not x["agent_policy_authorized"]
                            for x in report["items"]))

    def test_installed_permissions_do_not_authorize_user_oauth(self) -> None:
        report = diff.comparison(fixture(), self.candidates)
        block = next(x for x in report["items"] if x["historical_parameter"] == "blocking")
        self.assertTrue(all(v == "USER_OAUTH_NOT_PROVEN_BY_INSTALLATION"
                            for v in block["installation_report_status"].values()))

    def test_wrong_app_rejected(self) -> None:
        obj = fixture()
        obj["app"]["id"] = 9999
        with self.assertRaises(ValueError):
            diff.comparison(obj, self.candidates)

    def test_wrong_installation_rejected(self) -> None:
        obj = fixture()
        obj["installations"][0]["installation_id"] = 0
        with self.assertRaises(ValueError):
            diff.comparison(obj, self.candidates)

    def test_credential_input_rejected(self) -> None:
        obj = fixture()
        obj["private_key"] = "not-a-real-key"
        with self.assertRaises(diff.UnsafeAudit):
            diff.comparison(obj, self.candidates)
        obj = fixture()
        obj["checks"] = {"details": {"access_token": "fake-token"}}
        with self.assertRaises(diff.UnsafeAudit):
            diff.comparison(obj, self.candidates)

    def test_bad_permission_level_rejected(self) -> None:
        obj = fixture()
        obj["app"]["permissions"]["contents"] = "superadmin"
        with self.assertRaises(ValueError):
            diff.comparison(obj, self.candidates)

    def test_duplicate_or_missing_installation_rejected(self) -> None:
        obj = fixture()
        obj["installations"].append(copy.deepcopy(obj["installations"][0]))
        with self.assertRaises(ValueError):
            diff.comparison(obj, self.candidates)
        obj["installations"].pop()
        obj["installations"].pop()
        with self.assertRaises(ValueError):
            diff.comparison(obj, self.candidates)

    def test_unreported_organization_scope_not_a_denial(self) -> None:
        obj = fixture()
        obj["installations"][1]["granted_permissions"] = {}
        result = diff.comparison(obj, self.candidates)
        cell = next(x for x in result["items"]
                    if x["historical_parameter"] == "organization_actions_variables")
        self.assertIn("NO_EXACT_PARAMETER_IN_REPORTED_INSTALLATION",
                      cell["installation_report_status"].values())


if __name__ == "__main__":
    unittest.main()
