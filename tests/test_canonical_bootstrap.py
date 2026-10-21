"""Negative regression tests for canonical source and public-repository security gates."""
from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import validate_canonical_bootstrap as gate


class SecurityGateTests(unittest.TestCase):
    def assert_rejected(self, relative: str, contents: str) -> None:
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(contents, encoding="utf-8")
            with self.assertRaises(AssertionError):
                gate.check_tree_security(root)

    def test_all_standard_private_key_headers_rejected(self) -> None:
        for label in ("", "RSA ", "EC ", "DSA ", "OPENSSH ", "ENCRYPTED "):
            with self.subTest(header=label):
                fixture = "-----" + "BEGIN " + label + "PRIVATE KEY-----"
                self.assert_rejected("disguised.md", fixture + "\nredacted\n")

    def test_pgp_private_key_block_rejected(self) -> None:
        fixture = "-----" + "BEGIN PGP PRIVATE KEY BLOCK-----"
        self.assert_rejected("disguised.txt", fixture + "\nredacted\n")

    def test_key_extension_is_rejected_even_without_header(self) -> None:
        for name in ("id_rsa.key", "id_rsa.pem", "certificate.p12", "encrypted.p8", ".env.production"):
            with self.subTest(name=name):
                self.assert_rejected(name, "placeholder only\n")

    def test_github_token_pattern_rejected(self) -> None:
        fixture = "ghp_" + "A" * 25
        self.assert_rejected("notes.txt", fixture)

    def test_all_app_and_refresh_token_formats_rejected(self) -> None:
        for prefix in ("ghp_", "gho_", "ghu_", "ghs_", "ghr_", "github_pat_"):
            with self.subTest(prefix=prefix):
                self.assert_rejected("neutral.txt", prefix + ("ABC_DEF01234567890" * 2))

    def test_tracked_like_pycache_paths_are_not_exempted(self) -> None:
        fixture = "-----" + "BEGIN RSA PRIVATE KEY-----"
        self.assert_rejected("pkg/__pycache__/id.key", fixture)
        self.assert_rejected("pkg/__pycache__/leak.txt", "ghr_" + "A" * 25)

    def test_benign_file_accepted(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            (Path(folder) / "notes.md").write_text("benign documentation", encoding="utf-8")
            gate.check_tree_security(Path(folder))


class SourceIntegrityTests(unittest.TestCase):
    def test_canonical_manifest_missing_source_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            archive = Path(folder) / "docs/archive"
            archive.mkdir(parents=True)
            data = {"sources": [{"path": gate.ORIGINAL, "sha256": "placeholder", "bytes": 0}]}
            (archive / "IMPORT_MANIFEST.json").write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaises(AssertionError):
                gate.verify_manifest(Path(folder))

    def test_canonical_manifest_duplicate_source_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            archive = Path(folder) / "docs/archive"
            archive.mkdir(parents=True)
            record = {"path": gate.ORIGINAL, "sha256": "placeholder", "bytes": 0}
            (archive / "IMPORT_MANIFEST.json").write_text(json.dumps({"sources": [record, record, record]}))
            with self.assertRaises(AssertionError):
                gate.verify_manifest(Path(folder))

    def test_indexes_match_master_annexes(self) -> None:
        plan = (ROOT / gate.MASTER).read_text(encoding="utf-8")
        mapping = json.loads((ROOT / "docs/roadmap/MAPPING_20_SECTIONS_V5.json").read_text(encoding="utf-8"))
        catalog = json.loads((ROOT / "docs/roadmap/CATALOGUE_30_DOMAINES_V5.json").read_text(encoding="utf-8"))
        gate.verify_indexes(plan, mapping, catalog)

    def test_missing_mapping_content_rejected(self) -> None:
        plan = (ROOT / gate.MASTER).read_text(encoding="utf-8")
        mapping = json.loads((ROOT / "docs/roadmap/MAPPING_20_SECTIONS_V5.json").read_text(encoding="utf-8"))
        catalog = json.loads((ROOT / "docs/roadmap/CATALOGUE_30_DOMAINES_V5.json").read_text(encoding="utf-8"))
        bad = copy.deepcopy(mapping)
        del bad["items"][0]["source_title"]
        with self.assertRaises(AssertionError):
            gate.verify_indexes(plan, bad, catalog)

    def test_corrupted_domain_rejected(self) -> None:
        plan = (ROOT / gate.MASTER).read_text(encoding="utf-8")
        mapping = json.loads((ROOT / "docs/roadmap/MAPPING_20_SECTIONS_V5.json").read_text(encoding="utf-8"))
        catalog = json.loads((ROOT / "docs/roadmap/CATALOGUE_30_DOMAINES_V5.json").read_text(encoding="utf-8"))
        bad = copy.deepcopy(catalog)
        bad["domains"][0]["domain"] = "wrong"
        with self.assertRaises(AssertionError):
            gate.verify_indexes(plan, mapping, bad)


if __name__ == "__main__":
    unittest.main()
