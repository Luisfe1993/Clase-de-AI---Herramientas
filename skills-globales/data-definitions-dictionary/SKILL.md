---
name: data-definitions-dictionary
description: Use when you need to generate column-level documentation from a query (SQL or DAX) and its CSV output. Triggers include having a new dataset to document, needing a Data Definitions.md for an analysis project, onboarding a new data source, Phase 2 of the end-to-end-analysis-pipeline skill, or Phase 2 of the ba-automated-analysis skill. Also use when patterns.md is needed for Python analysis conventions.
---

# Data Definitions Dictionary

## Overview

Auto-generates column-level documentation from a source query (SQL or DAX) and CSV data. Produces two files: `Data Definitions.md` (comprehensive column dictionary) and `patterns.md` (technical patterns for downstream analysis). Every column gets a data type, source, business definition, NULL rate, and example values. Derived columns get formulas. Flags get both values explained.

Supports two input paths:
- **SQL path:** T-SQL query with CTEs → used by `end-to-end-analysis-pipeline`
- **DAX path:** DAX EVALUATE query from a Power BI semantic model → used by `ba-automated-analysis`

## When to Use

- You have a SQL or DAX query and its CSV output that need documentation
- You are in Phase 2 of the `end-to-end-analysis-pipeline` (SQL path)
- You are in Phase 2 of the `ba-automated-analysis` (DAX path)
- You need to onboard a new dataset for analysis
- An existing dataset needs updated documentation after column changes

## When NOT to Use

- You need to write the SQL query itself (use `tsql-query-writer` agent)
- You need statistical analysis (use `senior-data-analyst` agent)
- You need to structure findings into a report (use `analysis-report-authoring` skill)

## Inputs Required

1. **Source query** -- one of:
   - **SQL query** (.sql file or inline) -- for Source SQL Architecture section (CTE-based)
   - **DAX query** (inline or from ba-automated-analysis Phase 1) -- for Source DAX Query section
2. **CSV data** (.csv file) -- for Column Dictionary profiling
3. **Context** -- dataset name, grain, fiscal year, population definition, source system (database or semantic model)

## Output: Data Definitions.md

### Section 1: Overview

```markdown
## 1. Overview

| Property | Value |
|----------|-------|
| **Dataset** | [descriptive name] |
| **Grain** | [what each row represents] |
| **Row Count** | [exact count from CSV] |
| **Columns** | [exact count from CSV header] |
| **Snapshot Date** | [date of data extraction] |
| **Fiscal Year** | [fiscal context with start date] |
| **Population** | [who/what is included and the key filter] |
| **Regions** | [count and list if applicable] |
| **Source System** | [database/schema and table count] |

[1-2 sentence description of what the dataset IS -- e.g., "single-point-in-time export" vs "time series"]
```

If the analysis has initial requirements (questions to answer), list them as a numbered sub-section:

```markdown
### 1.1 Initial Requirements

[Numbered list of analysis questions]

**Audiences:** [who will consume this analysis]
```

### Section 2: Source Query Architecture

Use the variant that matches the input query type.

#### Variant A -- SQL (T-SQL with CTEs)

One subsection per CTE (or major query block). Follow this format exactly:

```markdown
## 2. Source SQL Architecture

The query is built from [N] CTEs that feed into a final SELECT:

### CTE [N]: `[CTE_NAME]`
- **Source:** `[schema.table]`
- **Filter:** `[key WHERE conditions]` (if any)
- **Logic:** [what the CTE does -- joins, CASE expressions, UNION ALL, etc.]
- **Output:** `[column1]`, `[column2]`, ...
- **Purpose:** [one-sentence business purpose]
```

For each CTE, explain:
- Which source tables it reads from
- What filters narrow the data
- What transformations or business logic it applies
- What columns it outputs
- Why it exists in the pipeline

#### Variant B -- DAX (Power BI semantic model)

When the source is a DAX query extracted from a semantic model, document:

