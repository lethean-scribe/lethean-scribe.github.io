---
draft: true # ← Will not appear in published site
---

## Step 9: Data Synthesis

Synthesis integrates findings across studies to answer your research question.

### Choosing Synthesis Method

| Factor | Narrative Synthesis | Meta-Analysis |
|--------|-------------------|---------------|
| **Study Homogeneity** | Studies too diverse | Studies sufficiently similar |
| **Outcome Measures** | Different measurement tools/scales | Same or convertible measures |
| **Statistical Data** | Incomplete or varied reporting | Complete statistical data available |
| **Study Designs** | Multiple different designs | Same design (typically RCTs) |
| **Populations** | Highly variable | Comparable populations |
| **Interventions** | Diverse interventions | Similar interventions |
| **When to Use** | High heterogeneity, limited data | Low-moderate heterogeneity, adequate data |

### Meta-Analysis Statistical Concepts

| Concept | Description | Interpretation |
|---------|-------------|----------------|
| **Effect Size** | Standardized measure of intervention effect | Cohen's d: 0.2=small, 0.5=medium, 0.8=large |
| **Confidence Interval** | Range likely to contain true effect | If excludes null value, effect is significant |
| **Heterogeneity (I²)** | Percentage of variability due to heterogeneity not chance | 0-40%: Low, 30-60%: Moderate, 50-90%: Substantial, 75-100%: Considerable |
| **Fixed-Effect Model** | Assumes one true effect size | Use when I² <40% |
| **Random-Effects Model** | Assumes distribution of true effects | Use when I² >40% |
| **Forest Plot** | Visual display of study results and pooled estimate | Shows effect sizes with confidence intervals |
| **Funnel Plot** | Scatter plot for publication bias detection | Asymmetry suggests bias |

### Sample Forest Plot Structure

```
┌─────────────────────────────────────────────────────────────────────┐
│                    FOREST PLOT EXAMPLE                               │
│  Effect of Mediterranean Diet on HbA1c (%) vs Control                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│ Study                     Mean Difference [95% CI]        Weight %   │
│                          -2.0  -1.0   0   1.0   2.0                  │
│                           |     |     |    |     |                   │
│ Smith 2020                ●─────|─────|    |     |        12.5%      │
│   MD: -0.85 [-1.2, -0.5] |     |     |    |     |                   │
│                           |     |     |    |     |                   │
│ Jones 2021                |    ●──────|────|     |        15.3%      │
│   MD: -0.62 [-0.9, -0.3] |     |     |    |     |                   │
│                           |     |     |    |     |                   │
│ Brown 2022                |     ●─────|────|     |        18.2%      │
│   MD: -0.45 [-0.7, -0.2] |     |     |    |     |                   │
│                           |     |     |    |     |                   │
│ Davis 2023                |     |    ●────|─────|        14.7%      │
│   MD: -0.35 [-0.6, -0.1] |     |     |    |     |                   │
│                           |     |     |    |     |                   │
│ Wilson 2024               |     |  ●──────|─────|        13.8%      │
│   MD: -0.28 [-0.5, -0.05]|     |     |    |     |                   │
│                           |     |     |    |     |                   │
│ Taylor 2024               |     | ●───────|─────|        11.2%      │
│   MD: -0.15 [-0.4, 0.1]  |     |     |    |     |                   │
│                           |     |     |    |     |                   │
│ Anderson 2024             |     |   ●─────|─────|        14.3%      │
│   MD: -0.22 [-0.5, 0.05] |     |     |    |     |                   │
│                           |     |     |    |     |                   │
│ ═══════════════════════════════════════════════════════════════     │
│ Overall (Random)          |    ◆────|─────|     |        100%        │
│   MD: -0.42 [-0.61, -0.23]|    |    |     |     |                   │
│   I² = 68%, p < 0.001     |     |     |    |     |                   │
│                           |     |     |    |     |                   │
│                       Favours     |   Favours                         │
│                       Mediterranean  Control                          │
│                                                                       │
│ Heterogeneity: I² = 68% (substantial), χ² = 21.8, p < 0.001         │
│ Test for overall effect: Z = 4.32 (p < 0.0001)                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Heterogeneity Assessment

| Statistical Test | What It Measures | Interpretation |
|-----------------|------------------|----------------|
| **Chi-squared (χ²) test** | Statistical significance of heterogeneity | p < 0.10 suggests significant heterogeneity |
| **I² statistic** | Percentage of total variation due to heterogeneity | 0-40%: Might not be important<br>30-60%: Moderate<br>50-90%: Substantial<br>75-100%: Considerable |
| **Tau² (τ²)** | Variance of true effect sizes | No universal interpretation; compare across subgroups |
| **Prediction interval** | Range of true effects in similar future studies | Wider than CI; shows clinical applicability |

### Subgroup Analysis Plan

| Variable | Subgroups | Rationale | Minimum Studies per Subgroup |
|----------|-----------|-----------|------------------------------|
| **Age** | <50 years vs ≥50 years | Metabolic differences by age | 3 |
| **Baseline HbA1c** | <8% vs ≥8% | Disease severity may affect response | 3 |
| **Intervention Duration** | 12-24 weeks vs >24 weeks | Longer duration may show greater effects | 3 |
| **Study Quality** | Low risk vs high risk of bias | Quality may impact effect estimates | 3 |
| **Geographic Region** | North America vs Europe vs Asia | Cultural dietary differences | 3 |
| **Adherence Level** | High (>80%) vs Low (<80%) | Adherence affects outcomes | 3 |

### Publication Bias Assessment

```
┌─────────────────────────────────────────────────────────────┐
│                    FUNNEL PLOT                               │
│         Standard Error (SE) vs Effect Size                   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   0.0 ┐                      ●                              │
│       │                    ●   ●                            │
│   0.1 │                  ●   ●   ●                          │
│       │                ●   ●   ●   ●                        │
│   0.2 │              ●   ●   ●   ●   ●                      │
│ S     │            ●   ●   ●   ●   ●   ●                    │
│ E 0.3 │          ●   ●   ●   ● ◆ ●   ●   ●                  │
│       │        ●   ●   ●   ●   ●   ●   ●   ●                │
│   0.4 │      ●   ●   ●   ●   ●   ●   ●   ●   ●              │
│       │    ●   ●   ●   ●   ●   ●   ●   ●   ●   ●            │
│   0.5 └──┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼──     │
│         -2.0  -1.5  -1.0  -0.5   0   0.5   1.0   1.5   2.0  │
│                      Mean Difference                         │
│                                                              │
│  ◆ = Pooled Effect Estimate                                 │
│  Symmetrical funnel = Low publication bias                  │
│  Asymmetry suggests missing studies on one side             │
└─────────────────────────────────────────────────────────────┘
```

**Publication Bias Tests**:

| Test | Result | Interpretation |
|------|--------|----------------|
| **Egger's Test** | p = 0.03 | Significant asymmetry detected |
| **Begg's Test** | p = 0.08 | Borderline significance |
| **Trim and Fill** | 5 studies imputed | Adjusted MD: -0.38 [-0.55, -0.21] |
| **Fail-safe N** | 124 studies | 124 null studies needed to nullify effect |

### GRADE Assessment Process

The GRADE (Grading of Recommendations Assessment, Development and Evaluation)
approach provides a structured framework for rating evidence certainty.


```
┌─────────────────────────────────────────────────────────────┐
│              GRADE ASSESSMENT WORKFLOW                       │
└─────────────────────────────────────────────────────────────┘

