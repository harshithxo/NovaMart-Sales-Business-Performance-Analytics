# Power BI Implementation Guide

1. Open Power BI Desktop and create a blank report.
2. Load the cleaned CSVs from `data/cleaned/`.
3. Keep Orders as the fact table. Load Customers, Products, Regions, Salespeople and Channels as dimensions.
4. Create a Date table covering 2025-01-01 to 2025-12-31 and mark it as the Date table.
5. Create the relationships documented in `data_model.md`.
6. Paste the measures from `measures.dax`.
7. Apply the six-page layout in `dashboard_spec.md`.
8. Add slicers and drill-down hierarchies.
9. Validate KPI values against `qa/cross_validation.csv`.
10. Export page screenshots to `screenshots/` after your local Power BI build.

### Expected KPI check
The screenshot previews in this repo were generated from the same cleaned analytical fact and are not substitutes for a native `.pbix` validation.