```markdown
## 2. Source DAX Query

**Semantic model:** [workspace] / [model name]
**Query type:** [EVALUATE / SUMMARIZECOLUMNS / etc.]

### Tables Referenced
| Table | Role |
|-------|------|
| `[TableName]` | [fact table / dimension / bridge -- one-sentence role] |

### Measures Used
| Measure | Definition | Purpose |
|---------|-----------|---------|
| `[Measure Name]` | [DAX expression or "model-defined"] | [what it computes] |

### Filters Applied
- [Filter 1 -- e.g., "CFY_PRIORITIZED = 1"]
- [Filter 2]

### Column Derivations
[Document any ADDCOLUMNS, calculated columns, or Month_Sort logic added during extraction]
```

For DAX queries, explain:
- Which model tables provide the data
- What measures are evaluated (model-defined vs inline)
- What filters narrow the population
- What post-query derivations were added (e.g., Month_Sort, Python-side calculations)

### Section 3: Column Dictionary

Group columns by business category. Each category gets its own sub-table.

```markdown
## 3. Column Dictionary

### 3.1 [Category Name]

| # | Column Name | Data Type | Source | Business Definition | NULL Rate | Example Values |
|---|------------|-----------|--------|-------------------|-----------|---------------|
| 1 | `COLUMN_NAME` | [type] | `[source_table.column]` or Derived | [definition] | [rate] | `val1`, `val2` |
```

#### Column Documentation Rules

