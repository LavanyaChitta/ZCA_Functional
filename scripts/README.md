Generate test cases from a User Story markdown file

Files:
- `generate_testcases.py`: CLI script to parse a user story and produce a CSV of test cases.

Quick usage:

1. Run interactively (it will prompt for the user story path and output path):

```bash
python3 scripts/generate_testcases.py
```

2. Run with arguments:

```bash
python3 scripts/generate_testcases.py --user-story 1_Base_Repo/User_Story/CAMS-1863.md --output 4_Design_Studio/CAMS-1863_TestCases.csv
```

Notes and behavior:
- The script extracts the User Story ID (if present) and the Acceptance Criteria section.
- It generates one test case per acceptance criteria item and writes the CSV with the headers required by the prompt.
- If no acceptance criteria are found the script exits with a message.

If you'd like, I can run the script now against a specific user story file in the repo and produce the CSV for you. Provide the path or say "use default" and I'll pick a file.