STARTING POINT
├─ Randomized Controlled Trials → HIGH certainty
└─ Observational Studies → LOW certainty

↓ DOWNGRADE FOR:

1. Risk of Bias (-1 or -2)
   └─ Study limitations affecting confidence in results

2. Inconsistency (-1 or -2)
   └─ Unexplained heterogeneity or variability in results

3. Indirectness (-1 or -2)
   └─ Differences in population, intervention, or outcomes

4. Imprecision (-1 or -2)
   └─ Wide confidence intervals, small sample size

5. Publication Bias (-1)
   └─ Strong evidence of missing studies

↑ UPGRADE FOR (observational studies only):

1. Large Effect (+1 or +2)
   └─ RR >2 or <0.5 (no confounders)

2. Dose-Response Gradient (+1)
   └─ Clear gradient supports causality

3. All Plausible Confounding Would Reduce Effect (+1)
   └─ Strengthens confidence in findings

FINAL CERTAINTY RATING
├─ High: Very confident in effect estimate
├─ Moderate: Moderately confident; true effect likely close
├─ Low: Limited confidence; true effect may differ substantially
└─ Very Low: Very little confidence; true effect likely differs
```

### GRADE Evidence Profile Example

| Outcome | Studies (Participants) | Risk of Bias | Inconsistency | Indirectness | Imprecision | Publication Bias | Effect Size | Certainty | Importance |
|---------|------------------------|--------------|---------------|--------------|-------------|------------------|-------------|-----------|------------|
| **HbA1c reduction at 6 months** | 7 RCTs (n=843) | Serious (-1) | Not serious | Not serious | Not serious | Suspected (-1) | MD -0.42% [-0.61, -0.23] | ⊕⊕○○ LOW | Critical |
| **Fasting glucose** | 5 RCTs (n=612) | Serious (-1) | Serious (-1) | Not serious | Not serious | Not detected | MD -12.5 mg/dL [-18.3, -6.7] | ⊕⊕○○ LOW | Critical |
| **Total cholesterol** | 6 RCTs (n=734) | Not serious | Serious (-1) | Not serious | Serious (-1) | Not detected | MD -8.2 mg/dL [-15.1, -1.3] | ⊕⊕○○ LOW | Important |
| **Adverse events** | 4 RCTs (n=523) | Serious (-1) | Not serious | Not serious | Very serious (-2) | Not detected | RR 1.12 [0.68, 1.85] | ⊕○○○ VERY LOW | Important |

**GRADE Certainty Legend**: 
- ⊕⊕⊕⊕ HIGH
- ⊕⊕⊕○ MODERATE  
- ⊕⊕○○ LOW
- ⊕○○○ VERY LOW

