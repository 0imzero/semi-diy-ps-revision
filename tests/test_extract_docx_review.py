from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "extract_docx_review.py"
SPEC = importlib.util.spec_from_file_location("extract_docx_review", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"


DOCUMENT_XML = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="{W}">
  <w:body>
    <w:p>
      <w:r><w:t>I learned </w:t></w:r>
      <w:del w:id="1" w:author="Editor" w:date="2026-08-30T10:00:00Z"><w:r><w:delText>finance</w:delText></w:r></w:del>
      <w:ins w:id="2" w:author="Applicant" w:date="2026-08-31T10:00:00Z"><w:r><w:t>data science</w:t></w:r></w:ins>
      <w:r><w:t> through practice.</w:t></w:r>
    </w:p>
    <w:p>
      <w:commentRangeStart w:id="0"/>
      <w:r><w:t>This claim</w:t></w:r>
      <w:commentRangeEnd w:id="0"/>
      <w:r><w:commentReference w:id="0"/></w:r>
      <w:r><w:t> needs evidence.</w:t></w:r>
    </w:p>
  </w:body>
</w:document>
"""

COMMENTS_XML = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:comments xmlns:w="{W}">
  <w:comment w:id="0" w:author="Reviewer" w:date="2026-08-31T12:00:00Z">
    <w:p><w:r><w:t>Please add a concrete example.</w:t></w:r></w:p>
  </w:comment>
</w:comments>
"""


def make_docx(path: Path, *, document: str = DOCUMENT_XML, comments: str | None = COMMENTS_XML) -> None:
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("word/document.xml", document.encode("utf-8"))
        if comments is not None:
            archive.writestr("word/comments.xml", comments.encode("utf-8"))


class ExtractDocxReviewTests(unittest.TestCase):
    def test_accepted_rejected_and_all_views(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "draft.docx"
            make_docx(source)
            review = MODULE.extract_review(source)

        accepted = review["paragraphs"]["accepted"]
        rejected = review["paragraphs"]["rejected"]
        all_changes = review["paragraphs"]["all"]
        self.assertEqual(accepted[0], "I learned data science through practice.")
        self.assertEqual(rejected[0], "I learned finance through practice.")
        self.assertEqual(
            all_changes[0],
            "I learned [-finance-]{+data science+} through practice.",
        )

    def test_comments_have_metadata_and_exact_anchor(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "draft.docx"
            make_docx(source)
            comment = MODULE.extract_review(source)["comments"][0]

        self.assertEqual(comment["id"], "0")
        self.assertEqual(comment["author"], "Reviewer")
        self.assertEqual(comment["anchor"], "This claim")
        self.assertEqual(comment["text"], "Please add a concrete example.")

    def test_changes_keep_author_date_and_text(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "draft.docx"
            make_docx(source)
            changes = MODULE.extract_review(source)["changes"]

        self.assertEqual([item["kind"] for item in changes], ["deletion", "insertion"])
        self.assertEqual(changes[0]["author"], "Editor")
        self.assertEqual(changes[1]["text"], "data science")

    def test_unicode_path_json_cli_and_parent_creation(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "中文初稿.docx"
            output = Path(temp) / "Reviews" / "提取.json"
            make_docx(source)
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(source), "-o", str(output)],
                check=False,
                capture_output=True,
                text=True,
                encoding="utf-8",
            )
            payload = json.loads(output.read_text(encoding="utf-8"))

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(payload["source"].endswith("中文初稿.docx"))

    def test_markdown_output(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "draft.docx"
            output = Path(temp) / "review.md"
            make_docx(source)
            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    str(source),
                    "--format",
                    "markdown",
                    "-o",
                    str(output),
                ],
                check=False,
                capture_output=True,
                text=True,
                encoding="utf-8",
            )
            markdown = output.read_text(encoding="utf-8")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("## Accepted text", markdown)
        self.assertIn("This claim", markdown)
        self.assertIn("## Tracked changes", markdown)

    def test_invalid_archive_returns_user_facing_error(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "broken.docx"
            source.write_text("not a zip", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(source)],
                check=False,
                capture_output=True,
                text=True,
                encoding="utf-8",
            )

        self.assertEqual(result.returncode, 2)
        self.assertIn("Not a valid DOCX archive", result.stderr)


if __name__ == "__main__":
    unittest.main()

