-- 25 business-analysis queries for NovaMart
USE novamart_analytics;

-- Q01: Total revenue
SELECT ROUND(SUM(Revenue),2) AS Total_Revenue FROM Orders WHERE Order_Status = 'Completed';

-- Q02: Total profit
SELECT ROUND(SUM(Profit),2) AS Total_Profit FROM Orders WHERE Order_Status = 'Completed';

-- Q03: Overall profit margin
SELECT ROUND(SUM(Profit)/NULLIF(SUM(Revenue),0)*100,2) AS Profit_Margin_Pct FROM Orders WHERE Order_Status = 'Completed';

-- Q04: Monthly revenue
SELECT DATE_FORMAT(Order_Date,'%Y-%m') AS Order_Month, ROUND(SUM(Revenue),2) AS Revenue FROM Orders WHERE Order_Status='Completed' GROUP BY DATE_FORMAT(Order_Date,'%Y-%m') ORDER BY Order_Month;

-- Q05: Monthly profit
SELECT DATE_FORMAT(Order_Date,'%Y-%m') AS Order_Month, ROUND(SUM(Profit),2) AS Profit FROM Orders WHERE Order_Status='Completed' GROUP BY DATE_FORMAT(Order_Date,'%Y-%m') ORDER BY Order_Month;

-- Q06: Revenue growth
WITH monthly AS (SELECT DATE_FORMAT(Order_Date,'%Y-%m') AS Order_Month, SUM(Revenue) AS Revenue FROM Orders WHERE Order_Status='Completed' GROUP BY DATE_FORMAT(Order_Date,'%Y-%m')) SELECT Order_Month, ROUND((Revenue-LAG(Revenue) OVER (ORDER BY Order_Month))/NULLIF(LAG(Revenue) OVER (ORDER BY Order_Month),0)*100,2) AS Revenue_Growth_Pct FROM monthly ORDER BY Order_Month;

-- Q07: Top products by revenue
SELECT p.Product_ID,p.Product_Name,ROUND(SUM(o.Revenue),2) AS Revenue FROM Orders o JOIN Products p ON o.Product_ID=p.Product_ID WHERE o.Order_Status='Completed' GROUP BY p.Product_ID,p.Product_Name ORDER BY Revenue DESC LIMIT 10;

-- Q08: Top products by profit
SELECT p.Product_ID,p.Product_Name,ROUND(SUM(o.Profit),2) AS Profit FROM Orders o JOIN Products p ON o.Product_ID=p.Product_ID WHERE o.Order_Status='Completed' GROUP BY p.Product_ID,p.Product_Name ORDER BY Profit DESC LIMIT 10;

-- Q09: Lowest-margin products
SELECT p.Product_ID,p.Product_Name,ROUND(SUM(o.Revenue),2) AS Revenue,ROUND(SUM(o.Profit)/NULLIF(SUM(o.Revenue),0)*100,2) AS Margin_Pct FROM Orders o JOIN Products p ON o.Product_ID=p.Product_ID WHERE o.Order_Status='Completed' GROUP BY p.Product_ID,p.Product_Name HAVING SUM(o.Revenue)>0 ORDER BY Margin_Pct ASC LIMIT 10;

-- Q10: Category performance
SELECT p.Category,ROUND(SUM(o.Revenue),2) AS Revenue,ROUND(SUM(o.Profit),2) AS Profit,ROUND(SUM(o.Profit)/NULLIF(SUM(o.Revenue),0)*100,2) AS Margin_Pct FROM Orders o JOIN Products p ON o.Product_ID=p.Product_ID WHERE o.Order_Status='Completed' GROUP BY p.Category ORDER BY Revenue DESC;

-- Q11: Subcategory performance
SELECT p.Category,p.Subcategory,ROUND(SUM(o.Revenue),2) AS Revenue,ROUND(SUM(o.Profit),2) AS Profit,ROUND(SUM(o.Profit)/NULLIF(SUM(o.Revenue),0)*100,2) AS Margin_Pct FROM Orders o JOIN Products p ON o.Product_ID=p.Product_ID WHERE o.Order_Status='Completed' GROUP BY p.Category,p.Subcategory ORDER BY Revenue DESC;

