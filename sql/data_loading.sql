USE novamart_analytics;

LOAD DATA LOCAL INFILE 'data/cleaned/customers_clean.csv'
INTO TABLE Customers
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
IGNORE 1 LINES
(Customer_ID,Customer_Name,Gender,Age,City,State,Region,Customer_Segment,Registration_Date);

LOAD DATA LOCAL INFILE 'data/cleaned/products_clean.csv'
INTO TABLE Products
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
IGNORE 1 LINES
(Product_ID,Product_Name,Category,Subcategory,Brand,Unit_Cost,Selling_Price);

LOAD DATA LOCAL INFILE 'data/cleaned/regions_clean.csv'
INTO TABLE Regions
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
IGNORE 1 LINES
(Region_ID,Region_Name,State,City);

LOAD DATA LOCAL INFILE 'data/cleaned/salespeople_clean.csv'
INTO TABLE Salespeople
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
IGNORE 1 LINES
(Salesperson_ID,Salesperson_Name,Region,Team);

LOAD DATA LOCAL INFILE 'data/cleaned/channels_clean.csv'
INTO TABLE Channels
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
IGNORE 1 LINES
(Channel_ID,Channel_Name);

LOAD DATA LOCAL INFILE 'data/cleaned/orders_clean.csv'
INTO TABLE Orders
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
IGNORE 1 LINES
(Order_ID,Order_Date,Customer_ID,Product_ID,Region_ID,Salesperson_ID,Channel_ID,Quantity,Unit_Price,Discount,Revenue,Unit_Cost,Cost,Profit,Payment_Method,Order_Status);