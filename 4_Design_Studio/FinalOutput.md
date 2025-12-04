# Functional Test Cases for CAMS-2736

## Project: Designated Professional Services Exclusion Validation
**User Story:** CAMS-2736 - Ensure Consistent Application of Designated Professional Services Exclusion across General Liability and Umbrella Policies ZC 3339 and ZC 3676

> **Navigation Steps Reference:** Key steps from `1_Base_Repo/Reference/navigation_steps.md` relevant to these test cases:
- **Step 1:** Create a submission in UWD (start a quote/policy). 
- **Step 5:** Line selection (add GL/Umbrella products).
- **Step 8:** Navigate to General Liability (GL) LOB and configure fields/exclusions.
- **Step 9:** Navigate to Umbrella LOB and configure fields/exclusions.
- **Step 11:** Price the submission.
- **Step 15-16:** Create/Validate Quote and Quote Document.
- **Step 18-19:** Bind and validate Binder Document.
- **Step 20-22:** Issue policy and verify issuance/price steps.

Use the above steps as the navigation flow when executing each test case. The full navigation details are in `1_Base_Repo/Reference/navigation_steps.md`.

---

## TC ID: TC_001
**Test Type:** Manual  
**Test Case Name:** Verify automatic addition of ZC 3676 when ZC 3339 is added to GL policy with Umbrella sub-line  
**Description:** Verify that the Exclusion - Designated Professional Services ZC 3676 is automatically added as a suggested exclusion when Exclusion - Designated Professional Services ZC 3339 is added to the General Liability (GL) policy and umbrella sub-line is selected.

**Navigation Steps:** Follow steps `1`, `5`, `8`, `9` from `1_Base_Repo/Reference/navigation_steps.md`.

**Actions:**
1. Login into the system and create a new quote/policy (Step 1).
2. Navigate to line selection and ensure GL and Umbrella products are present (Step 5).
3. Navigate to GL (Step 8) and add Exclusion - Designated Professional Services ZC 3339.
4. Navigate to Umbrella (Step 9) or enable Umbrella sub-line and observe exclusions.
5. Verify if ZC 3676 is suggested or automatically added.

**Expected Results:** 
- Exclusion - Designated Professional Services ZC 3676 should be automatically added or suggested in the Umbrella sub-line when ZC 3339 is present in GL sub-line.

**Test Repository Path:** CAMS-2736  
**Status:** Todo  
**User Story:** CAMS-2736  
**Priority:** High

---

## TC ID: TC_002
**Test Type:** Manual  
**Test Case Name:** Verify manual removal of ZC 3676 from Umbrella when already selected  
**Description:** Verify that the user has the ability to manually remove the Exclusion - Designated Professional Services ZC 3676 from the Umbrella sub-line when it is already selected.

**Navigation Steps:** `1`, `5`, `9` from `1_Base_Repo/Reference/navigation_steps.md`.

**Actions:**
1. Create a new quote/policy with GL and Umbrella (Steps 1,5).
2. Ensure ZC 3676 is present in Umbrella (Step 9) — either auto-added or manually added.
3. Use the UI remove/unselect for ZC 3676 in Umbrella and confirm.
4. Verify the exclusion is removed from the Umbrella exclusions list.

**Expected Results:**
- User should be able to remove Exclusion - Designated Professional Services ZC 3676 from the Umbrella sub-line.
- The exclusion should not appear after removal.

**Test Repository Path:** CAMS-2736  
**Status:** Todo  
**User Story:** CAMS-2736  
**Priority:** High

---

## TC ID: TC_003
**Test Type:** Manual  
**Test Case Name:** Verify automatic removal of ZC 3676 when ZC 3339 is removed from GL policy  
**Description:** Verify that the Exclusion - Designated Professional Services ZC 3676 is automatically removed from the Umbrella sub-line when Exclusion - Designated Professional Services ZC 3339 is removed from the General Liability (GL) policy.

**Navigation Steps:** `1`, `5`, `8`, `9`.

**Actions:**
1. Create a quote/policy with GL and Umbrella (Steps 1,5).
2. Add ZC 3339 to GL (Step 8) and confirm ZC 3676 appears in Umbrella (Step 9).
3. Remove ZC 3339 from GL (Step 8) and refresh or navigate to Umbrella (Step 9).
4. Verify ZC 3676 is removed from Umbrella exclusions.

**Expected Results:**
- ZC 3676 should be automatically removed from the Umbrella sub-line after ZC 3339 is removed from GL.

**Test Repository Path:** CAMS-2736  
**Status:** Todo  
**User Story:** CAMS-2736  
**Priority:** High

---

