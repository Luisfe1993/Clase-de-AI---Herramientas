---
name: analysis-report-authoring
description: Use when structuring statistical analysis findings into a multi-audience analytical report. Triggers include having completed statistical analysis output, needing to write an executive-grade report from Python analysis results, or converting analytical findings into a stakeholder-ready markdown document with Word conversion.
---

# Analysis Report Authoring

## Overview

Structures statistical analysis output into a multi-audience analytical report (markdown -> Word). Every finding follows a fixed format: what the number is, what the test does, what the result means, and whether it matters in practice. The report skeleton ensures leadership reads the summary, product teams read the sections, and delivery teams read the appendix.

## When to Use

- Statistical analysis is complete (run_analysis.py has been executed)
- You have findings that need structuring into a stakeholder-ready report
- You need to convert analysis output into a multi-audience document
- You are in Phase 4 of the `end-to-end-analysis-pipeline` skill

## When NOT to Use

- You need to run the statistical analysis itself (delegate to `senior-data-analyst` agent)
- You need to write SQL extraction queries (delegate to `tsql-query-writer` agent)
- You are documenting columns/data definitions (use `data-definitions-dictionary` skill)

## Report Skeleton (Fixed Structure)

Every report follows this exact structure. Do not reorder or omit sections.

```
# [Analysis Title] -- [Dataset Description]

> **Snapshot:** [date] | **Fiscal Year:** [fiscal year context]
> **Audience:** Leadership, Product Teams, Analytics & Delivery Teams

## How to Read This Report
   - Quick-reference table of EVERY statistical term used in the report
   - Each term gets: What it tells you | Plain-English Analogy
   - End with the universal causation caveat paragraph

## Executive Summary
   - 5-8 numbered key findings
   - Format: **Bold the so-what first**, evidence second
   - Include key numbers inline (win rates, effect sizes, NNTs)
   - This is the ONLY section leadership reads -- make it complete

## 1. Population Overview
   - Dataset dimensions: rows, unique entities, categories
   - ASCII population hierarchy tree (indented, with counts and percentages)
   - Population segment table with Count | Share | Definition
   - Primary rate definition with denominator stated
   - Analysis base rationale blockquote explaining exclusions

## 2-N. Analysis Sections (one per business question)
   - Business question stated at section top
   - Context paragraph explaining the dimension/intervention
   - Primary data table with **bold primary metric column**
   - Statistical test results with FULL explanation template
   - Key Insight blockquote
   - Caveats where applicable

## N+1. Methodology, Caveats & Limitations
   - Selection bias / causation disclaimer
   - Large-sample significance caveat
   - Multiple comparisons note
   - Snapshot-in-time limitation
   - Methods summary table: Method | What it answers | Where used

## Appendix (if needed)
   - Full-dataset breakdowns (complement, don't duplicate section tables)
   - Detailed tier tables
   - Secondary analyses
```

## Statistical Explanation Template (Required for Every Test)

Every statistical test result in the report MUST use this format. No exceptions.

```markdown
**[Test Name]:** [statistic] = [value], [df if applicable], [p-value], **[Effect Size Measure] = [value]** ([interpretation])

The **[test name]** answers: *"[question in plain language]?"* With a p-value [interpretation],
the answer is [conclusion] -- [what this means for the specific data].

But with [N]+ records, even tiny differences become "statistically significant." That's why we
also report **[effect size measure]**, which measures *how strong* the relationship is:
- [scale interpretation table or inline ranges]

Our [effect size] of **[value]** [interpretation in context]. In practical terms: **[one-sentence
business implication]**.
```

### Worked Example: Wrong vs Right

**WRONG -- just reporting numbers:**
> Chi-square = 835.2, p < 0.001. PEC Engage has a higher win rate.

**RIGHT -- full explanation:**
> **Chi-Square Test:** chi2 = 835.2, df = 2, p < 0.001, **Cramer's V = 0.190** (medium effect)
>
> The **chi-square test** answers: *"Could the difference in win rates between PEC Engage, PEC Triage, and No PEC be due to random chance?"* With a p-value far below 0.001, the answer is a definitive **no** -- the relationship between PEC status and winning is statistically real.
>
> But with 23,000+ records, even tiny differences become "statistically significant." That's why we also report **Cramer's V**, which measures *how strong* the relationship is:
> - 0.00-0.10 = negligible
> - 0.10-0.20 = small but meaningful
> - **0.20-0.30 = medium**
> - 0.30+ = large
>
> Our Cramer's V of **0.19** falls at the upper end of "small but meaningful," bordering on medium. In practical terms: **PEC status is a genuinely meaningful predictor of KPI wins** -- not the only factor, but an important one.

