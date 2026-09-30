#!/usr/bin/env python3
"""Generate the reproducible NovaMart synthetic raw dataset."""
from pathlib import Path
import random
import numpy as np
import pandas as pd
from pandas.api.types import is_datetime64_any_dtype

ROOT = Path(__file__).resolve().parents[1]
SEED = 20260930
N_ORDERS = 80000
N_CUSTOMERS = 7500
rng = np.random.default_rng(SEED)
random.seed(SEED)
for p in [ROOT / "data/raw", ROOT / "data/cleaned"]:
    p.mkdir(parents=True, exist_ok=True)

# -----------------------------
# Dimension setup
# -----------------------------
locations = [
    ('R01','South','Telangana','Hyderabad'),('R02','South','Telangana','Warangal'),('R03','South','Andhra Pradesh','Vijayawada'),
    ('R04','South','Karnataka','Bengaluru'),('R05','South','Tamil Nadu','Chennai'),('R06','South','Kerala','Kochi'),
    ('R07','West','Maharashtra','Mumbai'),('R08','West','Maharashtra','Pune'),('R09','West','Gujarat','Ahmedabad'),
    ('R10','West','Rajasthan','Jaipur'),('R11','North','Delhi','New Delhi'),('R12','North','Uttar Pradesh','Lucknow'),
    ('R13','North','Haryana','Gurugram'),('R14','North','Punjab','Ludhiana'),('R15','East','West Bengal','Kolkata'),
    ('R16','East','Odisha','Bhubaneswar'),('R17','East','Bihar','Patna'),('R18','Central','Madhya Pradesh','Indore'),
    ('R19','Central','Chhattisgarh','Raipur'),('R20','Central','Madhya Pradesh','Bhopal'),
]
regions = pd.DataFrame(locations, columns=['Region_ID','Region_Name','State','City'])

channels = pd.DataFrame([
    ('CH01','Online'),('CH02','Retail Store'),('CH03','Marketplace'),('CH04','Corporate')
], columns=['Channel_ID','Channel_Name'])

teams = ['North Team','South Team','West Team','East Team','Central Team']
sp_names = [
    'Aarav Mehta','Ananya Rao','Arjun Reddy','Aditi Sharma','Rahul Verma','Neha Iyer','Vikram Singh','Priya Nair',
    'Rohit Kumar','Kavya Joshi','Sanjay Patil','Sneha Kapoor','Karan Malhotra','Pooja Shah','Nikhil Desai',
    'Meera Menon','Varun Gupta','Riya Bhat','Aditya Kulkarni','Ishita Sinha','Manish Yadav','Tanvi Rao',
    'Siddharth Jain','Diya Das','Rakesh Naidu','Shreya Pillai','Abhishek Roy','Nandini Rao','Harsh Vardhan','Simran Kaur'
]
sp_rows=[]
for i,name in enumerate(sp_names,1):
    region = ['North','South','West','East','Central'][(i-1)%5]
    sp_rows.append((f'SP{i:02d}', name, region, teams[(i-1)%5]))
salespeople = pd.DataFrame(sp_rows, columns=['Salesperson_ID','Salesperson_Name','Region','Team'])

