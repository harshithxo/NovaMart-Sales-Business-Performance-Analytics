# Power BI Dashboard Specification

This repository contains the DAX, Power Query M, data-model definition and visual specifications needed to recreate the dashboard in Power BI Desktop. A native `.pbix` binary is **not** included because Power BI Desktop is not available in the build environment. No fake `.pbix` has been created.

## Global design

- Canvas: 16:9
- Background: light neutral
- Typography: Segoe UI / default Power BI font
- KPI cards at the top of each page
- Use restrained borders and whitespace
- Prefer line and bar/column charts; avoid unnecessary pie charts
- Global slicers: Date, Region, Category, Channel, Customer Segment where relevant

## Page 1 – Executive Overview

**KPI cards:** Revenue, Profit, Profit Margin %, Orders, Customers, Units, AOV

**Visuals:** Monthly Revenue Trend; Monthly Profit Trend; Revenue by Region; Profit by Category; Revenue by Channel; Top 10 Products.

## Page 2 – Sales Performance

KPI: Revenue, Profit, Orders, AOV, Revenue Growth %, Profit Growth %.
Visuals: Revenue/Profit trend, Order trend, Monthly Growth, Quarterly performance. Enable Year → Quarter → Month drill-down.

## Page 3 – Product Performance

KPI: Revenue, Profit, Margin, Units. Visuals: Top products, category/subcategory comparison, scatter or matrix for revenue vs margin. Detailed table with Product, Category, Revenue, Cost, Profit, Margin %, Quantity.

## Page 4 – Regional Performance

KPI: Revenue, Profit, Orders, Customers, AOV, Growth. Visuals: revenue/profit by region, margin by region, matrix with Region → State → City.

## Page 5 – Customer Analytics

KPI: Customers, New Customers, Repeat Customers, Revenue per Customer, Repeat Customer Rate. Visuals: segment revenue, revenue/customer, top customers table, customer contribution.

## Page 6 – Channel Performance

Compare Online, Retail Store, Marketplace, Corporate on revenue, profit, margin, orders, AOV and growth. Show trade-offs, not a universal winner.

## Tooltips

Create tooltips for Product and Region pages showing Revenue, Profit, Margin %, Orders, Units and AOV.
