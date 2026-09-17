from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = (ROOT / "SKILL.md").read_text(encoding="utf-8")
README = (ROOT / "README.md").read_text(encoding="utf-8")


class V9ContractTests(unittest.TestCase):
    def test_skill_declares_v9(self):
        self.assertIn('version: "9.0.0"', SKILL)
        self.assertIn("Human Social Designer — v9", SKILL)

    def test_original_requests_diverge_before_selection(self):
        self.assertRegex(SKILL, r"(?is)three.*concept candidates")
        self.assertRegex(SKILL, r"(?is)candidate.*different.*mechanism")

    def test_generic_result_forces_concept_change(self):
        self.assertRegex(SKILL, r"(?is)generic.*abandon.*concept")
        self.assertRegex(SKILL, r"(?is)retry once")

    def test_style_dna_and_prompt_compiler_are_required_resources(self):
        self.assertIn("references/style-dna.md", SKILL)
        self.assertIn("references/prompt-compiler.md", SKILL)
        self.assertTrue((ROOT / "references" / "style-dna.md").is_file())
        self.assertTrue((ROOT / "references" / "prompt-compiler.md").is_file())

    def test_prompt_compiler_orders_meaning_before_rendering(self):
        compiler = (ROOT / "references" / "prompt-compiler.md").read_text(encoding="utf-8")
        message = compiler.index("Message")
        metaphor = compiler.index("Metaphor")
        style = compiler.index("Style DNA")
        self.assertLess(message, metaphor)
        self.assertLess(metaphor, style)

    def test_sources_and_license_boundaries_are_documented(self):
        sources = (ROOT / "references" / "influences-and-licenses.md").read_text(encoding="utf-8")
        self.assertIn("story-picture", sources)
        self.assertIn("art-direct-imagegen-plugin", sources)
        self.assertIn("PromptEnhancer", sources)
        self.assertRegex(sources, r"(?is)no.*weights.*code.*copied")

    def test_readme_documents_v9_pipeline(self):
        self.assertIn("Version 9", README)
        for stage in ("Extract", "Diverge", "Select", "Compile", "Generate", "Inspect"):
            self.assertIn(stage, README)


if __name__ == "__main__":
    unittest.main()
