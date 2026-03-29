from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
ASSET_DIR = ROOT / "abi.d"


class SiteFileTests(unittest.TestCase):
    def test_expected_files_exist(self) -> None:
        expected_files = ["index.html", "style.css", "script.js"]
        for filename in expected_files:
            self.assertTrue((ASSET_DIR / filename).is_file(), f"Missing {filename}")

    def test_index_has_core_metadata(self) -> None:
        html = (ASSET_DIR / "index.html").read_text(encoding="utf-8")
        self.assertIn("abi.d - Portfolio", html)
        self.assertIn("style.css", html)


if __name__ == "__main__":
    unittest.main()
