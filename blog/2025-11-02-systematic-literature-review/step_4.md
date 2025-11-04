---
draft: true # ← Will not appear in published site
---

## Step 4: Designing the Search Strategy

A comprehensive search strategy is crucial for identifying all relevant studies
and minimizing publication bias.

### Search Strategy Development Timeline

```
Week 1: Planning & Preparation
│
├─ Day 1: Librarian Meeting
│  ├─ Discuss PICO components
│  ├─ Identify key concepts
│  ├─ Select databases
│  └─ Set timeline
│
├─ Day 2-3: Term Generation
│  ├─ List synonyms for each concept
│  ├─ Identify subject headings (MeSH, Emtree)
│  ├─ Check truncation options
│  └─ Note spelling variations
│
└─ Day 4-5: Build Initial Strategy
   ├─ Combine terms with Boolean operators
   ├─ Test in one database (PubMed)
   ├─ Check sample of results
   └─ Identify known key studies

Week 2: Testing & Refinement
│
├─ Day 6-7: Sensitivity Check
│  ├─ Are known studies captured?
│  ├─ Results too broad? Too narrow?
│  ├─ Review first 50-100 results
│  └─ Adjust terms as needed
│
├─ Day 8-9: Specificity Check
│  ├─ Too many irrelevant results?
│  ├─ Add more specific terms
│  ├─ Use proximity operators
│  └─ Re-test
│
└─ Day 10: Peer Review
   ├─ Share strategy with team
   ├─ Get feedback from content expert
   ├─ Librarian final review
   └─ Make final adjustments

Week 3: Translation & Documentation
│
├─ Day 11-14: Adapt for Each Database
│  ├─ PubMed/MEDLINE (MeSH)
│  ├─ Embase (Emtree)
│  ├─ Cochrane Library
│  ├─ Web of Science
│  └─ Discipline-specific databases
│
└─ Day 15: Document Everything
   ├─ Create search log template
   ├─ Save all strategies
   ├─ Prepare supplementary file
   └─ Ready for execution


┌─────────────────────────────────────────────────────────────┐
│              SEARCH STRATEGY DEVELOPMENT                    │
└─────────────────────────────────────────────────────────────┘
    │
    ├─▶ STEP 1: Identify Key Concepts from PICO
    │   • Break down each component
    │   • List main concepts
    │
    ├─▶ STEP 2: Generate Synonyms and Related Terms
    │   • Use thesauri and dictionaries
    │   • Consider spelling variations
    │   • Include acronyms and abbreviations
    │
    ├─▶ STEP 3: Identify Database Subject Headings
    │   • MeSH terms (PubMed)
    │   • Emtree terms (Embase)
    │   • Check each database's controlled vocabulary
    │
    ├─▶ STEP 4: Build Search Strings
    │   • Combine synonyms with OR
    │   • Combine concepts with AND
    │   • Use truncation (*) and wildcards (?)
    │   • Apply proximity operators (NEAR, ADJ)
    │
    ├─▶ STEP 5: Add Filters
    │   • Date range
    │   • Language
    │   • Publication type
    │   • Study design (if possible)
    │
    ├─▶ STEP 6: Pilot Test
    │   • Run in one database
    │   • Check sample of results
    │   • Verify known studies are captured
    │
    ├─▶ STEP 7: Refine
    │   • Adjust sensitivity/specificity
    │   • Add missing terms
    │   • Remove ineffective terms
    │
    └─▶ STEP 8: Adapt for Each Database
        • Modify syntax as needed
        • Translate subject headings
        • Document all variations
```

### Database Selection by Discipline

| Discipline | Primary Databases | Supplementary Databases | Gray Literature Sources |
|------------|-------------------|------------------------|------------------------|
| **Medicine/Health** | PubMed/MEDLINE, Embase, Cochrane Library | CINAHL, PsycINFO, Web of Science | ClinicalTrials.gov, WHO ICTRP, FDA.gov |
| **Psychology** | PsycINFO, PubMed, Scopus | PsycARTICLES, Web of Science | DARE, PsycEXTRA, dissertations |
| **Education** | ERIC, Education Source | British Education Index, Web of Science | Education databases, policy documents |
| **Social Sciences** | Sociological Abstracts, Social Sciences Citation Index | JSTOR, ProQuest | Government reports, NGO publications |
| **Engineering** | IEEE Xplore, Engineering Village | ACM Digital Library, Scopus | Technical reports, patents |
| **Business** | Business Source Complete, ABI/INFORM | EconLit, Web of Science | Industry reports, working papers |
| **Environmental** | Web of Science, Scopus | GeoRef, Environmental Science Database | EPA, environmental agency reports |

