# KPI Definitions

All core KPIs use **completed orders only**. Returned and cancelled orders remain in the raw/cleaned Orders table for lifecycle analysis but are excluded from the core sales-performance fact used for management KPIs.

| KPI | Definition |
|---|---|
| Revenue | Quantity × Unit Price × (1 - Discount) |
| Cost | Quantity × Unit Cost |
| Profit | Revenue - Cost |
| Profit Margin | Profit / Revenue × 100 |
| Average Order Value | Revenue / Number of completed orders |
| Revenue Growth | (Current Period Revenue - Previous Period Revenue) / Previous Period Revenue × 100 |
| Repeat Customer Rate | Customers with more than one completed order / Total completed-order customers × 100 |
| Units Sold | Sum of Quantity for completed orders |

### Customer Segmentation

Behavior segments are derived from completed-order history rather than copied from the raw customer master:

- **High Value:** Revenue at or above the 75th percentile and at least 3 completed orders.
- **Loyal:** At least 5 completed orders but does not meet the High Value rule.
- **Regular:** 3–4 completed orders but does not meet the prior rules.
- **Occasional:** Exactly 2 completed orders.
- **Low Value:** Exactly 1 completed order (customers with no completed order, if any, also fall here for reporting continuity).

### Final Project KPI Values

- Revenue: ₹924,577,392.41
- Cost: ₹642,467,270.00
- Profit: ₹282,110,122.41
- Profit Margin: 30.51%
- Orders: 74,478
- Customers: 7,363
- Units Sold: 130,073
- Average Order Value: ₹12,414.10
- Repeat Customers: 7,001
- Repeat Customer Rate: 95.08%
