"""Validate the public contents of this Codex Skill repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "SKILL.md",
    "README.md",
    "README.zh-CN.md",
    "LICENSE",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "agents/openai.yaml",
    ".github/CONTRIBUTING.md",
    ".github/CONTRIBUTING_en.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/bug_report.md",
    ".github/ISSUE_TEMPLATE/feature_request.md",
    ".github/ISSUE_TEMPLATE/config.yml",
)
FORBIDDEN_DIRECTORIES = {"data", "node_modules", "browser-profile", ".codex"}
FORBIDDEN_FILES = {".env", ".env.local", ".env.production"}
SECRET_PATTERNS = {
    "GitHub token": re.compile(r"(?i)(?:ghp_|github_pat_|gho_|ghu_|ghs_|ghr_)[A-Za-z0-9_]+"),
    "OpenAI-style key": re.compile(r"(?i)\bsk-[A-Za-z0-9]{20,}\b"),
    "Cookie value": re.compile(
        r"(?im)\b(?:MUSIC_U|NETEASE_COOKIE)[^\S\r\n]*=[^\S\r\n]*"
        r"(?!\.{3}(?:\s|$)|<|your_|placeholder|redacted)"
        r"[^;\s`'\"<>]+"
    ),
    "private Windows path": re.compile(r"(?i)\b[A-Z]:\\Users\\[^\\\s]+"),
    "private POSIX path": re.compile(r"(?i)(?:^|[\s(`])/(?:Users|home)/[^\s`)]+"),
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate() -> list[str]:
    errors: list[str] = []

    for relative_path in REQUIRED_FILES:
        path = ROOT / relative_path
        if not path.is_file():
            errors.append(f"missing required file: {relative_path}")

    skill_path = ROOT / "SKILL.md"
    if skill_path.is_file():
        skill_text = read_text(skill_path)
        if not skill_text.startswith("---\n"):
            errors.append("SKILL.md must start with YAML frontmatter")
        if "name: netease-playlist-sync" not in skill_text:
            errors.append("SKILL.md frontmatter has the wrong skill name")
        if "[TODO:" in skill_text or "TODO:" in skill_text:
            errors.append("SKILL.md contains an unfinished TODO placeholder")

    for path in ROOT.rglob("*"):
        relative_path = path.relative_to(ROOT)
        if ".git" in relative_path.parts:
            continue
        if path.is_dir() and path.name in FORBIDDEN_DIRECTORIES:
            errors.append(f"forbidden directory present: {relative_path}")
        if path.is_file() and path.name in FORBIDDEN_FILES:
            errors.append(f"forbidden credential file present: {relative_path}")
        if not path.is_file():
            continue

        try:
            text = read_text(path)
        except UnicodeDecodeError:
            errors.append(f"non-UTF-8 text file: {relative_path}")
            continue

        for line_number, line in enumerate(text.splitlines(), 1):
            if line.rstrip() != line:
                errors.append(
                    f"trailing whitespace: {relative_path}:{line_number}"
                )
            if "\x00" in line:
                errors.append(f"NUL byte: {relative_path}:{line_number}")

        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"possible {label} in {relative_path}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Skill validation passed: {ROOT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
