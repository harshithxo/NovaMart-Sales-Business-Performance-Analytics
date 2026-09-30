#!/usr/bin/env python3
"""Clean NovaMart raw CSVs and build the analytical fact layer."""
from pathlib import Path
import numpy as np
import pandas as pd
from pandas.api.types import is_datetime64_any_dtype

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data/raw"
OUT = ROOT / "data/cleaned"
OUT.mkdir(parents=True, exist_ok=True)

# Load dimension masters first so transaction foreign keys can be validated.
customers = pd.read_csv(RAW/'customers.csv', dtype=str)
products = pd.read_csv(RAW/'products.csv', dtype=str)
regions = pd.read_csv(RAW/'regions.csv', dtype=str)
salespeople = pd.read_csv(RAW/'salespeople.csv', dtype=str)
channels = pd.read_csv(RAW/'channels.csv', dtype=str)

# Clean customer master. Age is intentionally left missing where the raw source was missing.
customers_clean = customers.copy()
for c in ['Customer_ID','Customer_Name','Gender','City','State','Region','Customer_Segment']:
    customers_clean[c] = customers_clean[c].astype('string').str.strip()
customers_clean['Customer_Segment'] = customers_clean['Customer_Segment'].str.title()
customers_clean['Age'] = pd.to_numeric(customers_clean['Age'], errors='coerce')
customers_clean['Registration_Date'] = pd.to_datetime(customers_clean['Registration_Date'], errors='coerce')

# Clean product master.
products_clean = products.copy()
for c in ['Product_ID','Product_Name','Category','Subcategory','Brand']:
    products_clean[c] = products_clean[c].astype('string').str.strip()
products_clean['Category'] = products_clean['Category'].str.replace(r'(?i)^home appliances$','Home Appliances',regex=True)
products_clean['Category'] = products_clean['Category'].str.replace(r'(?i)^sports & outdoors$','Sports & Outdoors',regex=True)
products_clean['Unit_Cost'] = pd.to_numeric(products_clean['Unit_Cost'], errors='coerce')
products_clean['Selling_Price'] = pd.to_numeric(products_clean['Selling_Price'], errors='coerce')

# Clean remaining dimensions.
regions_clean = regions.copy()
for c in regions_clean.columns:
    regions_clean[c] = regions_clean[c].astype('string').str.strip()
regions_clean['Region_Name'] = regions_clean['Region_Name'].str.title()
salespeople_clean = salespeople.copy()
for c in salespeople_clean.columns:
    salespeople_clean[c] = salespeople_clean[c].astype('string').str.strip()
channels_clean = channels.copy()
for c in channels_clean.columns:
    channels_clean[c] = channels_clean[c].astype('string').str.strip()

# Load and clean transaction data.
orders = pd.read_csv(RAW/'orders.csv', dtype=str)
initial_rows = len(orders)
log = [('Raw order rows', initial_rows, initial_rows, 'Source rows loaded')]
for c in ['Order_ID','Customer_ID','Product_ID','Region_ID','Salesperson_ID','Channel_ID','Payment_Method','Order_Status']:
    orders[c] = orders[c].astype('string').str.strip()
orders['Order_Status'] = orders['Order_Status'].str.title()
orders['Payment_Method'] = orders['Payment_Method'].str.title()
for c in ['Quantity','Unit_Price','Revenue','Cost','Profit']:
    orders[c] = pd.to_numeric(orders[c].astype('string').str.strip(), errors='coerce')
orders['Discount'] = orders['Discount'].astype('string').str.replace('%','',regex=False)
orders['Discount'] = pd.to_numeric(orders['Discount'], errors='coerce')
orders['Discount'] = np.where(orders['Discount'] > 1, orders['Discount']/100, orders['Discount'])
orders['Order_Date'] = pd.to_datetime(orders['Order_Date'], errors='coerce')

dups = int(orders.duplicated('Order_ID').sum())
orders = orders.drop_duplicates('Order_ID', keep='first')
log.append(('Duplicate Order_ID rows', dups, 0, 'Deduplicated by Order_ID, retained first occurrence'))
missing_customer = int(orders['Customer_ID'].isna().sum())
orders = orders.dropna(subset=['Customer_ID'])
log.append(('Missing Customer_ID', missing_customer, 0, 'Dropped rows because customer linkage is required'))
invalid_product = int((~orders['Product_ID'].isin(products_clean['Product_ID'])).sum())
orders = orders[orders['Product_ID'].isin(products_clean['Product_ID'])].copy()
log.append(('Invalid Product_ID', invalid_product, 0, 'Dropped rows with no product master match'))
invalid_quantity = int((orders['Quantity'] <= 0).sum())
orders = orders[orders['Quantity'] > 0].copy()
log.append(('Non-positive Quantity', invalid_quantity, 0, 'Dropped rows because order quantity must be positive'))
orders = orders[orders['Unit_Price'] > 0].copy()
orders = orders[orders['Discount'].between(0, 0.30)].copy()
orders = orders[orders['Order_Date'].notna()].copy()

