# Data Quality Report

## Scope

The raw synthetic dataset was intentionally seeded with manageable issues to demonstrate analyst-style detection, investigation, correction and validation.

| Check | Raw count / baseline | Result | Action |
|---|---:|---:|---|
| Raw order rows | 80,340 | 80,340 | Source rows loaded |
| Duplicate Order_IDs | 340 | 0 | Deduplicated on Order_ID, retained first occurrence |
| Missing Customer_ID | 415 | 0 | Dropped because customer linkage is required for customer analysis |
| Invalid Product_ID | 99 | 0 | Dropped because product key does not exist in product master |
| Non-positive Quantity | 180 | 0 | Dropped because order lines must contain positive units |
| Final cleaned order rows | 80,340 | 79,298 | After deduplication, key validation, numeric parsing and positive-value checks |

## Additional validation

- Numeric fields were parsed with coercion and then validated for positive price and quantity plus discounts between 0% and 30%.
- `Revenue`, `Cost` and `Profit` were recalculated from their source components in the cleaning pipeline rather than trusting raw derived values.
- Foreign-key membership was checked against Customer, Product, Region, Salesperson and Channel dimensions.
- Text fields were trimmed and category/status/payment values normalized for consistent grouping.
- Age missingness in the customer master was retained as a source-quality flag; the analytical segment logic does not depend on age.

## Outliers

Outliers in revenue, quantity and order value were inspected using percentile/IQR views. High-value transactions were **not** automatically deleted because they can represent valid business events. The notebook documents extreme observations and keeps them in the cleaned data when keys and financial logic are valid.
