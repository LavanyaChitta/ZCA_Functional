---
agent: 'agent'
description: Generate detailed manual test cases in CSV format for the given user story and acceptance criteria.
---
 
# Manual Test Case Generation Prompt
 
## Input Requirements
 
**User Story File Path:** Prompt user to provide the file path at runtime
- Example: `C:\Users\LAVANYA.CHITTAJALLU\copilot\OptimusCore\1_Base_Repo\User_Story\{filename}.md`

- The prompt will ask: "Please provide the User Story file path:"
 
**Template Reference:** `C:\Users\LAVANYA.CHITTAJALLU\copilot\OptimusCore\1_Base_Repo\Template\Template.md`

**Navigation Steps Reference:** `C:\Users\LAVANYA.CHITTAJALLU\copilot\OptimusCore\1_Base_Repo\Reference\navigation_steps.md`

**Output Location:** `C:\Users\LAVANYA.CHITTAJALLU\copilot\OptimusCore\4_Design_Studio\{filename}_TestCases.csv`

- The prompt will ask: "Please provide the Output Location file path:"


---
 
## Goal
 
Generate manual test cases in CSV format based on the user story provided in the input file path. Each test case should follow the template structure and application flow defined in the reference documents.
 
---
 
## Instructions
 
### 1. Read Input Files
- Prompt the user to enter the User Story file path
- Read the user story and acceptance criteria from the provided file path
- Read the template structure from `Template.md`
- Read any reference documents for application flow (if available)
 
### 2. Analyze User Story
- Identify all distinct scenarios within the user story **ONLY**
- Do not create additional scenarios beyond what is explicitly defined in the user story acceptance criteria
- Extract scenario-specific details:
  - Scenario title/name
  - Acceptance criteria
  - Preconditions (explicit or contextual)
  - Expected outcomes
  - UI elements mentioned
 
### 3. Generate Test Cases
 
For each scenario **explicitly mentioned in the user story**, generate **exactly one** test case with multiple rows (one row per action-expected result pair):
 
#### Multi-Row Structure
 
**First Row (Complete Test Case Information):**
- TC ID: Sequential number
- Test Type: Manual
- Test Case Name: Full descriptive name following format
- Description: Complete objective of the test case
- Action: First action step (numbered as "1. ")
- Expected Result: First expected result (numbered as "1. ")
- Test Repository Path: Full path to test repository
- Status: Done / In Progress / Not Started
- Components: Middle Market
- User Story: User Story ID
- Priority: High / Medium / Low
- Scenario Type: Positive / Negative
 
**Subsequent Rows (Same Test Case - Additional Steps):**
- TC ID: Same as first row
- Test Type: Leave empty or repeat
- Test Case Name: Leave empty
- Description: Leave empty
- Action: Next action step (numbered as "2. ", "3. ", etc.)
- Expected Result: Next expected result (numbered as "2. ", "3. ", etc.)
- Test Repository Path: Leave empty
- Status: Leave empty
- Components: Leave empty
- User Story: Leave empty
- Priority: Leave empty
- Scenario Type: Leave empty
 
#### Test Case Structure (Based on Template)
 
**Required Fields:**
- **TC ID:** Sequential number (1, 2, 3...)
- **Test Type:** Manual
- **Test Case Name:** {Format: TC{ID}_{Scenario name}_{LOB/Module}_{Transaction Type}_{Acceptance Criteria}}
- **Description:** {Clear description of the objective and what the test case validates}
- **Action:** {Single action step - one per row}
- **Expected Result:** {Expected result for the corresponding action - one per row}
- **Test Repository Path:** {Path to test repository}
- **Status:** Done / In Progress / Not Started
- **Components:** Middle Market
- **User Story:** {User Story ID}
- **Priority:** High / Medium / Low
- **Scenario Type:** Positive / Negative
**Navigation Requirements:**
- Only include navigation steps that are explicitly required by the user story scenarios
- If the user story mentions specific navigation (e.g., "navigate to Claims Overview tab"), include those navigation steps
- If the user story mentions creating specific data or runs, include those creation steps in the first test case only
- If the user story is focused on a specific page/feature, navigate directly to that context after login
- Do not include unnecessary setup steps that are not mentioned in the user story
 
