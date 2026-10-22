"""GH-MAX-01: label matching never grants permission."""
from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import reconcile_gateway_permissions as mod


class PermissionReconciliationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.doc = mod.SPEC_PATH.read_text(encoding="utf-8")
        cls.hist, cls.official, cls.tokens = mod.parse_spec(cls.doc)

    def test_original_totals(self) -> None:
        self.assertEqual(len(self.hist), 100)
        self.assertEqual(len(self.official), 80)
        self.assertEqual(len(self.tokens), 57)

    def test_candidates_preserved(self) -> None:
        result = mod.match(self.hist, self.official, self.tokens)
        self.assertEqual(len(result["items"]), 100)
        self.assertEqual({z["scope"] for z in result["items"]},
                         {"repository", "organization", "account", "enterprise"})

    def test_exact_labels_are_not_permissions(self) -> None:
        result = mod.match(self.hist, self.official, self.tokens)
        self.assertEqual(result["statistics"]["exact_normalized_label_matches"], 70)
        self.assertEqual(result["statistics"]["review_other_api_or_alias"], 30)
        self.assertTrue(all(item["live_app_grant"] == "NOT_VERIFIED" for item in result["items"]))
        self.assertTrue(all(item["live_installation_grant"] == "NOT_VERIFIED" for item in result["items"]))
        self.assertTrue(all(item["agent_policy_status"] == "NOT_AUTHORIZED_BY_THIS_REPORT"
                            for item in result["items"]))

    def test_second_official_source_catches_more_parameters(self) -> None:
        result = mod.match(self.hist, self.official, self.tokens)
        self.assertEqual(result["statistics"]["official_token_schema_fields"], 57)
        self.assertEqual(result["statistics"]["token_schema_exact_parameter_matches"], 48)
        self.assertEqual(result["statistics"]["combined_documented_matches"], 84)
        self.assertEqual(result["statistics"]["remaining_without_either_reference"], 16)
        self.assertTrue(all(z["live_app_grant"] == "NOT_VERIFIED" for z in result["items"]))

    def test_token_schema_missing_rejected(self) -> None:
        tick = chr(96)
        target = f"| repository | {tick}discussions{tick} | {tick}NOT_VERIFIED{tick} |"
        self.assertIn(target, self.doc)
        with self.assertRaises(AssertionError):
            mod.parse_spec(self.doc.replace(target + "\n", "", 1))

    def test_missing_rest_label_not_assumed_invalid(self) -> None:
        item = next(z for z in mod.match(self.hist, self.official, self.tokens)["items"]
                    if z["historical_parameter"] == "agent_tasks" and z["scope"] == "repository")
        self.assertEqual(item["rest_index_match_status"],
                         "NOT_FOUND_IN_REST_INDEX_REVIEW_OTHER_APIS_OR_ALIASES")

    def test_duplicate_record_rejected(self) -> None:
        tick = chr(96)
        target = f"| {tick}repository{tick} | {tick}actions{tick} | {tick}write{tick} | {tick}NOT_VERIFIED{tick} |"
        self.assertIn(target, self.doc)
        with self.assertRaises(AssertionError):
            mod.parse_spec(self.doc.replace(target + "\n", (target + "\n") * 2, 1))

    def test_missing_record_rejected(self) -> None:
        tick = chr(96)
        target = f"| {tick}repository{tick} | {tick}actions{tick} | {tick}write{tick} | {tick}NOT_VERIFIED{tick} |"
        with self.assertRaises(AssertionError):
            mod.parse_spec(self.doc.replace(target + "\n", "", 1))

    def test_missing_rest_heading_rejected(self) -> None:
        tick = chr(96)
        target = f"| repository | Actions | {tick}NOT_PROBED_IN_CHAIN_GATEWAY{tick} |"
        self.assertIn(target, self.doc)
        with self.assertRaises(AssertionError):
            mod.parse_spec(self.doc.replace(target + "\n", "", 1))

    def test_scope_not_interchanged(self) -> None:
        altered = copy.deepcopy(self.hist)
        for item in altered:
            if item["parameter"] == "actions":
                item["scope"] = "account"
                break
        result = mod.match(altered, self.official, self.tokens)
        item = next(z for z in result["items"] if z["historical_parameter"] == "actions")
        self.assertEqual(item["rest_label_matches"], [])

    def test_no_secrets_or_mutations(self) -> None:
        report = mod.match(self.hist, self.official, self.tokens)
        self.assertIs(report["permissions_modified"], False)
        self.assertNotIn("private_key", report)
        self.assertNotIn("access_token", report)


if __name__ == "__main__":
    unittest.main()