-- Q12: Regional revenue
SELECT r.Region_Name,ROUND(SUM(o.Revenue),2) AS Revenue FROM Orders o JOIN Regions r ON o.Region_ID=r.Region_ID WHERE o.Order_Status='Completed' GROUP BY r.Region_Name ORDER BY Revenue DESC;

-- Q13: Regional profit
SELECT r.Region_Name,ROUND(SUM(o.Profit),2) AS Profit FROM Orders o JOIN Regions r ON o.Region_ID=r.Region_ID WHERE o.Order_Status='Completed' GROUP BY r.Region_Name ORDER BY Profit DESC;

-- Q14: Regional growth
WITH region_month AS (SELECT r.Region_Name,DATE_FORMAT(o.Order_Date,'%Y-%m') AS Order_Month,SUM(o.Revenue) AS Revenue FROM Orders o JOIN Regions r ON o.Region_ID=r.Region_ID WHERE o.Order_Status='Completed' GROUP BY r.Region_Name,DATE_FORMAT(o.Order_Date,'%Y-%m')), ranked AS (SELECT Region_Name,Order_Month,Revenue,LAG(Revenue) OVER (PARTITION BY Region_Name ORDER BY Order_Month) AS Prev_Revenue FROM region_month) SELECT Region_Name,Order_Month,ROUND((Revenue-Prev_Revenue)/NULLIF(Prev_Revenue,0)*100,2) AS Revenue_Growth_Pct FROM ranked ORDER BY Region_Name,Order_Month;

-- Q15: Top customers
SELECT c.Customer_ID,c.Customer_Name,ROUND(SUM(o.Revenue),2) AS Revenue,COUNT(DISTINCT o.Order_ID) AS Orders FROM Orders o JOIN Customers c ON o.Customer_ID=c.Customer_ID WHERE o.Order_Status='Completed' GROUP BY c.Customer_ID,c.Customer_Name ORDER BY Revenue DESC LIMIT 10;

-- Q16: Customer order frequency
SELECT Order_Count,COUNT(*) AS Customers FROM (SELECT Customer_ID,COUNT(DISTINCT Order_ID) AS Order_Count FROM Orders WHERE Order_Status='Completed' GROUP BY Customer_ID) x GROUP BY Order_Count ORDER BY Order_Count;

-- Q17: Average order value
SELECT ROUND(SUM(Revenue)/COUNT(DISTINCT Order_ID),2) AS Average_Order_Value FROM Orders WHERE Order_Status='Completed';

-- Q18: Repeat customer rate
WITH customer_orders AS (SELECT Customer_ID,COUNT(DISTINCT Order_ID) AS Order_Count FROM Orders WHERE Order_Status='Completed' GROUP BY Customer_ID) SELECT ROUND(SUM(CASE WHEN Order_Count>1 THEN 1 ELSE 0 END)/COUNT(*)*100,2) AS Repeat_Customer_Rate_Pct FROM customer_orders;

-- Q19: Customer-segment performance
SELECT c.Customer_Segment,COUNT(DISTINCT o.Customer_ID) AS Customers,COUNT(DISTINCT o.Order_ID) AS Orders,ROUND(SUM(o.Revenue),2) AS Revenue,ROUND(SUM(o.Revenue)/COUNT(DISTINCT o.Customer_ID),2) AS Revenue_Per_Customer FROM Orders o JOIN Customers c ON o.Customer_ID=c.Customer_ID WHERE o.Order_Status='Completed' GROUP BY c.Customer_Segment ORDER BY Revenue DESC;

-- Q20: Channel performance
SELECT ch.Channel_Name,ROUND(SUM(o.Revenue),2) AS Revenue,COUNT(DISTINCT o.Order_ID) AS Orders,ROUND(SUM(o.Profit),2) AS Profit,ROUND(SUM(o.Profit)/NULLIF(SUM(o.Revenue),0)*100,2) AS Margin_Pct,ROUND(SUM(o.Revenue)/COUNT(DISTINCT o.Order_ID),2) AS AOV FROM Orders o JOIN Channels ch ON o.Channel_ID=ch.Channel_ID WHERE o.Order_Status='Completed' GROUP BY ch.Channel_Name ORDER BY Revenue DESC;