**Setup Requirements:**
- If the user story requires creating runs or uploading data, include these steps in the first test case
- For subsequent test cases, reference the existing setup: "Use the Run created in TC1"
 
#### Validation Requirements
 
**UI Element Validation:**
- Validate all UI elements individually as per the user story (cards, textboxes, tables, toggles, buttons, dropdowns, etc.)
- Each element should have separate Input and Expected Result pairs
- Example:
  - Input: Verify the Amount field is displayed
  - Expected Result: Amount field is visible and enabled for input
  ---
 
## Output Format: CSV Structure
 
Generate test cases in CSV format with the following columns:
 
**CSV Headers:**
```
TC ID,Test Type,Test Case Name,Description,Action,Expected Result,Test Repository Path,Status,Components,User Story,Priority,Scenario Type
```
 
**CSV Format Rules:**
1. **Each Action-Expected Result pair is a separate row**
2. **First row of each test case** contains:
   - TC ID (e.g., 1, 2, 3)
   - Test Type (Manual)
   - Test Case Name (full descriptive name)
   - Description (objective of the test case)
   - Action: First Action step (numbered as "1. ")
   - Expected Result: First Expected Result (numbered as "1. ")
   - Test Repository Path
   - Status
   - Components (Middle Market)
   - User Story ID
   - Priority
   - Scenario Type
3. **Subsequent rows for the same test case** contain:
   - TC ID: Same as first row
   - Test Type: Empty
   - Test Case Name: Empty
   - Description: Empty
   - Action: Next Action step (numbered as "2. ", "3. ", etc.) - IN THE ACTION COLUMN ONLY
   - Expected Result: Next Expected Result (numbered as "2. ", "3. ", etc.) - IN THE EXPECTED RESULT COLUMN ONLY
   - Test Repository Path: Empty
   - Status: Empty
   - Components: Empty
   - User Story ID: Empty
   - Priority: Empty
   - Scenario Type: Empty
4. Escape commas within fields using double quotes
5. Escape double quotes within fields by doubling them ("")
6. Number actions sequentially (1., 2., 3., etc.)
7. Number expected results sequentially (1., 2., 3., etc.)
8. **CRITICAL:** Keep Action and Expected Result in SEPARATE columns - do NOT combine them

#### Scenario Coverage Rules
 
**Focus on Explicit Requirements:**
- Focus only on the specific functionality described in each scenario
- Do not add edge cases, boundary testing, or negative scenarios unless explicitly mentioned in the user story
- Generate **exactly one test case per scenario** as defined in the user story
- Include scope considerations (e.g., Domestic, Produced) 
- Ensure all transaction types mentioned in the user story are covered:
  - New Business
  - Policy Change (Inception, Midterm, Out of Sequence, Preemption)
  - Cancel (Flat, Pro rata & Short rate)
  - Reinstatement
  - Rewrite Full Term
- Genearte atleast 20 to 30 test cases covering all scenarios and transaction types mentioned in the user story
- The number of test cases must match exactly the number of scenarios defined in the user story
 
