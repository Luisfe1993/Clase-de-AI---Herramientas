# BA Automated Analysis

## What This Skill Does

This skill guides you through analyzing data from a Power BI semantic model, step by step. It connects to the model, helps you extract the right data, then delegates statistical analysis and report authoring to specialist agents and skills. It generates the interactive HTML dashboard and saves a session manifest for replay. If you need to refresh the analysis later, a single replay command re-runs the entire workflow with updated data.

## Prerequisites

1. **Power BI MCP server** -- the `powerbi-modeling-mcp` MCP server must be configured in your CLI environment. If you are not sure whether this is set up, contact your admin or check your CLI settings file for a `powerbi-modeling-mcp` entry.
2. **Python 3.10+** -- with these packages installed:
   ```
   pip install pandas numpy scipy statsmodels
   ```
3. **Internet access** -- needed for Chart.js CDN (used to render charts in the dashboard). The markdown report works offline.
4. **Specialist agents and skills** -- the following must be installed in your CLI environment:
   - `senior-data-analyst` agent
   - `data-definitions-dictionary` skill
   - `analysis-report-authoring` skill

## Quick Start: First Run

1. Open your CLI (GitHub Copilot CLI or Claude Code).
2. Navigate to your project directory.
3. Say: **"Run ba-automated-analysis"** (or "Analyze this semantic model").
4. The skill will walk you through five questions:
   - **Which workspace?** (default: "FT Data Analytics PRD")
   - **Which semantic model?**
   - **Describe the data you need** (in plain English -- e.g., "Monthly win rates by workload for CFY, split by PEC status")
   - **What type of analysis?** (pick from a list: descriptive, correlation, intervention effectiveness, dimensional breakdown, feature importance, or growth and adoption)
   - **Who is the audience?** (leadership brief, technical report, or both)
5. Review the generated DAX query when prompted. Approve it before the skill runs it.
6. Wait for analysis to complete. The skill will show progress as it moves through each phase.
7. Find your outputs in the `[analysis-name]/` directory that the skill creates.

## Quick Start: Replay

Use replay to refresh a previous analysis with current data -- no need to answer the setup questions again.

1. Navigate to the directory containing your previous `session-manifest.yaml`.
2. Say: **"Replay analysis from session-manifest.yaml"**
3. The skill reconnects to the same model and re-extracts fresh data.
4. It shows you the data delta (e.g., "Previous: 1,247 rows. Current: 1,312 rows (+65 new records)").
5. Updated outputs replace the previous versions. The manifest is updated with a new timestamp.

## Example Session Transcript

Below is an abbreviated example of what a typical session looks like. The key decision points are highlighted.

```
You:    Run ba-automated-analysis

Skill:  Which workspace should I connect to? (default: FT Data Analytics PRD)

You:    FT Data Analytics PRD

Skill:  Connected. Found 14 tables in the model.
        Which semantic model should I use?

You:    FT Engagement Analytics

Skill:  Model loaded. Tables include: FactEngagement, DimWorkload, DimCustomer,
        DimTimePeriod, ...
        Describe the data you need.

You:    Monthly win rates by workload for CFY, split by PEC status

Skill:  Here is the DAX query I generated:

        EVALUATE
        SUMMARIZECOLUMNS(
            DimTimePeriod[Fiscal_Month],
            DimWorkload[Workload_Family],
            FactEngagement[PEC_Flag],
            "Win_Rate", DIVIDE(...)
            ...
        )

        Does this DAX query look correct?

You:    Yes, run it

Skill:  Extracted 1,247 rows, 6 columns. Saved to data/win-rates-by-workload.csv.
        Profiling data...
        Generated Data Definitions.md (6 columns documented).
        Generated patterns.md.

        What type of analysis?
          - Descriptive
          - Correlation
          - Intervention effectiveness
          - Dimensional breakdown
          - Feature importance
          - Growth & adoption

You:    Intervention effectiveness

Skill:  Who is the audience?
          - Leadership brief
          - Technical report
          - Both

You:    Both

Skill:  Running analysis... Generated run_analysis.py.
        Script completed. 3 chart configs saved to charts/.
        Report written to output/Win Rates by Workload Report.md.
        ...
        Dashboard written to output/Win Rates by Workload Dashboard.html.
        Session manifest saved to session-manifest.yaml.

        Summary:
        - 1,247 rows analyzed across 8 workload families
        - PEC engagement associated with +12.4pp higher win rate (CMH OR 1.87, p < 0.001)
        - Strongest effect in Security (+18.2pp) and Modern Work (+14.1pp)

        To refresh this analysis later, run:
        "Replay analysis from session-manifest.yaml"
```

## Output Files

After the skill completes, your analysis directory contains these files:

| File | Location | Description |
|------|----------|-------------|
| Raw data CSV | `data/[name].csv` | Extracted data from the semantic model |
| Data Definitions | `data/Data Definitions.md` | Column dictionary with types, definitions, and examples |
| Patterns | `data/patterns.md` | Analysis conventions, domain terms, and visualization suggestions |
| Analysis script | `analysis/run_analysis.py` | Python script that produced the statistical results |
| Report | `output/[Name] Report.md` | Full analysis report with statistics and methodology |
| Dashboard | `output/[Name] Dashboard.html` | Interactive HTML dashboard with charts and KPI cards |
| Session manifest | `session-manifest.yaml` | Recipe file for replaying this analysis with fresh data |

## Troubleshooting

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| "Cannot connect to model" | MCP server not running or not configured | Check that `powerbi-modeling-mcp` is listed in your CLI settings and the server is running. Restart your CLI if needed. |
| Empty results from DAX query (0 rows) | The model has no data matching your filters | Verify the model has been refreshed recently. Check date filters -- if you asked for CFY data, make sure the model contains current fiscal year records. |
| "ModuleNotFoundError: pandas" | Python packages not installed | Run: `pip install pandas numpy scipy statsmodels` |
| Charts not showing in the dashboard | No internet access or Chart.js CDN is blocked | Open the dashboard on a machine with internet access. If your network blocks CDNs, ask your admin about local hosting options. |
| Replay fails with "manifest not found" | You are in the wrong directory | Navigate to the folder that contains `session-manifest.yaml`, then retry. |
| Analysis script errors out | Data shape is different from what the script expects | Open `data/Data Definitions.md` to check column types and names. If columns changed, re-run the full analysis instead of replay. |
| Unexpected NaN or missing values in the report | Source data has NULLs in key columns | Check the raw CSV for missing values. You may need to adjust your DAX query to filter out incomplete records. |
| Dashboard layout looks broken | Browser zoom is not at 100%, or very old browser | Reset browser zoom to 100%. Use a modern browser (Edge, Chrome, Firefox). The dashboard is responsive at 768px and above. |

## Skill Files (for maintainers)

These files make up the skill internals. You do not need to read them to use the skill -- they are here for people maintaining or extending it.

| File | Purpose |
|------|---------|
| `SKILL.md` | Orchestration flow with six phases, quality gates, and error handling |
| `references/dax-extraction.md` | DAX query patterns and MCP tool call sequences (loaded in Phase 1) |
| `references/fluent2-tokens.md` | Fluent 2 design tokens, Chart.js palette, and dashboard generation rules (loaded in Phase 4) |
