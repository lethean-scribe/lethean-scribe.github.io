---
draft: true # ← Will not appear in published site
---

## Step 7: Data Extraction

### Data Extraction Workflow

```
┌──────────────────────────────────────────────────────────────┐
│            COMPREHENSIVE DATA EXTRACTION PROCESS              │
└──────────────────────────────────────────────────────────────┘

PHASE 1: FORM DEVELOPMENT (Week 1)
│
├─ Day 1-2: Design Extraction Form
│  ├─ List all required variables
│  │  ├─ Study identifiers
│  │  ├─ Study characteristics
│  │  ├─ Participant characteristics
│  │  ├─ Intervention details
│  │  ├─ Outcome data
│  │  └─ Quality/bias indicators
│  │
│  ├─ Choose Format
│  │  ├─ Excel/Google Sheets
│  │  ├─ Covidence extraction
│  │  ├─ DistillerSR forms
│  │  └─ REDCap database
│  │
│  └─ Create Instructions
│     ├─ Define each variable
│     ├─ Coding guidelines
│     ├─ Examples for each field
│     └─ Decision rules for ambiguity
│
├─ Day 3: Peer Review Form
│  ├─ Team reviews form
│  ├─ Content expert reviews
│  ├─ Statistician reviews (outcome data)
│  └─ Incorporate feedback
│
└─ Day 4-5: Pilot Test
   ├─ Select 5 diverse studies
   ├─ Both extractors extract independently
   ├─ Time the process
   ├─ Compare results
   ├─ Identify issues
   │  ├─ Missing variables?
   │  ├─ Unclear instructions?
   │  ├─ Ambiguous coding?
   │  └─ Data not in papers?
   │
   └─ Refine form and retest

PHASE 2: TEAM TRAINING (Week 2)
│
├─ Training Session 1: Form Overview
│  ├─ Review each variable
│  ├─ Explain coding schemes
│  ├─ Discuss common issues
│  └─ Q&A session
│
├─ Training Session 2: Practice Extraction
│  ├─ Work through example study
│  ├─ Extract data together
│  ├─ Discuss challenging decisions
│  └─ Compare results
│
├─ Independent Practice
│  ├─ Each extractor does 3 studies
│  ├─ Compare with "gold standard"
│  ├─ Discuss discrepancies
│  └─ Clarify any confusion
│
└─ Finalize Procedures
   ├─ Document decision rules
   ├─ Create FAQ document
   ├─ Establish contact protocol
   └─ Set quality checks

PHASE 3: DATA EXTRACTION (Week 3-10)
│
├─ Extraction Process
│  │
│  For each study:
│  │
│  ├─ STEP 1: Independent Extraction
│  │  ├─ Extractor 1 completes form
│  │  ├─ Extractor 2 completes form
│  │  ├─ No communication during extraction
│  │  └─ Flag uncertainties
│  │
│  ├─ STEP 2: Comparison
│  │  ├─ Use comparison function
│  │  ├─ Identify discrepancies
│  │  ├─ Calculate agreement
│  │  └─ Flag for resolution
│  │
│  ├─ STEP 3: Resolution
│  │  ├─ Discuss differences
│  │  ├─ Re-check original paper
│  │  ├─ Consult third party if needed
│  │  ├─ Reach consensus
│  │  └─ Document decision
│  │
│  └─ STEP 4: Missing Data
│     ├─ Mark clearly in database
│     ├─ Add to author contact list
│     ├─ Note if could be calculated
│     └─ Plan for handling in analysis
│
├─ Progress Tracking
│  │
│  Weekly Check:
│  ├─ Studies extracted: ___/43
│  ├─ Agreement rate: ___%
│  ├─ Average time per study: ___ min
│  ├─ Issues encountered: ___
│  └─ Estimated completion: ___
│
└─ Quality Assurance
   ├─ Random audit of 10% extractions
   ├─ Check for systematic errors
   ├─ Verify calculations
   └─ Ensure consistency

PHASE 4: AUTHOR CONTACT (Week 6-10, ongoing)
│
├─ Identify Missing Data
│  ├─ List data needed from each study
│  ├─ Prioritize critical vs nice-to-have
│  ├─ Group by study/author
│  └─ Check if calculable from available data
│
├─ Prepare Contact Email
│  ├─ Introduce self and review
│  ├─ Specific data requests (numbered list)
│  ├─ Attach extraction form section
│  ├─ Offer authorship/acknowledgment
│  ├─ Set reasonable deadline (3-4 weeks)
│  └─ Keep polite and professional
│
├─ Tracking System
│  | Study | Contact Date | Response | Data Received | Follow-up |
│  |-------|-------------|----------|---------------|-----------|
│  | Smith 2020 | 2025-04-01 | 2025-04-05 | Yes (partial) | - |
│  | Jones 2021 | 2025-04-01 | - | - | 2025-04-15 |
│  | Brown 2022 | 2025-04-02 | 2025-04-20 | Yes (complete) | - |
│  | Davis 2023 | 2025-04-02 | Bounced | No | Try alt email |
│
└─ Follow-up Protocol
   ├─ Week 2: Send reminder if no response
   ├─ Week 4: Final reminder
   ├─ Week 6: Mark as "no response"
   ├─ Document all correspondence
   └─ Note in review how missing data handled

PHASE 5: DATA VERIFICATION & CLEANING (Week 11)
│
├─ Completeness Check
│  ├─ All studies have extraction completed?
│  ├─ All required fields populated?
│  ├─ Resolved conflicts documented?
│  └─ Missing data clearly marked?
│
├─ Accuracy Check
│  ├─ Random 20% double-check
│  ├─ Verify calculations (effect sizes, etc.)
│  ├─ Check units of measurement
│  └─ Validate data entry
│
├─ Consistency Check
│  ├─ Coding consistent across studies?
│  ├─ Same variable interpretations?
│  ├─ Units standardized?
│  └─ Categorical data consistent?
│
└─ Final Database
   ├─ Create analysis-ready dataset
   ├─ Code book for all variables
   ├─ Backup in multiple locations
   └─ Share with statistician

ESTIMATED TIME: 11 weeks for 43 studies
├─ Form development: 1 week
├─ Training: 1 week
├─ Extraction: 8 weeks (5-6 studies/week)
└─ Verification: 1 week
```

