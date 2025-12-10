#!/usr/bin/env python3
"""
Generate manual test cases CSV from a User Story markdown file.

Follows the rules described in `3_Prompt_config/Testcase.prompt.md` in this workspace.

Usage:
  python3 scripts/generate_testcases.py --user-story <path> --output <path>
If arguments are omitted the script will prompt for them interactively.

This script:
- Reads the user story file and extracts the User Story ID and Acceptance Criteria
- Generates exactly one test case per acceptance criteria item
- Writes a CSV with the required headers and one or more rows per test case

Note: The generator uses reasonable defaults when LOB/module info isn't available.
"""
import argparse
import csv
import os
import re
import sys
from pathlib import Path


def extract_user_story_id(text: str):
    # Try to find common patterns like 'User Story: CAMS-1863' or 'CAMS-1863'
    m = re.search(r"User Story\s*[:\-]?\s*([A-Za-z0-9_-]+)", text, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    # fallback: any STORY-like token
    m = re.search(r"([A-Z]{2,}-\d{1,6})", text)
    if m:
        return m.group(1)
    # fallback to filename
    return None


def extract_acceptance_criteria(text: str):
    # Robustly collect acceptance criteria or requirement lines.
    # Accept formats like:
    # - R1) ...
    # - 1. ...
    # - - bullet
    acs = []
    lines = text.splitlines()

    for i, line in enumerate(lines):
        # Match patterns like 'R1) text' or 'R 1) text' or '1) text' or '1. text'
        m = re.match(r"^\s*(?:R\s*)?(\d+)[\)\.]\s*(.*)", line, re.IGNORECASE)
        if m:
            content = m.group(2).strip()
            # If the content is short or looks like a header (ends with comma),
            # capture subsequent non-empty lines until a blank line or next numbered item.
            if not content or content.endswith(",") or len(content.split()) < 4:
                parts = [content] if content else []
                j = i + 1
                while j < len(lines):
                    nxt = lines[j].strip()
                    if not nxt:
                        break
                    if re.match(r"^\s*(?:R\s*)?\d+[\)\.]", nxt):
                        break
                    if re.match(r"^#{1,6}\s+", nxt):
                        break
                    parts.append(nxt)
                    j += 1
                full = " ".join([p for p in parts if p]).strip()
                if full:
                    acs.append(full)
                continue
            else:
                acs.append(content)
                continue

        # Match bullet lists '- item' or '* item'
        m2 = re.match(r"^\s*[-*]\s*(.*)", line)
        if m2 and m2.group(1).strip():
            acs.append(m2.group(1).strip())
            continue

    # If nothing found yet, as a last resort pick up any numbered '1. ' style lines
    if not acs:
        for line in lines:
            m3 = re.match(r"^\s*\d+\.\s*(.*)", line)
            if m3 and m3.group(1).strip():
                acs.append(m3.group(1).strip())

    # Clean duplicates and trim leading numbering like '1)' or '(1)'
    cleaned = []
    for a in acs:
        a2 = re.sub(r"^\d+\)|^\(\d+\)|^\d+\.|^R\s*\d+\)", "", a, flags=re.IGNORECASE).strip()
        if a2 and a2 not in cleaned:
            cleaned.append(a2)
    return cleaned


def short_name_from_text(text: str, max_words=6):
    # Create a short identifier from the acceptance criteria
    text = re.sub(r"[^A-Za-z0-9 ]+", " ", text)
    words = [w for w in text.split() if w]
    if not words:
        return "Scenario"
    return "_".join(words[:max_words])


def generate_testcases(user_story_path: Path, output_path: Path, template_path: Path = None, repo_path: Path = None):
    text = user_story_path.read_text(encoding="utf-8")
    us_id = extract_user_story_id(text) or user_story_path.stem
    acs = extract_acceptance_criteria(text)
    if not acs:
        print("No acceptance criteria found in the provided user story. Aborting.")
        return 0

    # CSV header
    headers = [
        "TC ID",
        "Test Type",
        "Test Case Name",
        "Description",
        "Action",
        "Expected Result",
        "Test Repository Path",
        "Status",
        "Components",
        "User Story",
        "Priority",
        "Scenario Type",
    ]

    rows = []
    repo_ref = str(repo_path) if repo_path else "1_Base_Repo"
    components = "Middle Market"

    for idx, ac in enumerate(acs, start=1):
        tc_id = idx
        short = short_name_from_text(ac)
        tc_name = f"TC{tc_id:02d}_Verify_{short}_General_NewBusiness_AC{tc_id}"
        description = f"Validate acceptance criteria: {ac}"
        # First action/expected pair
        action1 = f"1. Validate: {ac}"
        expected1 = f"1. System behavior should satisfy: {ac}"

        row1 = [
            str(tc_id),
            "Manual",
            tc_name,
            description,
            action1,
            expected1,
            repo_ref,
            "Not Started",
            components,
            us_id,
            "High",
            "Positive",
        ]
        rows.append(row1)

        # Optionally, if the AC mentions UI elements (heuristic), add extra steps
        # simple heuristic: look for words like 'display', 'visible', 'button', 'tab', 'dropdown', 'field'
        ui_keywords = ["display", "visible", "button", "tab", "dropdown", "field", "table", "textbox", "toggle", "card", "grid"]
        extra_index = 2
        lowered = ac.lower()
        for kw in ui_keywords:
            if kw in lowered:
                action = f"{extra_index}. Verify UI element: {kw} referenced in AC"
                expected = f"{extra_index}. {kw.capitalize()} should be present and behave as described"
                rows.append([str(tc_id), "", "", "", action, expected, "", "", "", "", "", ""]) 
                extra_index += 1

    # Write CSV
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(headers)
        for r in rows:
            writer.writerow(r)

    print(f"Generated {len(acs)} test case(s) and wrote CSV to: {output_path}")
    return len(acs)


def main():
    parser = argparse.ArgumentParser(description="Generate manual test cases CSV from a User Story markdown file.")
    parser.add_argument("--user-story", "-u", help="Path to the User Story markdown file")
    parser.add_argument("--output", "-o", help="Output CSV path")
    parser.add_argument("--template", "-t", help="Optional template reference path", default="1_Base_Repo/Template/Template.md")
    parser.add_argument("--repo-path", "-r", help="Test repository path to include in CSV", default="1_Base_Repo")
    args = parser.parse_args()

    if not args.user_story:
        args.user_story = input("Please provide the User Story file path: ").strip()
    if not args.output:
        default_out = os.path.join("4_Design_Studio", f"{Path(args.user_story).stem}_TestCases.csv")
        resp = input(f"Please provide the Output Location file path (default: {default_out}): ").strip()
        args.output = resp or default_out

    user_story_path = Path(args.user_story)
    output_path = Path(args.output)
    template_path = Path(args.template) if args.template else None
    repo_path = Path(args.repo_path) if args.repo_path else None

    if not user_story_path.exists():
        print(f"User story file does not exist: {user_story_path}")
        sys.exit(2)

    count = generate_testcases(user_story_path, output_path, template_path, repo_path)
    if count == 0:
        sys.exit(3)


if __name__ == "__main__":
    main()
