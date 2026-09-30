# NovaMart Sales & Business Performance Analytics - Final Project Report

## Project Completed

Built a GitHub-ready Data Analyst portfolio project for the fictional company **NovaMart**, covering the full workflow from raw synthetic retail transactions through cleaning, validation, SQL analysis, Python EDA, Excel reporting, Power BI design, DAX documentation and business storytelling.

## Tools Used

Python, Pandas, NumPy, Matplotlib, Seaborn, Jupyter Notebook, MySQL 8.0 syntax, Microsoft Excel, Power BI, DAX, Power Query M, Git/GitHub.

## Dataset

| Layer | Size |
|---|---:|
| Raw Orders | 80,340 rows |
| Cleaned Orders | 79,298 rows |
| Completed analytical fact | 74,478 rows |
| Customers | 7,500 |
| Products | 72 |
| Regions | 20 |
| Salespeople | 30 |
| Channels | 4 |

The dataset is synthetic, uses fixed seed `20260930`, and intentionally contains manageable data-quality defects for portfolio demonstration.

## Key KPIs

| KPI | Final value |
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

## Key Findings

1. October 2025 was the strongest revenue month at **₹96.998M**, materially above the monthly average in the dataset.
2. **Central** had the lowest regional margin at **28.3%**, while **West** had the highest regional margin at **32.1%**.
3. **NovaBook Pro 16** led product revenue at **₹84.769M** while carrying a comparatively low **20.1% margin**, creating a high-revenue/low-margin review case.
4. **SmartView 55 TV** generated the highest absolute product profit at **₹20.118M** with a **32.5% margin**.
5. **Electronics** was the largest revenue category at **₹412.039M**, while Fashion had the highest category margin at **42.4%**.
6. **Online** generated the most revenue at **₹389.835M**; Retail Store showed the highest channel margin at **35.5%**. The project presents these as trade-offs rather than a universal channel ranking.
7. High Value customers contributed the most revenue per customer, averaging about **₹298K** per customer in the segment.
8. The final month declined **12.3% month over month** from the previous month, which is flagged for continued monitoring rather than treated as proof of a durable trend.

See `business_insights.md` for the complete Finding → Evidence → Business Implication analysis and recommendations.

## Resume Version

- Cleaned and validated a synthetic **80,340-row** retail transaction dataset using Pandas, handling duplicates, missing keys, inconsistent text, invalid quantities and data-type issues before recalculating financial fields.
- Analyzed **74,478 completed orders** with MySQL, Python and Excel, and designed a six-page Power BI dashboard covering revenue, profit, margins, customers, products, regions and channels.
- Translated KPI and segmentation analysis into **12 evidence-based business insights**, identifying high-revenue/low-margin products, regional margin differences, channel trade-offs and customer contribution patterns.

## Interview Version (60-90 seconds)

"I built a Sales and Business Performance Analytics project for a fictional multi-channel retailer called NovaMart. I created about 80,000 synthetic raw order records with realistic Indian regions, products, customers and sales channels, and intentionally included manageable data-quality issues such as duplicates, missing keys, inconsistent text and invalid quantities. I cleaned and validated the data with Pandas, then built a MySQL schema and 25 business-analysis queries using joins, CTEs and window functions. In Python I performed KPI analysis, trend analysis, product, regional, customer and channel analysis, and outlier checks. I also created an Excel reporting workbook and a six-page Power BI dashboard design with DAX measures for revenue, profit, margin, growth and repeat customers. The final completed-order fact has 74,478 rows, ₹924.6 million in revenue and ₹282.1 million in profit. The main analytical lesson was that high revenue does not always mean high margin, so I used the data to identify products and regions that deserve pricing, discount and mix investigation. I also cross-validated the headline KPIs between Python and SQL and documented the limitations of the synthetic dataset." 

## Implementation Limitations

- The dataset is synthetic and should be described that way in interviews and on GitHub.
- A native Power BI `.pbix` cannot be generated or executed in this environment because Power BI Desktop is unavailable. The project therefore includes DAX, Power Query, model documentation, page specifications, implementation steps and dashboard design previews, without pretending that a PBIX was produced.
- The workbook uses pivot-style summary tables rather than Excel-native PivotTable caches because the available workbook API cannot create those caches.
- SQL is written for MySQL 8.0. A local SQLite compatibility test covers all 25 query shapes on a 12,000-row validation sample, while the seven headline KPI scalars were separately checked against the full cleaned fact.
