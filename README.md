# NovaMart Sales & Business Performance Analytics

A production-style Data Analyst portfolio project showing how raw retail transaction data can be converted into validated KPIs, SQL analysis, Python EDA, Excel reporting and a Power BI management dashboard.

> **Important:** NovaMart and the dataset are fictional. The dataset is synthetic and reproducible with seed `20260930`. It is not presented as real company data.

## Project Overview

NovaMart is a fictional multi-channel retail/e-commerce company selling consumer products across Indian markets. The business question is straightforward: **where is sales performance strong, where is profitability weaker, how are customers contributing, and how do regions and channels differ?**

## Business Problem

Management needs a consistent view of revenue, profitability, customers, products, regions and channels. The project creates a single analytical definition of key KPIs and carries it consistently through SQL, Python, Excel and Power BI.

## Objectives

- Clean and validate approximately 80K raw transaction records.
- Create a relational model with Orders, Customers, Products, Regions, Salespeople and Channels.
- Answer 25+ business questions in MySQL.
- Explore trends, products, regions, customers and channels in Python.
- Build an Excel analysis workbook with KPI and pivot-style analysis tables.
- Specify a six-page Power BI dashboard with DAX measures, Power Query and model documentation.
- Produce evidence-based findings and interview-ready explanations.

## Dataset

- Raw order rows: **80,340**
- Cleaned order rows: **79,298**
- Completed analytical fact rows: **74,478**
- Customers: **7,500**
- Products: **72**
- Regions: **20**
- Salespeople: **30**
- Channels: **4**

### Data-quality issues intentionally seeded

Duplicates, missing customer keys, invalid quantities, inconsistent capitalization/whitespace, textual percentages and invalid product IDs are included in the raw layer. The cleaning pipeline documents detection, correction and validation.

## Data Cleaning

The analytical layer trims text, normalizes category/status/payment values, validates keys and positive quantities, parses discounts, removes duplicate transaction IDs, and recalculates Revenue, Cost and Profit from source components.

## SQL Analysis

`sql/business_analysis.sql` contains **25 meaningful business queries**, progressing from aggregation and joins to CTEs, conditional aggregation and window functions.

## Python Analysis

`python/sales_analysis.ipynb` covers business understanding, data loading, profiling, data-quality assessment, cleaning validation, KPI calculation, EDA, outlier analysis and insight generation.

## Excel Analysis

`excel/sales_analysis.xlsx` contains raw-data reference, cleaned analytical data, KPI summary, pivot-style analysis tables, formula examples and charts. The build environment does not expose Excel-native PivotTable creation, so the workbook uses analysis tables that reconcile to the same cleaned fact.

## Power BI Dashboard

The `powerbi/` folder contains DAX measures, Power Query M, data-model documentation, a six-page dashboard specification and a local implementation guide. **A native `.pbix` file is not included because Power BI Desktop is not available in this environment.** The project does not pretend otherwise.

The six pages are:

1. Executive Overview
2. Sales Performance
3. Product Performance
4. Regional Performance
5. Customer Analytics
6. Channel Performance

## KPIs

| KPI | Value |
|---|---:|
| Revenue | ₹924,577,392.41 |
| Cost | ₹642,467,270.00 |
| Profit | ₹282,110,122.41 |
| Profit Margin | 30.51% |
| Orders | 74,478 |
| Customers | 7,363 |
| Units Sold | 130,073 |
| Average Order Value | ₹12,414.10 |
| Repeat Customer Rate | 95.08% |

## Key Insights

See `reports/business_insights.md` for the full Finding → Evidence → Business Implication analysis. The most decision-relevant pattern is that revenue leadership and margin leadership do not always align, which makes product mix, discounting and channel context important.

## Recommendations

The recommended next investigations are tied to the actual results: regional margin review, high-revenue/low-margin product review, seasonal planning and targeted retention/cross-sell analysis.

## Technologies Used

Python, Pandas, NumPy, Matplotlib, Seaborn, MySQL, Microsoft Excel, Power BI, DAX, Power Query M, Git/GitHub.

## Repository Structure

```text
sales-business-performance-analytics/
├── data/
│   ├── raw/
│   └── cleaned/
├── sql/
│   ├── schema.sql
│   ├── data_loading.sql
│   └── business_analysis.sql
├── python/
│   └── sales_analysis.ipynb
├── excel/
│   └── sales_analysis.xlsx
├── powerbi/
│   ├── measures.dax
│   ├── power_query.m
│   ├── data_model.md
│   ├── dashboard_spec.md
│   └── implementation_guide.md
├── reports/
│   ├── data_dictionary.md
│   ├── data_quality_report.md
│   ├── kpi_definitions.md
│   ├── business_insights.md
│   ├── interview_questions.md
│   └── resume_project_description.md
├── screenshots/
├── scripts/
├── qa/
├── README.md
├── requirements.txt
└── .gitignore
```

## How to Run

### Python

```bash
pip install -r requirements.txt
cd python
jupyter notebook sales_analysis.ipynb
```

### MySQL

1. Run `sql/schema.sql`.
2. Update local paths in `sql/data_loading.sql`.
3. Load the cleaned CSVs.
4. Run `sql/business_analysis.sql`.

### Excel

Open `excel/sales_analysis.xlsx`. KPI and analysis tables are already populated; formula examples are included for interview demonstration.

### Power BI

Open Power BI Desktop, load the cleaned CSVs, create the model in `powerbi/data_model.md`, paste measures from `powerbi/measures.dax`, and build pages from `powerbi/dashboard_spec.md`.

## Dashboard Screenshots

These PNGs are **Power BI-style design previews generated from the actual analytical data**, not screenshots of a native `.pbix` report.

- `screenshots/01_executive_overview.png`
- `screenshots/02_sales_performance.png`
- `screenshots/03_product_performance.png`
- `screenshots/04_regional_performance.png`
- `screenshots/05_customer_analytics.png`
- `screenshots/06_channel_performance.png`

## Skills Demonstrated

Data cleaning, data validation, SQL, joins, CTEs, window functions, Pandas, NumPy, EDA, KPI design, statistical reasoning, business segmentation, Excel reporting, DAX, Power BI modeling, visualization and business storytelling.

## Limitations

- The data is synthetic.
- Cost is modeled as a simplified unit-cost estimate and does not include freight, marketing, tax or operating overhead.
- Returns/cancellations are retained for status analysis but not modeled through a full refund ledger.
- Power BI `.pbix` execution cannot be performed in this environment; the implementation pack is provided instead.
- Excel-native PivotTable caches are not generated by the available workbook API, so pivot-style analysis tables are provided.

## Future Improvements

Add a proper returns/refunds fact table, shipping and marketing costs, fiscal calendars, automated database refresh, a fuller RFM framework and a local Power BI build with live measure validation.

## QA

The `qa/` folder includes 25-query SQL execution QA on a 12,000-row SQLite compatibility sample, full-fact SQL scalar KPI validation, cross-validation, and data/model checks.