product_catalog = [
    ('P001','NovaBook Air 14','Electronics','Laptops','NovaTech',48000,69999,1.15),
    ('P002','NovaBook Pro 16','Electronics','Laptops','NovaTech',64000,89999,0.90),
    ('P003','WorkMate 15 Laptop','Electronics','Laptops','WorkMate',39000,59999,1.00),
    ('P004','SmartView 43 TV','Electronics','Televisions','ViewMax',24000,38999,1.35),
    ('P005','SmartView 55 TV','Electronics','Televisions','ViewMax',32000,52999,1.10),
    ('P006','SoundPod Pro','Electronics','Audio','SoundPod',4500,7999,1.55),
    ('P007','SoundPod Mini','Electronics','Audio','SoundPod',1800,3299,2.20),
    ('P008','FitBand Active','Electronics','Wearables','NovaFit',1500,2999,2.30),
    ('P009','AirCool 1.5T AC','Home Appliances','Cooling','HomeEase',32000,48999,1.10),
    ('P010','BreezePlus Cooler','Home Appliances','Cooling','HomeEase',8500,13499,1.40),
    ('P011','CleanPro Vacuum','Home Appliances','Cleaning','CleanPro',6200,9999,1.65),
    ('P012','WashSmart 7kg Washer','Home Appliances','Laundry','WashSmart',21000,32999,1.00),
    ('P013','HeatWave Microwave','Home Appliances','Kitchen','HeatWave',7000,10999,1.35),
    ('P014','ChefMate Air Fryer','Home Appliances','Kitchen','ChefMate',4200,6999,1.80),
    ('P015','AutoBrew Coffee Maker','Home Appliances','Kitchen','ChefMate',3500,5999,1.55),
    ('P016','LoungeMax 3-Seater','Furniture','Living Room','CasaLiving',18000,29999,0.75),
    ('P017','ErgoFlex Office Chair','Furniture','Office','CasaLiving',6500,10999,1.45),
    ('P018','UrbanWood Study Desk','Furniture','Office','UrbanWood',7500,12499,1.00),
    ('P019','SleepWell Queen Mattress','Furniture','Bedroom','SleepWell',10500,16999,0.90),
    ('P020','NestHome Bedside Table','Furniture','Bedroom','NestHome',2500,4499,1.25),
    ('P021','Everyday Polo Shirt','Fashion','Men','UrbanWear',700,1299,2.30),
    ('P022','Classic Denim Jeans','Fashion','Men','UrbanWear',1100,1999,1.65),
    ('P023','Comfort Sneakers','Fashion','Footwear','Stride',1500,2999,1.80),
    ('P024','Active Joggers','Fashion','Sportswear','Stride',900,1699,1.55),
    ('P025','Everyday Kurta','Fashion','Women','EthnicCo',800,1499,1.40),
    ('P026','Aero Running Shoes','Fashion','Footwear','Stride',2200,3999,1.20),
    ('P027','SkinGlow Face Serum','Beauty','Skincare','GlowLab',650,1199,1.65),
    ('P028','SkinGlow Sunscreen','Beauty','Skincare','GlowLab',450,799,1.90),
    ('P029','FreshMist Body Spray','Beauty','Personal Care','FreshMist',300,599,1.85),
    ('P030','SilkTouch Shampoo','Beauty','Haircare','SilkTouch',240,499,2.00),
    ('P031','ProBlend Mixer','Home Appliances','Kitchen','ChefMate',2600,4499,1.70),
    ('P032','SmartScale Body Scale','Electronics','Wearables','NovaFit',1200,2299,1.85),
    ('P033','PowerBank 20K','Electronics','Accessories','ChargePro',1100,1999,2.00),
    ('P034','FastCharge Adapter','Electronics','Accessories','ChargePro',500,999,2.20),
    ('P035','UrbanLamp Desk Lamp','Furniture','Office','UrbanWood',900,1699,1.50),
    ('P036','Memory Foam Pillow','Furniture','Bedroom','SleepWell',550,999,1.80),
    ('P037','NutriGranola 1kg','Grocery','Pantry','NutriLife',330,549,2.10),
    ('P038','Organic Coffee 500g','Grocery','Pantry','BeanCraft',420,699,1.80),
    ('P039','Daily Olive Oil 1L','Grocery','Cooking','DailyFresh',520,799,1.70),
    ('P040','Premium Basmati 5kg','Grocery','Staples','HarvestGold',520,799,1.40),
    ('P041','GreenTea 100 Bags','Grocery','Beverages','WellLeaf',180,349,2.00),
    ('P042','Protein Oats 1kg','Grocery','Health','FitFuel',340,599,1.85),
    ('P043','Yoga Mat Pro','Sports & Outdoors','Fitness','FlexFit',650,1199,1.90),
    ('P044','Home Dumbbell Set','Sports & Outdoors','Fitness','FlexFit',1800,3299,1.10),
    ('P045','Cycling Helmet','Sports & Outdoors','Cycling','RideSafe',1200,2199,1.15),
    ('P046','Cricket Bat Club','Sports & Outdoors','Cricket','PlayPro',1900,3499,1.10),
    ('P047','Badminton Racket Pair','Sports & Outdoors','Racquet Sports','PlayPro',1400,2599,1.30),
    ('P048','SmartOffice Monitor 24','Electronics','Monitors','ViewMax',9000,14999,1.00),
    ('P049','NovaTab 10','Electronics','Tablets','NovaTech',15500,24999,1.35),
    ('P050','NovaPhone 5G','Electronics','Mobiles','NovaTech',13500,21999,1.70),
    ('P051','NovaPhone Max 5G','Electronics','Mobiles','NovaTech',20500,32999,1.25),
    ('P052','StreamCam 1080p','Electronics','Accessories','ViewMax',2600,4499,1.15),
    ('P053','Wireless Keyboard','Electronics','Accessories','WorkMate',900,1699,1.60),
    ('P054','Wireless Mouse','Electronics','Accessories','WorkMate',450,899,1.90),
    ('P055','Premium Office Bundle','Furniture','Office','CasaLiving',11200,17999,0.80),
    ('P056','Executive Office Desk','Furniture','Office','CasaLiving',14500,23999,0.70),
    ('P057','SmartKettle 1.5L','Home Appliances','Kitchen','HeatWave',1300,2299,1.75),
    ('P058','Induction Cooktop','Home Appliances','Kitchen','HeatWave',1600,2799,1.55),
    ('P059','Steam Iron Plus','Home Appliances','Laundry','CleanPro',1200,2199,1.40),
    ('P060','LED Study Lamp','Furniture','Office','UrbanWood',700,1299,1.70),
    ('P061','Travel Backpack 28L','Fashion','Bags','UrbanWear',900,1799,1.55),
    ('P062','Premium Handbag','Fashion','Bags','EthnicCo',1600,3199,1.00),
    ('P063','Analog Fitness Watch','Electronics','Wearables','NovaFit',900,1799,1.30),
    ('P064','Smart Speaker Mini','Electronics','Audio','SoundPod',2200,3999,1.40),
    ('P065','Smart Speaker Max','Electronics','Audio','SoundPod',4300,7499,1.00),
    ('P066','Electric Grill','Home Appliances','Kitchen','ChefMate',2400,4199,1.00),
    ('P067','Robot Floor Cleaner','Home Appliances','Cleaning','CleanPro',16800,26999,0.70),
    ('P068','Dining Table 4-Seater','Furniture','Dining','CasaLiving',14500,23999,0.65),
    ('P069','Dining Chair Pair','Furniture','Dining','CasaLiving',4800,7999,0.70),
    ('P070','Kids Study Chair','Furniture','Kids','CasaLiving',2800,4799,0.95),
    ('P071','Organic Honey 500g','Grocery','Pantry','NutriLife',260,499,1.80),
    ('P072','Almonds 500g','Grocery','Health','HarvestGold',400,699,1.65),
]
products = pd.DataFrame(product_catalog, columns=['Product_ID','Product_Name','Category','Subcategory','Brand','Unit_Cost','Selling_Price','Demand_Index'])
products['Unit_Cost'] = products['Unit_Cost'].astype(float)
products['Selling_Price'] = products['Selling_Price'].astype(float)