### Search String Construction Guide

```
┌──────────────────────────────────────────────────────────────┐
│           BUILDING EFFECTIVE SEARCH STRINGS                  │
└──────────────────────────────────────────────────────────────┘

STEP 1: Identify Core Concepts (from PICO)
        Example: Diabetes, Mediterranean diet, Glycemic control

STEP 2: Generate Synonyms & Related Terms
        │
        Diabetes:
        ├─ diabetes mellitus
        ├─ diabetic
        ├─ T2DM
        ├─ NIDDM
        └─ non-insulin dependent diabetes
        
        Mediterranean Diet:
        ├─ Mediterranean diet
        ├─ MedDiet
        ├─ Mediterranean-style diet
        └─ Mediterranean dietary pattern
        
        Glycemic Control:
        ├─ glycemic control
        ├─ glycaemic control (UK spelling)
        ├─ blood glucose
        ├─ HbA1c
        ├─ hemoglobin A1c
        └─ glucose control

STEP 3: Add Database Subject Headings
        │
        PubMed MeSH Terms:
        ├─ "Diabetes Mellitus, Type 2"[Mesh]
        ├─ "Diet, Mediterranean"[Mesh]
        └─ "Glycated Hemoglobin A"[Mesh]

STEP 4: Combine Synonyms with OR (within concept)
        │
        (diabetes OR "diabetes mellitus" OR diabetic OR T2DM OR NIDDM)

STEP 5: Combine Concepts with AND (between concepts)
        │
        [Diabetes terms] AND [Diet terms] AND [Outcome terms]

STEP 6: Apply Truncation & Wildcards
        │
        diet* → diet, diets, dietary
        glyc?emic → glycemic, glycaemic

STEP 7: Use Proximity Operators (if available)
        │
        mediterranean ADJ2 diet → Mediterranean, diet within 2 words
        "mediterranean diet" → exact phrase

STEP 8: Add Filters
        │
        Filters: English, 2010-present, Humans, Clinical Trial or RCT

FINAL SEARCH STRING:
("Diabetes Mellitus, Type 2"[Mesh] OR "diabetes mellitus, type 2" 
OR "type 2 diabetes" OR T2DM OR NIDDM OR "non-insulin dependent 
diabetes") AND ("Diet, Mediterranean"[Mesh] OR "mediterranean diet*" 
OR "MedDiet" OR "mediterranean-style diet*") AND ("Glycated Hemoglobin 
A"[Mesh] OR HbA1c OR "hemoglobin A1c" OR "haemoglobin A1c" OR 
"glycemic control" OR "glycaemic control" OR "blood glucose" OR 
"glucose control") 
Filters: English, 2010/01/01 - present, Humans
```

### Search Sensitivity vs Precision Trade-off

```
                HIGH SENSITIVITY
                (Comprehensive)
                      │
        ┌─────────────┼─────────────┐
        │             │             │
    Many results   Captures all   Time-consuming
    (10,000+)    relevant studies    to screen
        │             │             │
        └─────────────┼─────────────┘
                      │
        ◄─────────────●─────────────►
      BROAD                      NARROW
     Search                      Search
        │                           │
        └─────────────┬─────────────┘
                      │
        ┌─────────────┼─────────────┐
        │             │             │
    Fewer results  May miss some   Faster to
    (100-500)      relevant studies  screen
        │             │             │
        └─────────────┼─────────────┘
                      │
                HIGH PRECISION
                 (Focused)

RECOMMENDATION: Start with HIGH SENSITIVITY
Then refine if needed based on results
```

### Comprehensive Search Source Checklist