**Every column gets ALL of these:**
- **Sequential number** (#) across the entire dataset
- **Column name** in backtick code formatting
- **Data type** (INT, VARCHAR, DATE, INT (0/1) for flags, etc.)
- **Source** -- SQL: `TABLE.COLUMN`; DAX: `'TableName'[Column]` or `[Measure Name]`; or "Derived (CASE)" / "Derived (formula)" for computed columns
- **Business definition** -- what it means, not just what it contains. For ambiguous columns, explain the business context.
- **NULL rate** -- approximate percentage or descriptor (0%, Low, Moderate, High, Very High). Note if NULLs are coalesced to 0.
- **Example values** -- 2-4 representative values in backticks

**Additional rules by column type:**

| Column Type | Additional Requirement |
|-------------|----------------------|
| **Flag (0/1)** | Explain what 1 means AND what 0 means. State count of 1s. |
| **Derived column** | Document the formula or CASE logic. Reference source columns by name. |
| **Date column** | Note sentinel values (e.g., fiscal year start = "pre-existing") |
| **Coalesced column** | State "COALESCE(..., 0)" and note that NULLs are replaced |
| **Parent/CFY pair** | Cross-reference the partner column. State subset relationship. |
| **Hierarchical status** | Document the waterfall logic (e.g., Engage -> Triage -> None) |

**Suggested categories** (adapt to your dataset):
- Identifiers & Dimensions
- Eligibility & Outcomes
- Usage & Capacity Metrics
- Growth Metrics
- Time-to-Value
- Funnel / Stage
- Resource Flags
- Forecast

### Section 4: Key Business Logic

Document relationships between columns. This section contains:

#### 4.1 Parent vs CFY Column Pattern

If the dataset has parent (all-time) and CFY (current fiscal year) column pairs:

```markdown
| Parent (all-time) | CFY (current fiscal year) | Relationship |
|---|---|---|
| `PARENT_COL` (N1) | `CFY_COL` (N2) | CFY is a subset of parent |
```

#### 4.2 Key Formulas

Document exact formulas with counts:

```markdown
**Formula [N] -- [description] ([exact/conceptual]):**

[COLUMN_A] (count) = [COLUMN_B] (count) + [COLUMN_C] (count)
```

Mark formulas as "exact" (holds for 100% of rows) or "conceptual" (edge cases exist -- state count).

#### 4.3 Visual Hierarchy

ASCII tree showing how populations nest:

```
TOP_LEVEL (count)  [description]
  +-- SUBSET_A (count)  [description]
  |     +-- LEAF_1 (count)  -- detail
  |     +-- LEAF_2 (count)  -- detail
  +-- SUBSET_B (count)
```

#### Additional Business Logic Sections

Add as needed:
- COALESCE patterns
- Population structure (opportunity vs. already-won)
- Special column behaviors (negative values, sentinel dates)
- Growth calculation methodology

### Section 5: Data Quality Notes

Table of known data quality issues:

```markdown
| Issue | Details |
|-------|---------|
| **[Column or pattern]** | [Description, impact, and whether it's a data error or valid business case] |
```

### Section 6: Statistical Methods & Formulas (if applicable)

If this dataset will be used for statistical analysis, document every method that will be applied:

For each method:
1. **What it is** -- plain language
2. **How it works** -- conceptual explanation
3. **Formula** -- in code block
4. **How to read the results** -- interpretation guide

### Section 7: Source Tables

**SQL path:**

```markdown
| # | Table | Schema | Role |
|---|-------|--------|------|
| 1 | `TABLE_NAME` | Schema | [one-sentence role description] |
```

**DAX path:**

```markdown
| # | Table | Semantic Model | Role |
|---|-------|---------------|------|
| 1 | `TableName` | [Model Name] | [one-sentence role description] |
```

## Output: patterns.md

Generate alongside Data Definitions.md. Contains technical patterns for downstream Python analysis.

```markdown
# Technical Patterns -- [Project Name]

## Python Pipeline Patterns
- [CSV reading gotchas, encoding, na_values]
- [Console vs file encoding rules]
- [Library-specific patterns from analysis]

## Terminology
- [Domain-specific terms and correct usage]
- [NEVER/ALWAYS rules for language]
- [Abbreviation expansions]

## Excluded Columns
- [Columns excluded from analysis and why]

## Analysis Patterns
- [Primary denominator definition]
- [Statistical method preferences (Wilson over Wald, etc.)]
- [Specific formula implementations]
- [Edge cases and how to handle them]

## Markdown Output
- [Formatting rules for report output]

## Column Evolution Log
- [Track column count changes during development]
- [Always check CSV header before assuming count]
```

## Abbreviation Cross-Reference

Always expand abbreviations on first use in Data Definitions.md. Refer to the **Data Dictionary** section in CLAUDE.md for the canonical list of abbreviations (PAU, DPU, MAU, MPU, RFA, PEC, FTOP, CFY, TPID, EOU, SME, KPI, OKR, etc.). Add any dataset-specific abbreviations not in CLAUDE.md to the Data Definitions.md document.

## Hard Guardrails

1. **Column count validation:** Column count in CSV header MUST equal the number of columns documented in Section 3. If they don't match, STOP and reconcile.
2. **No phantom columns:** Never document a column that doesn't exist in the CSV. If the source query (SQL SELECT or DAX EVALUATE) has a column not in the CSV, flag it as a potential export issue.
3. **No undocumented columns:** Every CSV column must appear in Section 3. If you can't determine a column's meaning, mark it with "**[NEEDS CLARIFICATION]**" -- do not guess.
4. **Abbreviation expansion:** Every abbreviation must be expanded on first use. Use the cross-reference table above plus domain knowledge.
5. **Denominator identification:** By the end of Section 4, the primary analysis denominator must be explicitly identified and justified.

## Validation Checklist

Run after generating both files:

- [ ] Column count in CSV == column count in Data Definitions.md Section 3
- [ ] Every column has all 6 fields (type, source, definition, NULL rate, examples, sequential #)
- [ ] Every flag (0/1) column has both values explained
- [ ] Every derived column has its formula documented
- [ ] Every abbreviation is expanded on first use
- [ ] Source Query Architecture covers every CTE (SQL) or every table/measure/filter (DAX)
- [ ] Key formulas are marked exact or conceptual with counts
- [ ] Population hierarchy tree is present
- [ ] patterns.md exists with all 5+ sections
- [ ] No "[TODO]" or "[NEEDS CLARIFICATION]" markers remain (or they are flagged to user)

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Documenting columns by scanning the query only | Always validate against CSV header -- the CSV is truth |
| Missing COALESCE documentation | Every COALESCE(..., 0) changes NULL semantics -- document it |
| Flag columns without explaining both values | "1 = [meaning], 0 = [meaning]" for every 0/1 column |
| Vague business definitions | "Customer identifier" is not enough. "Unique identifier for each prioritized customer (TPID)" is. |
| Skipping the visual hierarchy | The ASCII tree is often the most-referenced part of the document |
| Not tracking column count changes | Always note in patterns.md Column Evolution Log |
