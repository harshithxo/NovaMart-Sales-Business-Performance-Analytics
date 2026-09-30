# Power BI Data Model

## Model

Use a star-style semantic model:

- **Fact:** Orders
- **Dimensions:** Customers, Products, Regions, Salespeople, Channels, Date

## Relationships

| From | To | Cardinality | Cross-filter |
|---|---|---|---|
| Customers[Customer_ID] | Orders[Customer_ID] | 1:* | Single |
| Products[Product_ID] | Orders[Product_ID] | 1:* | Single |
| Regions[Region_ID] | Orders[Region_ID] | 1:* | Single |
| Salespeople[Salesperson_ID] | Orders[Salesperson_ID] | 1:* | Single |
| Channels[Channel_ID] | Orders[Channel_ID] | 1:* | Single |
| Date[Date] | Orders[Order_Date] | 1:* | Single |

## Date table

Create a calendar table covering 2025-01-01 through 2025-12-31 with Year, Month Number, Month Name, Quarter, and Year-Month columns. Mark it as the model date table.

## Design notes

- Core measures filter `Orders[Order_Status]` to `Completed`.
- Geography drill-down: Region → State → City.
- Product drill-down: Category → Subcategory → Product.
- Avoid bi-directional relationships unless a specific business requirement needs one.