# -----------------------------
# Customers
# -----------------------------
N_CUSTOMERS = 7500
first_names = ['Aarav','Vivaan','Aditya','Arjun','Sai','Rahul','Rohan','Karthik','Vikram','Varun','Siddharth','Nikhil','Anirudh','Akash','Manish','Harsh','Sanjay','Ritesh','Ravi','Abhishek','Aditi','Ananya','Diya','Isha','Ishita','Kavya','Keerthi','Meera','Neha','Nandini','Pooja','Priya','Riya','Sneha','Shreya','Simran','Tanvi','Vaishnavi','Anusha','Sahithi']
last_names = ['Rao','Reddy','Sharma','Mehta','Verma','Iyer','Nair','Patil','Gupta','Kapoor','Joshi','Singh','Jain','Desai','Kulkarni','Menon','Naidu','Roy','Pillai','Kaur','Das','Sinha','Malhotra','Bhat']
city_weights = np.array([2.0,0.9,1.1,2.3,1.8,0.8,2.4,1.5,1.2,0.9,1.9,1.5,1.3,0.8,1.5,0.8,0.7,1.1,0.7,1.0])
city_weights = city_weights / city_weights.sum()
loc_idx = rng.choice(len(regions), size=N_CUSTOMERS, p=city_weights)
customer_rows=[]
for i in range(N_CUSTOMERS):
    loc = regions.iloc[loc_idx[i]]
    name = f'{rng.choice(first_names)} {rng.choice(last_names)}'
    gender = rng.choice(['Male','Female'], p=[0.56,0.44])
    age = int(np.clip(rng.normal(34, 9), 20, 65))
    customer_rows.append((f'C{i+1:05d}', name, gender, age, loc.City, loc.State, loc.Region_Name, rng.choice(['Standard','Premium','Corporate'], p=[0.69,0.24,0.07])))
