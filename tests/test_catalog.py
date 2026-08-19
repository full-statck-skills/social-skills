import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
MANIFEST = ROOT / ".claude-plugin" / "plugin.json"
NAME_PATTERN = re.compile(r"^name:\s*([a-z0-9]+(?:-[a-z0-9]+)*)\s*$", re.MULTILINE)


def skill_name(skill_file: Path) -> str:
    """Return a valid name from a SKILL.md frontmatter block."""
    contents = skill_file.read_text(encoding="utf-8")
    if not contents.startswith("---\n"):
        raise ValueError(f"{skill_file} has no YAML frontmatter")
    frontmatter = contents.split("---\n", 2)[1]
    match = NAME_PATTERN.search(frontmatter)
    if match is None:
        raise ValueError(f"{skill_file} has no valid kebab-case name")
    return match.group(1)


class CatalogTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        cls.declared = {
            (ROOT / entry).resolve().relative_to(SKILLS_ROOT.resolve()).as_posix()
            for entry in cls.manifest["skills"]
        }
        cls.directories = {path.name for path in SKILLS_ROOT.iterdir() if path.is_dir()}

    def test_manifest_matches_skill_directories(self) -> None:
        self.assertEqual(self.declared, self.directories)

    def test_skill_names_match_directories(self) -> None:
        for directory in sorted(self.directories):
            with self.subTest(directory=directory):
                self.assertEqual(skill_name(SKILLS_ROOT / directory / "SKILL.md"), directory)

    def test_readmes_list_every_skill_and_count(self) -> None:
        for filename in ("README.md", "README.zh-CN.md"):
            contents = (ROOT / filename).read_text(encoding="utf-8")
            with self.subTest(filename=filename):
                self.assertIn(f"({len(self.directories)})", contents)
                for directory in self.directories:
                    self.assertIn(f"`{directory}`", contents)

    def test_manifest_has_semantic_version(self) -> None:
        self.assertRegex(self.manifest["version"], r"^\d+\.\d+\.\d+$")


if __name__ == "__main__":
    unittest.main()