prod_cost_map = products_clean.set_index('Product_ID')['Unit_Cost'].to_dict()
orders['Unit_Cost'] = orders['Product_ID'].map(prod_cost_map)
orders['Revenue'] = (orders['Quantity'] * orders['Unit_Price'] * (1 - orders['Discount'])).round(2)
orders['Cost'] = (orders['Quantity'] * orders['Unit_Cost']).round(2)
orders['Profit'] = (orders['Revenue'] - orders['Cost']).round(2)

# Referential integrity checks.
assert orders['Customer_ID'].isin(customers_clean['Customer_ID']).all()
assert orders['Product_ID'].isin(products_clean['Product_ID']).all()
assert orders['Region_ID'].isin(regions_clean['Region_ID']).all()
assert orders['Salesperson_ID'].isin(salespeople_clean['Salesperson_ID']).all()
assert orders['Channel_ID'].isin(channels_clean['Channel_ID']).all()

orders_clean = orders[['Order_ID','Order_Date','Customer_ID','Product_ID','Region_ID','Salesperson_ID','Channel_ID','Quantity','Unit_Price','Discount','Revenue','Unit_Cost','Cost','Profit','Payment_Method','Order_Status']].copy()

# Business segmentation is derived only from completed-order behavior, then mapped to the customer master.
completed = orders_clean[orders_clean['Order_Status'] == 'Completed'].copy()
agg = completed.groupby('Customer_ID').agg(Order_Count=('Order_ID','nunique'), Revenue=('Revenue','sum')).reindex(customers_clean['Customer_ID']).fillna({'Order_Count':0,'Revenue':0})
q75 = float(agg['Revenue'].quantile(0.75))
def segment(row):
    if row.Revenue >= q75 and row.Order_Count >= 3:
        return 'High Value'
    if row.Order_Count >= 5:
        return 'Loyal'
    if row.Order_Count >= 3:
        return 'Regular'
    if row.Order_Count == 2:
        return 'Occasional'
    return 'Low Value'
segment_map = agg.apply(segment, axis=1)
customers_clean['Customer_Segment'] = customers_clean['Customer_ID'].map(segment_map).fillna('Low Value')

# Save cleaned tables.
def save_df(name, df):
    dfx = df.copy()
    for c in dfx.columns:
        if is_datetime64_any_dtype(dfx[c]):
            dfx[c] = dfx[c].dt.strftime('%Y-%m-%d')
    dfx.to_csv(OUT/f'{name}_clean.csv', index=False)

save_df('orders', orders_clean)
save_df('customers', customers_clean)
save_df('products', products_clean)
save_df('regions', regions_clean)
save_df('salespeople', salespeople_clean)
save_df('channels', channels_clean)

# Denormalized completed-order analytical fact for Python/Power BI/Excel reporting.
analytics = completed.merge(customers_clean[['Customer_ID','Customer_Name','Gender','Age','City','State','Customer_Segment']], on='Customer_ID', how='left') \
    .merge(products_clean[['Product_ID','Product_Name','Category','Subcategory','Brand']], on='Product_ID', how='left') \
    .merge(regions_clean[['Region_ID','Region_Name','State','City']], on='Region_ID', how='left', suffixes=('','_Region')) \
    .merge(salespeople_clean[['Salesperson_ID','Salesperson_Name','Team']], on='Salesperson_ID', how='left') \
    .merge(channels_clean[['Channel_ID','Channel_Name']], on='Channel_ID', how='left')
analytics['Year'] = analytics['Order_Date'].dt.year
analytics['Month_Number'] = analytics['Order_Date'].dt.month
analytics['Month'] = analytics['Order_Date'].dt.strftime('%b')
analytics['Quarter'] = 'Q' + analytics['Order_Date'].dt.quarter.astype(str)
analytics['Order_Month'] = analytics['Order_Date'].dt.to_period('M').astype(str)
analytics['Profit_Margin'] = np.where(analytics['Revenue'] != 0, analytics['Profit']/analytics['Revenue'], 0)
analytics.to_csv(OUT/'analytics_sales.csv', index=False)

log.append(('Final cleaned order rows', initial_rows, len(orders_clean), 'After duplicate removal, key validation, numeric parsing and business-rule checks'))
pd.DataFrame(log, columns=['Check','Before','After/Count','Action']).to_csv(OUT/'cleaning_log.csv', index=False)
print(f'Cleaned orders: {len(orders_clean):,}; completed analytical rows: {len(analytics):,}')