customers = pd.DataFrame(customer_rows, columns=['Customer_ID','Customer_Name','Gender','Age','City','State','Region','Customer_Segment'])

# latent purchase frequency + value behavior
latent = rng.choice(['HighValue','Loyal','Regular','Occasional','LowValue'], size=N_CUSTOMERS, p=[0.08,0.18,0.34,0.28,0.12])
base_lambda = {'HighValue':20,'Loyal':12,'Regular':7,'Occasional':3,'LowValue':1.5}
customer_lambda = np.array([base_lambda[x] for x in latent])
# corporate customers are more order-heavy
customer_lambda += np.where(customers.Customer_Segment.values=='Corporate', 4, 0)

# -----------------------------
# Order generation
# -----------------------------
N_ORDERS = 80000
dates = pd.date_range('2025-01-01','2025-12-31',freq='D')
month_weights = np.array([0.95,0.90,0.98,1.00,1.05,0.97,0.96,0.99,1.08,1.28,1.42,1.15])
weekday_weights = np.array([0.80,1.00,1.05,1.05,1.08,1.12,0.92])
day_factor = month_weights[dates.month-1] * weekday_weights[dates.dayofweek]
day_factor = day_factor/day_factor.sum()
order_dates = rng.choice(dates.values, size=N_ORDERS, p=day_factor)
order_dates = pd.to_datetime(order_dates)

# sample customers proportional to latent value and some randomness
cust_prob = customer_lambda / customer_lambda.sum()
cust_idx = rng.choice(N_CUSTOMERS, size=N_ORDERS, p=cust_prob)
product_demand = products.Demand_Index.values / products.Demand_Index.values.sum()
prod_idx = rng.choice(len(products), size=N_ORDERS, p=product_demand)

# map location -> region group
region_lookup = regions.set_index('Region_ID')
# customer location determines most regional orders
order_region_ids = customers.iloc[cust_idx].City.values
city_to_region = dict(zip(regions.City, regions.Region_ID))
region_ids = np.array([city_to_region[x] for x in order_region_ids])
# 12% of online / marketplace orders can ship from adjacent market, but retain realism
adjacent = {'South':['R01','R02','R03','R04','R05','R06'],'West':['R07','R08','R09','R10'],'North':['R11','R12','R13','R14'],'East':['R15','R16','R17'],'Central':['R18','R19','R20']}
for i in range(N_ORDERS):
    if rng.random() < 0.07:
        current = region_lookup.loc[region_ids[i], 'Region_Name']
        candidates = [r for r in regions.Region_ID if r not in adjacent[current]]
        region_ids[i] = rng.choice(candidates)

channel_probs = {'South':[0.43,0.24,0.25,0.08],'West':[0.47,0.22,0.23,0.08],'North':[0.44,0.23,0.23,0.10],'East':[0.39,0.25,0.27,0.09],'Central':[0.36,0.27,0.28,0.09]}
region_group = region_lookup.loc[region_ids,'Region_Name'].values
channel_ids = np.array([rng.choice(channels.Channel_ID.values, p=channel_probs[g]) for g in region_group])

# salesperson chosen mostly by region
sp_by_region = {r: salespeople[salespeople.Region==r].Salesperson_ID.tolist() for r in salespeople.Region.unique()}
sp_ids = np.array([rng.choice(sp_by_region[g]) for g in region_group])