## TC ID: TC_004
**Test Type:** Manual  
**Test Case Name:** Verify VAL-559 validation trigger for duplicate schedule items  
**Description:** Verify that the VAL-559 validation is triggered when there is a duplicate entry in the schedule items list between ZC 3339 in GL and ZC 3676 in Umbrella exclusions.

**Navigation Steps:** `1`, `5`, `8`, `9`, `11`.

**Actions:**
1. Create a quote/policy with GL and Umbrella (Steps 1,5).
2. Add ZC 3339 to GL with schedule items (Step 8).
3. Add ZC 3676 to Umbrella with identical schedule items (Step 9).
4. Attempt to price/validate (Step 11) and observe validation messages.

**Expected Results:**
- VAL-559 should be triggered when duplicate schedule entries exist across the two exclusions.
- Validation message should identify duplicate or conflicting schedule items.

**Test Repository Path:** CAMS-2736  
**Status:** Todo  
**User Story:** CAMS-2736  
**Priority:** High

---

## TC ID: TC_005
**Test Type:** Manual  
**Test Case Name:** Verify VAL-559 validation trigger for schedule item count mismatch  
**Description:** Verify that the VAL-559 validation is triggered when there is a mismatch in the number of schedule items between ZC 3339 in GL and ZC 3676 in Umbrella exclusions.

**Navigation Steps:** `1`, `5`, `8`, `9`, `11`.

**Actions:**
1. Create a quote/policy with GL and Umbrella (Steps 1,5).
2. Add ZC 3339 to GL with 5 schedule items (Step 8).
3. Add ZC 3676 to Umbrella with a different count, e.g., 3 items (Step 9).
4. Attempt to price/validate (Step 11).

**Expected Results:**
- VAL-559 should be triggered when schedule item counts mismatch between the two exclusions.
- Error message should indicate the mismatch and required reconciliation.

**Test Repository Path:** CAMS-2736  
**Status:** Todo  
**User Story:** CAMS-2736  
**Priority:** High

---

## TC ID: TC_006
**Test Type:** Manual  
**Test Case Name:** Verify UW-418 block when pricing with ZC 3339 in GL but without ZC 3676 in Umbrella  
**Description:** Verify that the UW-418 validation is triggered and blocks the quote when attempting to price a policy with Exclusion - Designated Professional Services ZC 3339 in GL but without Exclusion - Designated Professional Services ZC 3676 in Umbrella.

**Navigation Steps:** `1`, `5`, `8`, `11`.

**Actions:**
1. Create a quote/policy with GL and Umbrella (Steps 1,5).
2. Add ZC 3339 to GL (Step 8) and ensure ZC 3676 is NOT present in Umbrella (Step 9).
3. Attempt to price the policy (Step 11).
4. Verify whether UW-418 validation appears and blocks pricing.

**Expected Results:**
- UW-418 should be triggered and pricing should be blocked when ZC 3339 is present in GL but ZC 3676 is missing in Umbrella.

**Test Repository Path:** CAMS-2736  
**Status:** Todo  
**User Story:** CAMS-2736  
**Priority:** High

---

## TC ID: TC_007
**Test Type:** Manual  
**Test Case Name:** Verify successful pricing with both ZC 3339 and ZC 3676 without conflicts  
**Description:** Verify that the policy can be successfully priced when both Exclusion - Designated Professional Services ZC 3339 and ZC 3676 are present with matching and valid schedule items.

**Navigation Steps:** `1`, `5`, `8`, `9`, `11`.

**Actions:**
1. Create a quote/policy with GL and Umbrella (Steps 1,5).
2. Add ZC 3339 to GL with valid schedule items (Step 8).
3. Add ZC 3676 to Umbrella with matching schedule items (Step 9).
4. Price the policy (Step 11) and confirm pricing completes without VAL-559 or UW-418.

**Expected Results:**
- Policy prices successfully without triggering VAL-559 or UW-418.

**Test Repository Path:** CAMS-2736  
**Status:** Todo  
**User Story:** CAMS-2736  
**Priority:** High

---

## TC ID: TC_008
**Test Type:** Manual  
**Test Case Name:** Verify automatic ZC 3676 addition in GL-only scenario with Umbrella later  
**Description:** Verify that when adding ZC 3339 to GL without an initial Umbrella sub-line, adding Umbrella later triggers the automatic addition of ZC 3676.

**Navigation Steps:** `1`, `5`, `8`, `9`.

**Actions:**
1. Create a quote/policy with only GL (Steps 1,5,8).
2. Add ZC 3339 to GL (Step 8).
3. Later add/enable Umbrella (Step 5/9) and navigate to Umbrella exclusions.
4. Verify ZC 3676 is automatically suggested or added.

