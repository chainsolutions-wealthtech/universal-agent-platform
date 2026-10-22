"""Safeguards against executing a documentary GH-MAX plan without authorization."""
from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import check_gateway_execution_plan as gateway


class GatewayExecutionPlanTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.plan = json.loads((ROOT / gateway.MANIFEST).read_text(encoding="utf-8"))
        cls.source = (ROOT / gateway.SOURCE).read_text(encoding="utf-8")

    def test_ten_tasks_and_safe_initial_candidates(self) -> None:
        tasks = gateway.validate(self.plan, self.source)
        self.assertEqual(len(tasks), 10)
        self.assertEqual(gateway.preview(tasks, set()), ["GH-MAX-01", "GH-MAX-02"])
        self.assertEqual(gateway.preview(tasks, {"GH-MAX-01", "GH-MAX-02"}), ["GH-MAX-03"])

    def test_runtime_enabled_rejected(self) -> None:
        altered = copy.deepcopy(self.plan)
        altered["execution_enabled"] = True
        with self.assertRaises(AssertionError):
            gateway.validate(altered, self.source)

    def test_implicit_mutations_rejected(self) -> None:
        altered = copy.deepcopy(self.plan)
        altered["mutations_enabled"] = True
        with self.assertRaises(AssertionError):
            gateway.validate(altered, self.source)

    def test_unapproved_sensitive_write_rejected(self) -> None:
        altered = copy.deepcopy(self.plan)
        task = altered["tasks"][5]
        task["mutating_actions_authorized"] = True
        with self.assertRaises(AssertionError):
            gateway.validate(altered, self.source)

    def test_dependency_cycle_or_forward_reference_rejected(self) -> None:
        altered = copy.deepcopy(self.plan)
        altered["tasks"][0]["depends_on"] = ["GH-MAX-10"]
        with self.assertRaises(AssertionError):
            gateway.validate(altered, self.source)

    def test_missing_evidence_contract_rejected(self) -> None:
        altered = copy.deepcopy(self.plan)
        altered["evidence_contract"]["proof_refs_required_for_done"] = False
        with self.assertRaises(AssertionError):
            gateway.validate(altered, self.source)

    def test_task_specification_cannot_diverge_from_document_owner(self) -> None:
        altered = self.source.replace("`GH-MAX-04`", "`GH-MAX-99`", 1)
        with self.assertRaises(AssertionError):
            gateway.validate(self.plan, altered)

    def test_unknown_task_simulation_rejected(self) -> None:
        with self.assertRaises(ValueError):
            gateway.preview(self.plan["tasks"], {"GH-MAX-99"})


if __name__ == "__main__":
    unittest.main()
