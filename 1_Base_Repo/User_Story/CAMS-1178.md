CANP-3054 GL/Umbrella International Premium Allocation - table enhancements
Component: Middle Market

## User Story: CAMS-1178 - GL/Umbrella International Premium Allocation - table enhancements
As an underwriter I want the ability to enter the local premiums for each international country and separately specify any DIC/DIL amounts to add to the master policy so that the quoted and actual premiums can be automatically allocated without duplication.

Requirement Detail:
Currently there are 2 screens for entering international premiums: Update screen and International Premium Allocation (IPA) screen.

Current workflow:

Enter premium for each country in update screen, for admitted locations = local policy premium + DIC/DIL
Go to IPA screen, system brings forward premium with GL/Umbrella split
User overrides the premium split for print (but this only alters the master policy premium split and NOT the split on premium summary screen)
Add DIC/DIL for both GL and Umbrella.
Subtract DIC/DIL premium to come up with local policy premium
Convert local premiums to local currency for print
Master policy premium is calculated as (Total Program premium - Local policy premiums (in policy currency))
DIC/DIL and local policy quoted premiums are not retained once actual premium is entered
New requirement (update screen): 

On current summary showing countries make following changes:
only display the following countries:
Canada
Any countries = local policy
Any countries = Freedom of Service - Local Policy
Any Countries = Freedom of Service - Ground up
Show the insurance solution:  Canada = Master Policy, else copy the solution entered on for the receiving territory.
On Canada screen add a Master Policy table showing the summary of the solution/coverage and premium for each country as it relates to the Canada Master:
Master Coverage:
Canada = Master Policy
If Insurance Solution is "Exempt" = Master Policy
If Insurance Solution is "Non-Admitted" = Ground up
If Insurance solution = "Local Policy" = DIC/DIL
If Insurance Solution = "FinC" = Ground up
If Insurance Solution = Fos(ground up or local) - TBD of we add to this tab
Coverage type:
Blank for Canada and Exempt
For Insurance Solution Non Admitted = "Non Admitted"
Insurance Solution FinC = "Financial Interest"
For insurance solution Local Policy: Copy DIC/DIL Type (Non Admitted or Financial Interest)
For insurance Solution Fos - TBD
Include quoted/actual premiums for each row.  For DIC/DIL premium comes from newly created DIC/DIL coverages added to Canada for each country.  For ground up and FInc the premiums are blank and editable. 
4. Umbrella Simplified approach to Umbrella (see screenshot) with premium entered being considered as 100% DIC/DIL i.e. premium entered for Umbrella coverage on IPA section is 100% allocated to the master policy.

Requirements Link:

GLUmbrella International Premium Allocation - table enhancements.xlsx

Link: Product Model - CGL and Umbrella.xlsx

SL-ML-CC Code: SL-ML-CC Coverage Mapping - Final - 08 May 2025.xlsx

Acceptance Criteria:

 GIVEN: As a Policy Center user with the role of UW Agent, Underwriter or Manager 
 WHEN: Initiates a submission for GL/UMB SCOPE= PRODUCED and price the policy                                                                         THEN: The new update screen should come up for the GL/UMB policy 

 

GIVEN: As a Policy Center user with the role of UW Agent, Underwriter or Manager 
 WHEN: Initiates a submission for GL/UMB SCOPE= PRODUCED and price the policy                                                                         THEN: A new coverage (DIC/DIL - XXX, XXX = Country added as receiving territory) is available when "Local Policy" is entered as insurance solution in receiving territory (both GL and Umbrella LOBs)

GIVEN: As a Policy Center user with the role of UW Agent, Underwriter or Manager 
WHEN: Initiates a submission for GL/UMB SCOPE = PRODUCED and price the policy                                                                        THEN: The new update screen should be visible only for the new submission and shouldn't be visible only for any existing policies and the transaction performed on any existing policies until renewed. Cancellation Rewrite/Cancellation/Reinstatement should also, behave as it is.

GIVEN: As a Policy Center user with the role of UW Agent, Underwriter or Manager 
WHEN: Initiates a submission for GL/UMB, SCOPE = PRODUCED and issue the policy                                                                        THEN: There should not be any impact to BORIS and should get the data as it is

GIVEN: As a Policy Center user with the role of UW Agent, Underwriter or Manager 
WHEN: Initiates a submission for GL/UMB, SCOPE= PRODUCED and issue the policy                                                                          THEN: The new coverage (DIC/DIL) should flow to the CESAR successfully with correct ML-SL-CC Code

GIVEN: As a Policy Center user with the role of UW Agent, Underwriter or Manager 
WHEN: Initiates a submission for GL/UMB, SCOPE= PRODUCED and issues the policy                                                                        THEN: In Claim Center the new coverage (DIC/DIL) shouldn't be available for any claims.

GIVEN: As a Policy Center user with the role of UW Agent, Underwriter or Manager 

WHEN: Initiates a submission for Scope=Produced submission for Casualty (General Liability) and Umbrella AND adds Receiving territories with Insurance Solution = Local Policy & Ground Up AND Price it AND Clicks on Update Screen Table 1 row with Insurance Solution = Local Policy OR Ground Up

THEN: The below coverage section should be hidden

 