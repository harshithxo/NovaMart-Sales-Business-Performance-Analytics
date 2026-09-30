# Final QA Summary

## Data

- Raw order rows: **80,340**
- Cleaned order rows: **79,298**
- Completed analytical rows: **74,478**
- Customer master rows: **7,500**
- Product master rows: **72**
- Region rows: **20**
- Salesperson rows: **30**
- Channel rows: **4**
- Order IDs unique after cleaning: **PASS**
- Foreign-key validation: **PASS**
- Financial formula reconciliation: **PASS**
- Reproducibility test: **PASS** using the repository's generator/cleaner with seed `20260930`

## SQL

- MySQL 8.0 schema/scripts created: **PASS**
- 25 business-analysis queries: **25/25 PASS** in a local SQLite compatibility test on a 12,000-row validation sample. The sample was chosen for execution-speed QA because several window-function queries are expensive in SQLite.
- Full cleaned-fact scalar KPI validation: **PASS** for Revenue, Profit, Orders, Customers, Units Sold, Profit Margin and AOV.
- Compatibility note: MySQL server/client is not installed in this environment, so the repository SQL was not executed by MySQL itself. The SQL remains MySQL 8.0 syntax.

## Python

- Notebook executed from start to finish: **PASS**
- No notebook execution errors: **PASS**
- Visualizations render in the executed notebook: **PASS**

## Excel

- Workbook created and exported: **PASS**
- KPI formulas inspected without formula errors: **PASS**
- KPI values reconcile to the full analytical fact: **PASS**
- Pivot-style analysis tables reconcile to the full analytical fact: **PASS**
- Limitation: the available workbook API does not generate native Excel PivotTable caches, so refreshable summary tables are used instead.

## Power BI

- Data model documentation: **PASS**
- Power Query M: **PASS**
- DAX measure definitions: **PASS**
- Six-page dashboard architecture: **PASS**
- Design preview screenshots: **PASS**
- Native `.pbix`: **NOT GENERATED** because Power BI Desktop is unavailable in this environment. No live PBIX measure/filter/drill-down execution is claimed.

## Cross-validation

Python and SQL were reconciled on the **full cleaned fact** for the seven headline KPIs. Excel KPI values were reconciled to those same full-fact values. Power BI outputs are specified as expected values from the same business rules, but could not be live-executed without Power BI Desktop.
