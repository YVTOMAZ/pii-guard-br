"""O pacote desktop e a extensão do Claude Desktop devem declarar a mesma versão."""
import json
import re
import unittest
from pathlib import Path

DESKTOP = Path(__file__).resolve().parent.parent / "desktop"
SEMVER = re.compile(r"\d+\.\d+\.\d+")


def pyproject_version() -> str:
    text = (DESKTOP / "pyproject.toml").read_text(encoding="utf-8")
    project = re.search(r"^\[project\]\s*$(.*?)(?=^\[|\Z)", text, re.M | re.S)
    assert project, "tabela [project] ausente"
    found = re.search(r'^version\s*=\s*"([^"]+)"', project.group(1), re.M)
    assert found, "version ausente em [project]"
    return found.group(1)


def manifest_version() -> str:
    return json.loads((DESKTOP / "manifest.json").read_text(encoding="utf-8"))["version"]


class VersionsTest(unittest.TestCase):
    def test_versions_match(self):
        self.assertEqual(pyproject_version(), manifest_version())

    def test_versions_are_semver(self):
        for value in (pyproject_version(), manifest_version()):
            self.assertRegex(value, SEMVER)


if __name__ == "__main__":
    unittest.main()