| Source Type | Specific Sources | Purpose | Completed |
|-------------|------------------|---------|-----------|
| **Electronic Databases** | PubMed, Embase, Cochrane, Web of Science, etc. | Primary literature search | ☐ |
| **Gray Literature** | | | |
| ├─ Trial Registries | ClinicalTrials.gov, WHO ICTRP, EU Clinical Trials Register | Unpublished/ongoing trials | ☐ |
| ├─ Thesis/Dissertations | ProQuest Dissertations, EThOS, DART-Europe | Academic gray literature | ☐ |
| ├─ Conference Proceedings | Web of Science Conference Proceedings, Scopus | Recent unpublished findings | ☐ |
| ├─ Government/Agency Reports | WHO, CDC, FDA, NICE, relevant agencies | Policy/regulatory documents | ☐ |
| **Citation Searching** | | | |
| ├─ Backward Citation | Reference lists of included studies | Studies cited by included papers | ☐ |
| ├─ Forward Citation | Google Scholar, Web of Science "Cited by" | Studies citing included papers | ☐ |
| **Hand Searching** | | | |
| ├─ Key Journals | Top 3-5 journals in field | Issues not yet indexed | ☐ |
| ├─ Relevant Organizations | Professional societies, advocacy groups | Organization publications | ☐ |
| **Expert Consultation** | | | |
| ├─ Content Experts | Email key researchers in field | Known ongoing/unpublished work | ☐ |
| ├─ Author Contact | Contact authors of conference abstracts | Request full papers | ☐ |

### Search Results Tracking Table

| Database | Date Searched | Search Strategy File | Results | Unique Records | Notes |
|----------|---------------|---------------------|---------|----------------|-------|
| PubMed | 2025-03-15 | search_pubmed_v1.txt | 1,247 | 1,247 | Baseline search |
| Embase | 2025-03-15 | search_embase_v1.txt | 1,834 | 978 | 856 duplicates with PubMed |
| Cochrane CENTRAL | 2025-03-15 | search_cochrane_v1.txt | 156 | 34 | 122 already in PubMed/Embase |
| CINAHL | 2025-03-16 | search_cinahl_v1.txt | 423 | 89 | 334 duplicates |
| Web of Science | 2025-03-16 | search_wos_v1.txt | 967 | 234 | 733 duplicates |
| **Subtotal Databases** | — | — | **4,627** | **2,582** | — |
| ClinicalTrials.gov | 2025-03-17 | manual_search_log.docx | 45 | 12 | 33 already found or not relevant |
| WHO ICTRP | 2025-03-17 | manual_search_log.docx | 23 | 8 | — |
| **Subtotal Trials** | — | — | **68** | **20** | — |
| Forward citation (5 key papers) | 2025-03-18 | citation_tracking.xlsx | 234 | 45 | Google Scholar |
| Backward citation (included studies) | 2025-03-18 | citation_tracking.xlsx | 156 | 28 | From initial screening |
| **Subtotal Citation** | — | — | **390** | **73** | — |
| Hand search: 3 key journals | 2025-03-19 | manual_search_log.docx | 12 | 12 | 2023-2024 issues |
| Gray literature (ProQuest) | 2025-03-19 | search_proquest_v1.txt | 34 | 7 | Dissertations |
| **Grand Total** | — | — | **5,131** | **2,694** | After de-duplication |

### Search Documentation Template

| Database | Platform | Date | Search # | Search Terms | Limiters | Results |
|----------|----------|------|----------|--------------|----------|---------|
| PubMed | NLM | 2025-03-15 | #1 | "diabetes mellitus, type 2"[MeSH] | None | 156,823 |
| PubMed | NLM | 2025-03-15 | #2 | "type 2 diabetes" OR T2DM OR NIDDM | None | 203,456 |
| PubMed | NLM | 2025-03-15 | #3 | #1 OR #2 | None | 245,789 |
| PubMed | NLM | 2025-03-15 | #4 | "diet, mediterranean"[MeSH] OR "mediterranean diet*" | None | 3,456 |
| PubMed | NLM | 2025-03-15 | #5 | #3 AND #4 | None | 234 |
| PubMed | NLM | 2025-03-15 | #6 | #5 AND ("HbA1c" OR "glycemic control"...) | English, 2010-present | 87 |