-- Q21: Channel profitability
SELECT ch.Channel_Name,ROUND(SUM(o.Profit),2) AS Profit,ROUND(SUM(o.Profit)/NULLIF(SUM(o.Revenue),0)*100,2) AS Margin_Pct FROM Orders o JOIN Channels ch ON o.Channel_ID=ch.Channel_ID WHERE o.Order_Status='Completed' GROUP BY ch.Channel_Name ORDER BY Profit DESC;

-- Q22: Salesperson performance
SELECT s.Salesperson_Name,s.Team,s.Region,COUNT(DISTINCT o.Order_ID) AS Orders,ROUND(SUM(o.Revenue),2) AS Revenue,ROUND(SUM(o.Profit),2) AS Profit FROM Orders o JOIN Salespeople s ON o.Salesperson_ID=s.Salesperson_ID WHERE o.Order_Status='Completed' GROUP BY s.Salesperson_ID,s.Salesperson_Name,s.Team,s.Region ORDER BY Revenue DESC;

-- Q23: High revenue, low margin products
WITH product_perf AS (SELECT p.Product_ID,p.Product_Name,SUM(o.Revenue) AS Revenue,SUM(o.Profit) AS Profit FROM Orders o JOIN Products p ON o.Product_ID=p.Product_ID WHERE o.Order_Status='Completed' GROUP BY p.Product_ID,p.Product_Name), thresholds AS (SELECT AVG(Revenue) AS Avg_Revenue FROM product_perf) SELECT Product_ID,Product_Name,ROUND(Revenue,2) AS Revenue,ROUND(Profit/NULLIF(Revenue,0)*100,2) AS Margin_Pct FROM product_perf,thresholds WHERE Revenue > Avg_Revenue AND Profit/NULLIF(Revenue,0) < (SELECT AVG(Profit/NULLIF(Revenue,0)) FROM product_perf) ORDER BY Revenue DESC;

-- Q24: Monthly sales trends
SELECT DATE_FORMAT(Order_Date,'%Y-%m') AS Order_Month,COUNT(DISTINCT Order_ID) AS Orders,SUM(Quantity) AS Units,ROUND(SUM(Revenue),2) AS Revenue,ROUND(SUM(Profit),2) AS Profit FROM Orders WHERE Order_Status='Completed' GROUP BY DATE_FORMAT(Order_Date,'%Y-%m') ORDER BY Order_Month;

-- Q25: Products with declining performance
WITH monthly_product AS (SELECT Product_ID,DATE_FORMAT(Order_Date,'%Y-%m') AS Order_Month,SUM(Revenue) AS Revenue FROM Orders WHERE Order_Status='Completed' GROUP BY Product_ID,DATE_FORMAT(Order_Date,'%Y-%m')), bounds AS (SELECT Product_ID,MIN(Order_Month) AS First_Month,MAX(Order_Month) AS Last_Month FROM monthly_product GROUP BY Product_ID), ranked AS (SELECT mp.Product_ID,mp.Order_Month,mp.Revenue,ROW_NUMBER() OVER(PARTITION BY mp.Product_ID ORDER BY mp.Order_Month DESC) AS rn FROM monthly_product mp), latest AS (SELECT Product_ID,MAX(CASE WHEN rn=1 THEN Revenue END) AS Latest_Revenue,MAX(CASE WHEN rn=2 THEN Revenue END) AS Prev_Revenue FROM ranked GROUP BY Product_ID) SELECT p.Product_ID,p.Product_Name,ROUND(Latest_Revenue,2) AS Latest_Month_Revenue,ROUND(Prev_Revenue,2) AS Previous_Month_Revenue,ROUND((Latest_Revenue-Prev_Revenue)/NULLIF(Prev_Revenue,0)*100,2) AS Growth_Pct FROM latest l JOIN Products p ON l.Product_ID=p.Product_ID WHERE Prev_Revenue IS NOT NULL AND Latest_Revenue < Prev_Revenue ORDER BY Growth_Pct ASC LIMIT 20;