payment_options = ['UPI','Credit Card','Debit Card','Net Banking','Cash on Delivery','Bank Transfer']
pay_probs = {
    'Online':[0.45,0.25,0.15,0.10,0.05,0.00],
    'Retail Store':[0.20,0.26,0.28,0.02,0.22,0.02],
    'Marketplace':[0.38,0.24,0.17,0.06,0.15,0.00],
    'Corporate':[0.10,0.25,0.15,0.10,0.00,0.40]
}
channel_name = dict(zip(channels.Channel_ID, channels.Channel_Name))
payments = np.array([rng.choice(payment_options, p=pay_probs[channel_name[c]]) for c in channel_ids])

quantity = rng.choice([1,2,3,4], size=N_ORDERS, p=[0.58,0.27,0.10,0.05]).astype(int)
# category-specific quantities
cats = products.Category.values[prod_idx]
quantity = np.where(cats=='Grocery', rng.choice([1,2,3,4,5,6], size=N_ORDERS, p=[.20,.25,.22,.15,.10,.08]), quantity)
quantity = np.where(cats=='Fashion', rng.choice([1,2,3,4], size=N_ORDERS, p=[.55,.28,.12,.05]), quantity)
quantity = np.where(cats=='Furniture', rng.choice([1,2], size=N_ORDERS, p=[.82,.18]), quantity)

base_prices = products.Selling_Price.values[prod_idx]
base_costs = products.Unit_Cost.values[prod_idx]
region_factor = np.array([{\
    'South':1.01,'West':1.03,'North':1.00,'East':0.98,'Central':0.97}[g] for g in region_group])
channel_factor = np.array([{'Online':1.00,'Retail Store':1.02,'Marketplace':0.98,'Corporate':0.95}[channel_name[c]] for c in channel_ids])
price_noise = rng.normal(0,0.018,size=N_ORDERS)
unit_price = np.round(base_prices*region_factor*channel_factor*(1+price_noise),2)
# stable procurement cost around catalog cost
unit_cost = np.round(base_costs*(1+rng.normal(0,0.035,size=N_ORDERS)),2)

# discount by channel, with promotion month uplift
base_disc = {'Online':0.10,'Retail Store':0.05,'Marketplace':0.14,'Corporate':0.07}
discount = np.array([np.clip(rng.normal(base_disc[channel_name[c]],0.035),0,0.25) for c in channel_ids])
discount += np.where(pd.to_datetime(order_dates).month.isin([10,11]), 0.025, 0)
# slightly higher electronics discounts during festive period
discount += np.where((cats=='Electronics') & pd.to_datetime(order_dates).month.isin([10,11,12]), 0.018, 0)
discount = np.round(np.clip(discount,0,0.30),4)

revenue = np.round(quantity*unit_price*(1-discount),2)
cost = np.round(quantity*unit_cost,2)
profit = np.round(revenue-cost,2)

# Ensure a manageable set of low-margin but not wildly negative lines
status = rng.choice(['Completed','Returned','Cancelled'], size=N_ORDERS, p=[0.92,0.055,0.025])
# Payment method and status can be correlated with returns
return_mask = (status=='Returned')
status[return_mask & (rng.random(N_ORDERS)<0.35)] = 'Completed'

orders = pd.DataFrame({
    'Order_ID':[f'O{i+1:06d}' for i in range(N_ORDERS)],
    'Order_Date':pd.to_datetime(order_dates),
    'Customer_ID':customers.Customer_ID.values[cust_idx],
    'Product_ID':products.Product_ID.values[prod_idx],
    'Region_ID':region_ids,
    'Salesperson_ID':sp_ids,
    'Channel_ID':channel_ids,
    'Quantity':quantity,
    'Unit_Price':unit_price,
    'Discount':discount,
    'Revenue':revenue,
    'Cost':cost,
    'Profit':profit,
    'Payment_Method':payments,
    'Order_Status':status
})

# Registration date based on first observed order, with a realistic pre-order buffer.
first_order = orders.groupby('Customer_ID').Order_Date.min()
reg_dates=[]
for cid in customers.Customer_ID:
    if cid in first_order.index:
        f = first_order[cid]
        back_days = int(rng.integers(15, 540))
        reg_dates.append(max(pd.Timestamp('2024-01-01'), f-pd.Timedelta(days=back_days)))
    else:
        reg_dates.append(pd.Timestamp('2024-01-01') + pd.Timedelta(days=int(rng.integers(0, 365))))