**No Duplicate Test Cases:**
- Do not create duplicate test cases for the same scenario
- Do not create additional scenarios beyond what is defined in the user story
- Do not include steps/validations not explicitly mentioned in the user story or acceptance criteria

 
**Example CSV Rows (Multiple rows for one test case):**
```csv
1,Manual,TC01_Verify Contractors Equipment Form ZC 6356 Display_Inland Marine_New Business_R1,The objective of this test case is to validate that the Contractors Equipment form ZC 6356 is displayed with correct version and edition date in the Inland Marine LOB for new business submissions,1. Navigate to Phoenix submission creation screen,1. User should be able to view the submission creation screen with all required fields,Inland Marine/CAMS-1863 Form Display,Done,Middle Market,CAMS-1863,High,Positive
1,,,,2. Create a Domestic submission with Inland Marine LOB,2. User should be able to create a submission successfully and proceed to line selection,,,,,,
1,,,,3. Navigate to Inland Marine screen and select Contractors Equipment Coverage,3. User should be able to view the Inland Marine screen with all mandatory fields displayed,,,,,,
1,,,,4. Verify form ZC 6356 is listed in the coverage options,4. User should verify that form ZC 6356 is available and selectable in the Contractors Equipment coverage options,,,,,,
1,,,,"5. Verify form edition date is ""03/25""","5. User should verify that the form edition date displays as ""03/25"" (March 2025 edition)",,,,,,
1,,,,6. Verify form version information is correctly displayed,6. User should verify that form version and edition date are properly displayed with correct metadata,,,,,,
2,Manual,TC02_Verify Form ZC 6356 Auto-Attachment on Selection_Inland Marine_New Business_R2,The objective of this test case is to validate that the Contractors Equipment form ZC 6356 is automatically attached to the document when user selects the coverage,1. Navigate to Phoenix submission creation screen,1. User should be able to view the submission creation screen,Inland Marine/CAMS-1863 Form Attachment,Done,Middle Market,CAMS-1863,High,Positive
2,,,,2. Create a Domestic submission with Inland Marine LOB,2. User should be able to create a submission successfully,,,,,,
2,,,,3. Navigate to Inland Marine screen and select Contractors Equipment Coverage,3. User should be able to view the Inland Marine screen,,,,,,
2,,,,4. Select form ZC 6356 from coverage options,4. Form ZC 6356 should be automatically added to the documents section,,,,,,
2,,,,5. Navigate to documents section,5. User should be able to view the documents section with attached forms,,,,,,
2,,,,6. Verify that form ZC 6356 is attached with latest version,6. User should verify that the attached form is the latest 03/25 edition and not the old version,,,,,,
2,,,,7. Verify form versioning information,7. User should verify that form metadata displays correct version and edition date information,,,,,,
3,Manual,TC03_Verify Form ZC 6356 Latest Edition in Payload_Inland Marine_New Business_R1,The objective of this test case is to validate that the latest 03/25 edition form ZC 6356 is sent in the payload to the backend system,1. Navigate to Phoenix submission creation screen,1. User should be able to view the submission creation screen,Inland Marine/CAMS-1863 Form Payload,Done,Middle Market,CAMS-1863,High,Positive
3,,,,2. Create a Domestic submission with Inland Marine LOB,2. User should be able to create a submission successfully,,,,,,
3,,,,3. Navigate to Inland Marine screen and select Contractors Equipment Coverage,3. User should be able to view the Inland Marine screen with all fields,,,,,,
3,,,,4. Select form ZC 6356 from coverage options,4. Form ZC 6356 should be selected,,,,,,
3,,,,"5. Verify the edition date in system payload is ""03/25""","5. System should send the form with edition date ""03/25"" in the API payload",,,,,,
3,,,,6. Verify form metadata in payload,6. The payload should include correct form versioning information and metadata,,,,,,
```
 
---
**CSV Formatting:**
- Ensure proper escaping of special characters
- Use double quotes for fields containing commas
- Use || as step separator and | as input/expected separator
- Keep formatting consistent across all test cases
 
---
 
## Example Test Case Generation
 
**Given User Story:**
```
User Story: As a customer, I want to subscribe to a UT fund by entering my investment details
 
Acceptance Criteria:
1. Minimum investment amount is displayed
2. Amount validation prevents entry below minimum
3. Sales charge and tax information is displayed
```
 
**Generated CSV Output:**
```csv
TC ID,Test Type,Test Case Name,Description,Action,Expected Result,Test Repository Path,Status,Components,User Story,Priority,Scenario Type
1,Manual,"TC01_Verify Minimum Investment Display_UT Fund Subscription_New Business_AC1","The objective of this test case is to validate that the minimum investment amount is displayed correctly and retrieved from WIS product management system","1. Navigate to UT fund subscription page","1. User should be able to view the UT fund subscription page with all required fields displayed","UT Fund/STORY-123 Minimum Investment",Done,UT Fund Subscription,STORY-123,High,Positive
1,,,"2. Verify minimum investment message below amount field","2. User should see ""Min 500 SGD"" message displayed below the amount field",,,,,,
1,,,"3. Verify source of minimum amount","3. User should verify minimum amount is retrieved from WIS system",,,,,,
```
---
 
## Execution Command
 
When ready to generate test cases, the system will:
1. Prompt user for input file path
2. Read and analyze the user story
3. Generate test cases following the template
4. Save as CSV in the specified location
5. Display confirmation with file path and test case count
 
---