**Expected Results:**
- ZC 3676 should be automatically added or suggested in Umbrella even when Umbrella is added after GL exclusion configuration.

**Test Repository Path:** CAMS-2736  
**Status:** Todo  
**User Story:** CAMS-2736  
**Priority:** Medium

---

## TC ID: TC_009
**Test Type:** Manual  
**Test Case Name:** Verify system behavior when only ZC 3676 is added without ZC 3339  
**Description:** Verify the system behavior when Exclusion - Designated Professional Services ZC 3676 is added to Umbrella sub-line without ZC 3339 being present in GL sub-line.

**Navigation Steps:** `1`, `5`, `9`, `11`.

**Actions:**
1. Create a quote/policy with GL and Umbrella (Steps 1,5).
2. Do NOT add ZC 3339 to GL (Step 8).
3. Manually add ZC 3676 to Umbrella (Step 9).
4. Attempt to price/validate (Step 11) and observe results.

**Expected Results:**
- System should allow ZC 3676 to be added independently.
- Pricing should proceed without UW-418 since ZC 3339 is absent in GL.

**Test Repository Path:** CAMS-2736  
**Status:** Todo  
**User Story:** CAMS-2736  
**Priority:** Medium

---

## TC ID: TC_010
**Test Type:** Manual  
**Test Case Name:** Verify VAL-559 validation when reverting schedule item changes  
**Description:** Verify that VAL-559 is triggered when schedule items are modified after pricing, creating a mismatch between GL ZC 3339 and Umbrella ZC 3676 exclusions.

**Navigation Steps:** `1`, `5`, `8`, `9`, `11`.

**Actions:**
1. Create a quote/policy with GL and Umbrella (Steps 1,5).
2. Add ZC 3339 to GL and ZC 3676 to Umbrella with matching schedule items (Steps 8,9).
3. Price successfully (Step 11).
4. Modify schedule items in GL (Step 8) creating a mismatch, then attempt to re-price/validate (Step 11).
5. Verify VAL-559 is triggered.

**Expected Results:**
- VAL-559 should be triggered when schedule items are modified causing mismatch across the exclusions.

**Test Repository Path:** CAMS-2736  
**Status:** Todo  
**User Story:** CAMS-2736  
**Priority:** Medium

---

## Summary of Test Coverage

| Acceptance Criteria | Test Cases | Type |
|---|---|---|
| AC1: Auto-add ZC 3676 when ZC 3339 is added | TC_001, TC_008 | Positive |
| AC2: Ability to remove ZC 3676 | TC_002 | Positive |
| AC3: Auto-remove ZC 3676 when ZC 3339 is removed | TC_003 | Positive |
| AC4: VAL-559 trigger for duplicates/mismatch | TC_004, TC_005, TC_010 | Negative |
| AC5: UW-418 trigger for missing ZC 3676 | TC_006 | Negative |
| General Scenarios | TC_007, TC_009 | Mixed |

**Total Test Cases Generated:** 10  
**Positive Scenarios:** 5  
**Negative Scenarios:** 5  
**Coverage:** All acceptance criteria covered with comprehensive positive and negative test cases

---

## Transaction Coverage (Mandatory Scenarios)
The following transaction scenarios must be exercised for Domestic and Produced scope across the test cases above: 
- New Business
- Policy Change: Inception, Midterm, Out of Sequence, Preemption
- Cancel: Flat, Pro rata, Short rate
- Reinstatement
- Rewrite Full Term

Approach: Execute the relevant functional test (TC_001 - TC_010) within each transaction context. For clarity and traceability, the next set of concise transaction-specific test cases (TC_011–TC_020) demonstrates how to run the core acceptance checks in each mandated transaction type and scope.

## TC ID: TC_011
**Test Type:** Manual  
**Test Case Name:** AC1 Auto-add ZC 3676 — New Business (Domestic & Produced)  
**Description:** Validate TC_001 behavior (auto-add ZC 3676) when creating a New Business submission for both Domestic and Produced scope.

**Actions:**
1. Create a New Business submission in UWD (Navigation Step 1) for Domestic scope; repeat for Produced scope.
2. Select GL and Umbrella lines (Step 5).
3. Add ZC 3339 to GL (Step 8).
4. Verify ZC 3676 is suggested/added in Umbrella (Step 9).

**Expected Results:** ZC 3676 is auto-added/suggested in Umbrella for both Domestic and Produced New Business submissions.

## TC ID: TC_012
**Test Type:** Manual  
**Test Case Name:** AC1 Auto-add ZC 3676 — Policy Change (Inception)  
**Description:** Validate auto-add behavior when performing an Inception policy change.