## Audience Layering

| Audience | Reads | Needs |
|----------|-------|-------|
| **Leadership** | Executive Summary only | So-what first, 1-2 supporting numbers, no methodology |
| **Product Teams** | Analysis sections 2-N | Full breakdowns with CIs, tier analysis, correlations, dimensional cuts |
| **Delivery/Operations** | Appendix + coverage tables | NNT, lift tables, uncovered opportunity lists, actionable segments |

Write each section for its primary audience. The Executive Summary must stand alone -- a reader who stops there should still understand all key findings.

## Hard Guardrails

### Denominator Discipline
- **NEVER report a rate without stating the denominator explicitly**
- State N in every table header or as a column
- Define the analysis population and exclusions before any rates appear
- Wrong: "Win rate is 34.4%"
- Right: "Win rate is 34.4% (2,513 / 6,695 CFY-eligible PEC Engage records)"

### Causation Disclaimers
- Every intervention analysis (PEC, SME, any treatment) MUST include a causation caveat
- Place the caveat in both the How to Read section AND inline with findings
- Template: "**Caveat:** [Metric] assumes [intervention] *causes* the difference. Because [intervention] is not randomly assigned ([reason]), the true [metric] is likely [direction]. Treat these findings as strong directional evidence, not proof of cause and effect."

### Effect Size Required
- **NEVER report a p-value without an effect size measure**
- Chi-square -> Cramer's V
- Proportions -> Absolute lift (pp) AND relative lift (multiplier)
- Continuous -> Mann-Whitney with median comparison
- Always interpret the effect size: negligible / small / medium / large

### Formatting Safety
- Use `--` not em-dash (`---`) for encoding safety
- Bold the **primary metric** column in every comparison table
- ASCII only in inline text (`->`, `[x]`, `--`). Unicode fine in file output with `encoding='utf-8'`
- Every table must have aligned columns and consistent formatting

## Language Rules

| Instead of | Use |
|------------|-----|
| "at-risk" | "opportunity" |
| "failing" | "uncovered" or "addressable" |
| "subjects" | "customer-workloads" or the specific entity name |
| Raw average alone (skewed data) | Median alongside average, with explanation of why median is preferred |
| "significant" (ambiguous) | "statistically significant" or "practically meaningful" (be explicit which) |

## Data Table Format

Every comparison table follows this structure:

```markdown
| [Dimension] | Records | % of Pop. | Wins | **Win Rate** | 95% Wilson CI | Lift vs [Baseline] |
|---|---|---|---|---|---|---|
| **[Top group]** | N | pct | wins | **rate** | [lo%, hi%] | +X.Xpp |
| [Other group] | N | pct | wins | rate | [lo%, hi%] | +/-X.Xpp |
| [Baseline group] | N | pct | wins | rate | [lo%, hi%] | -- |
```

- **Bold the primary metric column header** (usually Win Rate)
- Bold the top-performing row's dimension value
- Include Wilson CIs on every proportion
- Show lift relative to baseline (last row = `--`)
- Include Records column so denominators are always visible

## md_to_docx Conversion Checklist

After Report.md is complete, convert to Word:

1. Generate `md_to_docx.py` using pandoc or python-docx
2. Verify all markdown tables render as Word tables (not code blocks)
3. Confirm heading hierarchy maps to Word styles (H1 -> Heading 1, H2 -> Heading 2)
4. Check that blockquotes render as styled callout boxes or indented text
5. Verify code blocks (ASCII trees, formulas) render in monospace font
6. Confirm bold/italic formatting carries through
7. Test that the document opens correctly in Word
8. Page breaks before major sections (Executive Summary, each analysis section)

## Delegation

| Task | Delegate To |
|------|-------------|
| Statistical analysis content (findings, tests, code) | `senior-data-analyst` agent |
| SQL extraction queries | `tsql-query-writer` agent |
| Column documentation | `data-definitions-dictionary` skill |
| Pipeline orchestration | `end-to-end-analysis-pipeline` skill |

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Reporting p < 0.001 without effect size | Always pair with Cramer's V, lift, or equivalent |
| "Win rate is 34%" with no denominator | State N and population definition |
| Claiming PEC "causes" wins | Add causation caveat; use "associated with" language |
| Showing averages for skewed data | Add medians; explain mean-median gap |
| Duplicating section tables in appendix | Appendix tables complement with different cuts (full dataset vs. subset) |
| Using em-dashes or Unicode in console output | Use `--` and ASCII; Unicode only in file output with utf-8 encoding |
