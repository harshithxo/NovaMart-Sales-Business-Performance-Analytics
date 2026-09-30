-- NovaMart Sales & Business Performance Analytics
-- MySQL 8.0+
CREATE DATABASE IF NOT EXISTS novamart_analytics;
USE novamart_analytics;

DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Regions;
DROP TABLE IF EXISTS Salespeople;
DROP TABLE IF EXISTS Channels;
DROP TABLE IF EXISTS Dim_Date;

CREATE TABLE Customers (
    Customer_ID VARCHAR(10) PRIMARY KEY,
    Customer_Name VARCHAR(120) NOT NULL,
    Gender VARCHAR(20),
    Age INT,
    City VARCHAR(80),
    State VARCHAR(80),
    Region VARCHAR(40),
    Customer_Segment VARCHAR(30),
    Registration_Date DATE
);

CREATE TABLE Products (
    Product_ID VARCHAR(10) PRIMARY KEY,
    Product_Name VARCHAR(150) NOT NULL,
    Category VARCHAR(80),
    Subcategory VARCHAR(80),
    Brand VARCHAR(80),
    Unit_Cost DECIMAL(12,2),
    Selling_Price DECIMAL(12,2)
);

CREATE TABLE Regions (
    Region_ID VARCHAR(10) PRIMARY KEY,
    Region_Name VARCHAR(40),
    State VARCHAR(80),
    City VARCHAR(80)
);

CREATE TABLE Salespeople (
    Salesperson_ID VARCHAR(10) PRIMARY KEY,
    Salesperson_Name VARCHAR(120),
    Region VARCHAR(40),
    Team VARCHAR(80)
);

CREATE TABLE Channels (
    Channel_ID VARCHAR(10) PRIMARY KEY,
    Channel_Name VARCHAR(40)
);

CREATE TABLE Orders (
    Order_ID VARCHAR(20) PRIMARY KEY,
    Order_Date DATE NOT NULL,
    Customer_ID VARCHAR(10) NOT NULL,
    Product_ID VARCHAR(10) NOT NULL,
    Region_ID VARCHAR(10) NOT NULL,
    Salesperson_ID VARCHAR(10) NOT NULL,
    Channel_ID VARCHAR(10) NOT NULL,
    Quantity INT NOT NULL,
    Unit_Price DECIMAL(12,2) NOT NULL,
    Discount DECIMAL(8,4) NOT NULL,
    Revenue DECIMAL(14,2) NOT NULL,
    Unit_Cost DECIMAL(12,2) NOT NULL,
    Cost DECIMAL(14,2) NOT NULL,
    Profit DECIMAL(14,2) NOT NULL,
    Payment_Method VARCHAR(40),
    Order_Status VARCHAR(20),
    CONSTRAINT fk_orders_customer FOREIGN KEY (Customer_ID) REFERENCES Customers(Customer_ID),
    CONSTRAINT fk_orders_product FOREIGN KEY (Product_ID) REFERENCES Products(Product_ID),
    CONSTRAINT fk_orders_region FOREIGN KEY (Region_ID) REFERENCES Regions(Region_ID),
    CONSTRAINT fk_orders_salesperson FOREIGN KEY (Salesperson_ID) REFERENCES Salespeople(Salesperson_ID),
    CONSTRAINT fk_orders_channel FOREIGN KEY (Channel_ID) REFERENCES Channels(Channel_ID)
);

CREATE INDEX idx_orders_date ON Orders(Order_Date);
CREATE INDEX idx_orders_customer ON Orders(Customer_ID);
CREATE INDEX idx_orders_product ON Orders(Product_ID);
CREATE INDEX idx_orders_region ON Orders(Region_ID);
CREATE INDEX idx_orders_channel ON Orders(Channel_ID);