### Data Extraction Form Structure

| Category | Variables to Extract | Format | Example |
|----------|---------------------|---------|---------|
| **Study Identification** | | | |
| | First author surname | Text | Smith |
| | Publication year | Number (YYYY) | 2020 |
| | Study ID | Text | Smith2020 |
| | Title | Text | Effects of Mediterranean... |
| | Journal | Text | Diabetes Care |
| | DOI | Text | 10.1234/dc20-1234 |
| | Country | Dropdown | USA, UK, Spain, etc. |
| **Study Design** | | | |
| | Study design | Dropdown | RCT, Quasi-exp, etc. |
| | Randomization method | Text | Computer-generated |
| | Blinding | Checkboxes | Participants, Assessors, Analysts |
| | Study duration | Number (weeks) | 24 |
| | Follow-up period | Number (weeks) | 52 |
| | Multi-center? | Yes/No | Yes |
| | Number of centers | Number | 3 |
| | Setting | Dropdown | Hospital, Community, etc. |
| **Participants** | | | |
| | Sample size - total | Number | 150 |
| | Sample size - intervention | Number | 75 |
| | Sample size - control | Number | 75 |
| | Age - mean (SD) | Number (Number) | 58.3 (8.2) |
| | Age - range | Text | 45-72 |
| | Sex - % female | Percentage | 52% |
| | BMI - mean (SD) | Number (Number) | 31.2 (4.5) |
| | Diabetes duration - years mean (SD) | Number (Number) | 7.3 (3.1) |
| | Baseline HbA1c - mean (SD) | Number (Number) | 8.1 (0.9) |
| | Inclusion criteria | Text | Adults 18-75, T2DM, HbA1c 7-10% |
| | Exclusion criteria | Text | T1DM, insulin therapy, CVD |
| | Ethnicity breakdown | Text | 60% Caucasian, 25% Hispanic... |
| **Intervention** | | | |
| | Intervention name | Text | Mediterranean diet |
| | Intervention description | Text | <45% fat, olive oil primary... |
| | Duration | Number (weeks) | 24 |
| | Intensity/frequency | Text | Daily, counseling q2weeks |
| | Delivery method | Dropdown | Individual, Group, Self-directed |
| | Provider training | Text | Registered dietitians |
| | Adherence measure | Text | Food diary, olive oil biomarkers |
| | Adherence rate | Percentage | 78% |
| | Co-interventions | Text | Exercise encouraged |
| **Comparison** | | | |
| | Comparison name | Text | Low-fat diet |
| | Comparison description | Text | <30% fat, low saturated fat... |
| | Duration | Number (weeks) | 24 |
| | Other details | Text | Same counseling schedule |
| **Outcomes** | | | |
| | PRIMARY: HbA1c at end | | |
| | - Intervention mean (SD) | Number (Number) | 7.2 (0.8) |
| | - Control mean (SD) | Number (Number) | 7.7 (0.9) |
| | - Mean difference (95% CI) | Number (Number, Number) | -0.5 (-0.8, -0.2) |
| | - P-value | Number | 0.003 |
| | Fasting glucose at end | | |
| | - Intervention mean (SD) | Number (Number) | 132 (18) |
| | - Control mean (SD) | Number (Number) | 145 (22) |
| | - Mean difference (95% CI) | Number (Number, Number) | -13 (-21, -5) |
| | - P-value | Number | 0.002 |
| | [Additional outcomes...] | | |
| **Quality Indicators** | | | |
| | Funding source | Text | NIH grant R01DK12345 |
| | Conflicts of interest | Text | None declared |
| | Trial registration | Text | NCT01234567 |
| | Protocol published | Yes/No | Yes |
| | ITT analysis | Yes/No/Unclear | Yes |
| | Attrition rate | Percentage | 12% |
| | Reasons for dropout | Text | Lost follow-up (8%), adverse events (2%) |
| **Risk of Bias** | | | |
| | [RoB 2 domains] | Low/Some concerns/High | [See RoB section] |
| **Notes** | | | |
| | Additional notes | Text | Subgroup analysis by baseline HbA1c |
| | Missing data | Text | Lipid data not reported |
| | Contact author | Yes/No | Yes - requested lipid data |
| | Data calculated | Text | SE converted to SD |