customers['Registration_Date']=pd.to_datetime(reg_dates)

# -----------------------------
# Raw data-quality issues
# -----------------------------
raw_orders = orders.copy()
# Duplicates: exact duplicates
n_dup = 340
raw_orders = pd.concat([raw_orders, raw_orders.sample(n_dup, random_state=SEED)], ignore_index=True)
# Missing customer IDs
miss_idx = rng.choice(raw_orders.index, size=420, replace=False)
raw_orders.loc[miss_idx,'Customer_ID'] = None
# Invalid quantities
bad_q_idx = rng.choice(raw_orders.index, size=180, replace=False)
raw_orders.loc[bad_q_idx,'Quantity'] = rng.choice([0,-1], size=len(bad_q_idx))
# Incorrect numeric types for discount
bad_d_idx = rng.choice(raw_orders.index, size=180, replace=False)
raw_orders['Discount'] = raw_orders['Discount'].astype(object)
raw_orders.loc[bad_d_idx,'Discount'] = [f'{int(round(float(x)*100))}%' for x in raw_orders.loc[bad_d_idx,'Discount']]
# Leading/trailing spaces and casing inconsistencies
for col in ['Payment_Method','Order_Status']:
    idx = rng.choice(raw_orders.index, size=220, replace=False)
    raw_orders.loc[idx,col] = raw_orders.loc[idx,col].astype(str).map(lambda x: f'  {x.upper()}  ')
# Invalid product IDs
bad_p_idx = rng.choice(raw_orders.index, size=100, replace=False)
raw_orders.loc[bad_p_idx,'Product_ID'] = 'P999'
# Small number of unit prices stored as text with spaces
bad_price_idx = rng.choice(raw_orders.index, size=90, replace=False)
raw_orders['Unit_Price'] = raw_orders['Unit_Price'].astype(object)
raw_orders.loc[bad_price_idx,'Unit_Price'] = raw_orders.loc[bad_price_idx,'Unit_Price'].map(lambda x: f' {x} ')

raw_customers = customers.copy()
mc_idx = rng.choice(raw_customers.index, size=35, replace=False)
raw_customers.loc[mc_idx,'Age'] = None
seg_idx = rng.choice(raw_customers.index, size=80, replace=False)
raw_customers.loc[seg_idx,'Customer_Segment'] = raw_customers.loc[seg_idx,'Customer_Segment'].map(lambda x: f' {x.lower()} ')
city_idx = rng.choice(raw_customers.index, size=70, replace=False)
raw_customers.loc[city_idx,'City'] = raw_customers.loc[city_idx,'City'].map(lambda x: f'{x} ')

raw_products = products.drop(columns=['Demand_Index']).copy()
cat_idx = rng.choice(raw_products.index, size=40, replace=False)
raw_products.loc[cat_idx,'Category'] = raw_products.loc[cat_idx,'Category'].astype(str).map(lambda x: x.lower())
brand_idx = rng.choice(raw_products.index, size=30, replace=False)
raw_products.loc[brand_idx,'Brand'] = raw_products.loc[brand_idx,'Brand'].map(lambda x: f' {x} ')

raw_regions = regions.copy()
rg_idx = rng.choice(raw_regions.index, size=12, replace=False)
raw_regions.loc[rg_idx,'Region_Name'] = raw_regions.loc[rg_idx,'Region_Name'].astype(str).map(lambda x: x.lower())

raw_salespeople = salespeople.copy()
sp_idx = rng.choice(raw_salespeople.index, size=15, replace=False)
raw_salespeople.loc[sp_idx,'Team'] = raw_salespeople.loc[sp_idx,'Team'].map(lambda x: f'{x} ')

# Save raw data. Dates ISO for portability.
for name, df in [('orders',raw_orders),('customers',raw_customers),('products',raw_products),('regions',raw_regions),('salespeople',raw_salespeople),('channels',channels)]:
    out = ROOT/'data/raw'/f'{name}.csv'
    dfx = df.copy()
    for c in dfx.columns:
        if is_datetime64_any_dtype(dfx[c]):
            dfx[c] = dfx[c].dt.strftime('%Y-%m-%d')
    dfx.to_csv(out, index=False)


print(f'Generated raw NovaMart data in {ROOT / "data/raw"}.')