**Actions:**
1. Open an existing policy and initiate a Policy Change (Inception).
2. Ensure GL is in scope and add ZC 3339.
3. Add/enable Umbrella and verify ZC 3676 presence.

**Expected Results:** ZC 3676 is suggested/added on Umbrella during an Inception policy change.

## TC ID: TC_013
**Test Type:** Manual  
**Test Case Name:** AC1 Auto-add ZC 3676 — Policy Change (Midterm / Out of Sequence / Preemption)  
**Description:** Validate auto-add behavior across Midterm, Out of Sequence and Preemption policy changes (run separately for each type).

**Actions:**
1. For each policy change type (Midterm, Out of Sequence, Preemption): open policy, perform the change
2. Add ZC 3339 to GL and enable Umbrella
3. Verify ZC 3676 is suggested/added

**Expected Results:** ZC 3676 is suggested/added for all listed policy change types.

## TC ID: TC_014
**Test Type:** Manual  
**Test Case Name:** AC1 Auto-add ZC 3676 — Cancel (Flat / Pro rata / Short rate)  
**Description:** Validate system behavior for cancellation transactions — ensure exclusion logic remains consistent when cancellation types are executed (test impact on coverage/exclusions where applicable).

**Actions:**
1. For each cancel type (Flat, Pro rata, Short rate): create a policy with GL and Umbrella and ZC 3339 present
2. Trigger the cancellation transaction and verify whether exclusion suggestions/records persist or are appropriately handled

**Expected Results:** Cancellation should not leave inconsistent exclusion state; where applicable, ZC 3676 presence should be consistent with business rules (no orphaned required exclusions).

## TC ID: TC_015
**Test Type:** Manual  
**Test Case Name:** AC1 Auto-add ZC 3676 — Reinstatement  
**Description:** Validate exclusion sync when reinstating a previously canceled policy containing ZC 3339.

**Actions:**
1. Cancel a policy that had ZC 3339 and ZC 3676 configured
2. Perform Reinstatement transaction
3. Verify ZC 3676 is present/consistent after reinstatement

**Expected Results:** Reinstated policy should retain consistent exclusion mapping (ZC 3676 present if ZC 3339 present).

## TC ID: TC_016
**Test Type:** Manual  
**Test Case Name:** AC1 Auto-add ZC 3676 — Rewrite Full Term  
**Description:** Validate exclusion behavior when performing a Rewrite Full Term transaction on a policy with ZC 3339.

**Actions:**
1. From an existing policy with ZC 3339, execute Rewrite Full Term
2. Ensure Umbrella is in scope and verify ZC 3676 presence post-rewrite

**Expected Results:** ZC 3676 should be present/suggested after rewrite when GL contains ZC 3339.

## TC ID: TC_017
**Test Type:** Manual  
**Test Case Name:** AC4/AC5 Validation — Pricing block and VAL-559 across transactions  
**Description:** Run TC_004/TC_005/TC_006 validations (VAL-559, UW-418) across New Business, Midterm change and Rewrite transactions to ensure validations trigger consistently.

**Actions:**
1. For each transaction type (New Business, Midterm, Rewrite): create the transaction and configure schedule items to produce duplicate/mismatch or missing ZC 3676 scenarios
2. Attempt to price and observe VAL-559 / UW-418 behavior

**Expected Results:** VAL-559 and UW-418 validations should trigger consistently across transaction types when the corresponding conditions exist.

## TC ID: TC_018
**Test Type:** Manual  
**Test Case Name:** Regression Sweep — Domestic vs Produced scope  
**Description:** For a representative subset of core tests (TC_001, TC_003, TC_006, TC_004) perform regression verification across both Domestic and Produced scopes.

**Actions:**
1. Execute the selected core tests in Domestic scope.
2. Repeat the same steps in Produced scope.
3. Compare results and note any scope-specific discrepancies.

**Expected Results:** Behavior should be consistent across Domestic and Produced scopes; differences documented as defects if found.

## Notes and Test Execution Guidance
- Where the core test steps reference price/validate actions, use Navigation Steps `11` (Price) and `15-16` (Quote/Document) as required.
- For Policy Change variants, use the appropriate transaction entry points documented in `navigation_steps.md` and the policy management UI.
- Mark each test run with the transaction type and scope in the test repository path (e.g., `CAMS-2736/NewBusiness/Domestic`).

---

If you want, I can expand any of the above transaction-specific items into full step-by-step test cases following the `Template.md` format (one file per test case) — tell me which transactions you'd like fully expanded first.