### Example Completed Extraction

**Study: Smith et al. 2020**

| Field | Data |
|-------|------|
| **Study ID** | Smith2020 |
| **Design** | Parallel RCT |
| **Duration** | 24 weeks |
| **Total N** | 150 (75 intervention, 75 control) |
| **Population** | Adults 45-72 years with T2DM |
| **Mean age** | 58.3 ± 8.2 years |
| **Female** | 52% |
| **Baseline HbA1c** | 8.1 ± 0.9% |
| **Intervention** | Mediterranean diet (35% fat, olive oil, nuts, fish, fruits, vegetables, whole grains) with biweekly dietitian counseling |
| **Comparison** | Low-fat diet (<30% fat) with same counseling schedule |
| **Primary Outcome** | HbA1c at 24 weeks |
| **Results** | Intervention: 7.2 ± 0.8% vs Control: 7.7 ± 0.9%, MD -0.5% (95% CI -0.8 to -0.2), p=0.003 |
| **Secondary** | Fasting glucose: MD -13 mg/dL (95% CI -21 to -5), p=0.002 |
| **Adherence** | 78% based on food diaries and olive oil biomarkers |
| **Attrition** | 12% (18/150) - 8% lost to follow-up, 2% adverse events, 2% withdrew consent |
| **Risk of Bias** | Low risk overall (see detailed assessment) |

### Missing Data Management Strategy

```
┌──────────────────────────────────────────────────────────────┐
│              HANDLING MISSING DATA                            │
└──────────────────────────────────────────────────────────────┘

TYPE 1: Missing Study-Level Data
│
├─ Standard Deviations Not Reported
│  Options:
│  ├─ Calculate from SE, CI, or p-value
│  ├─ Request from authors
│  ├─ Impute from similar studies
│  └─ Document method used
│
├─ Only Median/IQR Reported
│  Options:
│  ├─ Request mean/SD from authors
│  ├─ Estimate mean/SD using formulas
│  ├─ Include in narrative only
│  └─ Sensitivity analysis with/without
│
└─ Outcome Not Reported
   Options:
   ├─ Contact authors
   ├─ Check for protocol or trial registry
   ├─ Document as selective reporting
   └─ Note in risk of bias

TYPE 2: Participant-Level Missing Data
│
├─ Intention-to-Treat (ITT) Analysis
│  ├─ All randomized included
│  └─ Preferred for meta-analysis
│
├─ Per-Protocol or Complete-Case
│  ├─ Only completers analyzed
│  ├─ Potential for bias
│  └─ Note in quality assessment
│
└─ Last Observation Carried Forward (LOCF)
   ├─ Imputation method used
   └─ Note in extraction

EXTRACTION CODING FOR MISSING DATA:
├─ "NR" = Not reported
├─ "NC" = Not calculable from available data
├─ "Requested" = Contacted author
├─ "Calculated" = Derived from other data
└─ "Estimated" = Imputed or estimated

ANALYSIS PLAN:
├─ Best-case: Use all available data
├─ Sensitivity: Exclude studies with missing data
├─ Exploration: Examine impact of missing data
└─ Report: Transparent about all missing data
```

### Data Extraction Agreement Tracking

| Extractor Pair | Studies Extracted | Perfect Agreement | Minor Discrepancy | Major Discrepancy | Agreement % |
|----------------|-------------------|-------------------|-------------------|-------------------|-------------|
| Extractor 1 & 2 | 43 | 28 (65%) | 12 (28%) | 3 (7%) | 93% |

**Discrepancy Types**:
- Minor: Rounding differences, formatting (easily resolved)
- Major: Different values extracted, missing vs present data (requires discussion)

**Common Discrepancies**:
1. Baseline vs endpoint data confusion (5 instances)
2. ITT vs per-protocol sample sizes (3 instances)  
3. Converting units (4 instances)
4. Interpreting unclear text (6 instances)

