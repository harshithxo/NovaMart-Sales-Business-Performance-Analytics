let
    Root = "<PROJECT_ROOT>",
    RawFolder = Root & "/data/cleaned/",

    OrdersSource = Csv.Document(File.Contents(RawFolder & "orders_clean.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    OrdersPromoted = Table.PromoteHeaders(OrdersSource, [PromoteAllScalars=true]),
    OrdersTyped = Table.TransformColumnTypes(OrdersPromoted, {
        {"Order_ID", type text}, {"Order_Date", type date}, {"Customer_ID", type text}, {"Product_ID", type text},
        {"Region_ID", type text}, {"Salesperson_ID", type text}, {"Channel_ID", type text}, {"Quantity", Int64.Type},
        {"Unit_Price", type number}, {"Discount", type number}, {"Revenue", type number}, {"Unit_Cost", type number},
        {"Cost", type number}, {"Profit", type number}, {"Payment_Method", type text}, {"Order_Status", type text}
    }),

    CustomersSource = Csv.Document(File.Contents(RawFolder & "customers_clean.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Customers = Table.TransformColumnTypes(Table.PromoteHeaders(CustomersSource, [PromoteAllScalars=true]), {
        {"Customer_ID", type text}, {"Customer_Name", type text}, {"Gender", type text}, {"Age", Int64.Type},
        {"City", type text}, {"State", type text}, {"Region", type text}, {"Customer_Segment", type text}, {"Registration_Date", type date}
    }),

    ProductsSource = Csv.Document(File.Contents(RawFolder & "products_clean.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Products = Table.TransformColumnTypes(Table.PromoteHeaders(ProductsSource, [PromoteAllScalars=true]), {
        {"Product_ID", type text}, {"Product_Name", type text}, {"Category", type text}, {"Subcategory", type text},
        {"Brand", type text}, {"Unit_Cost", type number}, {"Selling_Price", type number}
    }),

    RegionsSource = Csv.Document(File.Contents(RawFolder & "regions_clean.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Regions = Table.TransformColumnTypes(Table.PromoteHeaders(RegionsSource, [PromoteAllScalars=true]), {
        {"Region_ID", type text}, {"Region_Name", type text}, {"State", type text}, {"City", type text}
    }),

    SalespeopleSource = Csv.Document(File.Contents(RawFolder & "salespeople_clean.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Salespeople = Table.TransformColumnTypes(Table.PromoteHeaders(SalespeopleSource, [PromoteAllScalars=true]), {
        {"Salesperson_ID", type text}, {"Salesperson_Name", type text}, {"Region", type text}, {"Team", type text}
    }),

    ChannelsSource = Csv.Document(File.Contents(RawFolder & "channels_clean.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Channels = Table.TransformColumnTypes(Table.PromoteHeaders(ChannelsSource, [PromoteAllScalars=true]), {
        {"Channel_ID", type text}, {"Channel_Name", type text}
    }),

    Output = [Orders=OrdersTyped, Customers=Customers, Products=Products, Regions=Regions, Salespeople=Salespeople, Channels=Channels]
in
    Output
