# Interview Questions & Answers

## SQL

1. **Explain the most complex SQL query you wrote.**
   - I used a multi-CTE query to compare monthly revenue with the previous month using `LAG()`, then calculated growth and ranked the strongest changes. The query separates aggregation from comparison, which makes the business logic easier to read and validate.

2. **Why did you use a CTE?**
   - I used CTEs when an intermediate business concept needed a name, such as monthly revenue or repeat-customer counts. This reduced nested subqueries and made the logic easier to test.

3. **Where did you use a window function?**
   - I used `LAG()` for month-over-month revenue and profit growth and `ROW_NUMBER()` for top-product and top-customer ranking.

4. **How did you calculate revenue growth?**
   - I aggregated revenue by calendar month, used `LAG(Revenue)` to get prior-month revenue, and calculated `(Current - Previous) / Previous * 100`.

5. **How would you optimize the query?**
   - I would index foreign keys and `Order_Date`, analyze the execution plan, reduce repeated scans by using clearly defined CTEs or summary tables where appropriate, and filter completed orders early when that is the business scope.

6. **How did you prevent duplicate rows after joins?**
   - I validated key uniqueness in dimension tables and kept `Order_ID` unique in the cleaned fact. I also compared row counts before and after joins as part of QA.

7. **How did you identify high-revenue, low-margin products?**
   - I aggregated revenue and profit by product, calculated margin as profit divided by revenue, then filtered to products above the 75th revenue percentile and sorted by margin.

8. **Why did you use conditional aggregation?**
   - It lets one query compute metrics such as completed orders, returned orders and cancelled orders side by side without separate queries.

9. **How did you calculate repeat-customer rate in SQL?**
   - I counted completed orders per customer, counted customers with order counts greater than one, and divided by the total number of completed-order customers.

10. **What is one important SQL validation you performed?**
   - I reconciled the SQL total revenue, profit, order count and customer count against the Python analytical layer.

## Python / Pandas

11. **Why did you use Pandas?**
   - The project is tabular business data, so Pandas is a practical tool for loading CSVs, cleaning values, joining dimensions, grouping metrics and producing analysis-ready datasets.

12. **How did you handle missing values?**
   - I treated missing values based on business importance. Missing Customer_ID was a critical linkage problem and those order rows were excluded from the analytical fact. Missing customer age was retained as source-quality missingness because it was not needed for the core KPIs.

13. **How did you handle duplicates?**
   - I checked duplicate `Order_ID` values and removed duplicate records while keeping the first occurrence.

14. **How did you handle inconsistent categories?**
   - I stripped whitespace and normalized capitalization, then mapped known category variants to the standard business labels.

15. **How did you validate the financial columns?**
   - I recomputed Revenue, Cost and Profit from Quantity, Unit_Price, Discount and Unit_Cost instead of trusting the raw derived fields.

16. **How did you identify outliers?**
   - I used percentile/IQR views for quantity, revenue and order value and then investigated whether extreme values were valid business events before deciding to keep them.

17. **Why did you choose line charts for monthly trends?**
   - Time-series changes are easier to read with a line chart because the viewer can see direction, seasonality and month-to-month movement.

18. **Why use bar charts for category or region comparisons?**
   - Bars are effective for comparing discrete groups and ranking values without forcing the viewer to compare angles, as with a pie chart.

19. **How did you avoid fabricating insights?**
   - The insight file is generated from grouped outputs of the final dataset. Each statement includes a numerical evidence line and a business implication that is explicitly framed as an investigation or planning action rather than a causal claim.

20. **What was the biggest cleaning issue?**
   - Duplicate Order_IDs were intentionally injected into the raw data, alongside missing customer keys and invalid quantities. The pipeline detects them before creating the final fact table.

## Power BI / DAX

21. **Explain your data model.**
   - I use a star-style model with `Orders` as the fact table and Customers, Products, Regions, Salespeople, Channels and a Date dimension as supporting dimensions. Relationships flow from dimensions to the fact.

22. **What relationships did you create?**
   - Customers[Customer_ID] to Orders[Customer_ID], Products[Product_ID] to Orders[Product_ID], Regions[Region_ID] to Orders[Region_ID], Salespeople[Salesperson_ID] to Orders[Salesperson_ID], Channels[Channel_ID] to Orders[Channel_ID], and Date[Date] to Orders[Order_Date].

23. **Measure vs calculated column?**
   - I used measures for aggregations such as Total Revenue and Profit Margin because they should respond to filter context. I use columns for descriptive fields and row-level attributes.

24. **Explain Total Revenue in DAX.**
   - `CALCULATE(SUM(Orders[Revenue]), Orders[Order_Status] = "Completed")` keeps the completed-order business rule inside the measure.

25. **How did you calculate Revenue Growth %?**
   - I calculated current-period revenue, previous-period revenue using `DATEADD`, and then divided the difference by previous-period revenue with `DIVIDE` to avoid divide-by-zero errors.

26. **Why use slicers?**
   - They let management change the analytical context by date, region, category, channel and customer segment without creating separate pages for every view.

27. **How did you design the dashboard?**
   - The first page is a management overview, followed by focused pages for sales, products, regions, customers and channels. Each page limits the number of visuals and prioritizes KPIs, trends and comparisons.

28. **How would you add drill-down?**
   - For geographic analysis I use Region → State → City. For product analysis I use Category → Subcategory → Product.

29. **How did you validate Power BI KPIs?**
   - I used the same completed-order inclusion rule and KPI definitions as Python and SQL, then created a cross-validation table containing the expected values. In this environment, Power BI Desktop itself was not available for live `.pbix` execution, so the DAX measures are documented and logic-reviewed rather than falsely marked as executed.

30. **What would you improve next?**
   - I would add a proper calendar table with fiscal periods, automate refresh from a database, and incorporate returns/refunds at a more detailed level so management can distinguish gross sales from net sales after returns.

## Business / Communication

31. **What was the most important finding?**
   - A useful management-level finding is the gap between top-line and margin performance: the dataset contains products and regions that generate substantial revenue but have weaker margins. That makes pricing, discounting and mix important follow-up areas.

32. **Which KPI matters most?**
   - There is no single KPI that explains the entire business. Revenue shows scale, profit and margin show economics, orders and units show activity, and customer metrics show contribution and retention.

33. **What would you investigate next?**
   - I would investigate the drivers of the lowest-margin region and high-revenue/low-margin products by channel, discount level and product mix.

34. **What limitations exist?**
   - The data is synthetic, so it cannot prove real-world company behavior. It also uses a simplified cost structure and excludes detailed refund logistics, shipping costs and marketing spend.

35. **How would you explain the project to a non-technical manager?**
   - I would say: “I took raw sales data, cleaned and validated it, calculated consistent sales and profitability KPIs, and built dashboards that show where revenue is coming from, where profit is stronger or weaker, and which customer and channel patterns deserve attention.”
