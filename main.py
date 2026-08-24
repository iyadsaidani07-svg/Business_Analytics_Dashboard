import pandas as pd
df=pd.read_csv("data/sales_data.csv")
#CHECKING TYPES ------------------------------------------------------------------------------
print(df.head())
print(df.shape)
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())
df["Sale_Date"]=pd.to_datetime(df["Sale_Date"])             #change type to date
print(df["Sale_Date"].dtype)
num_cols=df.select_dtypes(include=["number"])               #making sure no neg vals in num cols
rows_with_negs=df[(num_cols<0).any(axis=1)]
df= df.drop(rows_with_negs.index)
print(rows_with_negs)
for col in df.select_dtypes(include=["number"]).columns:    #handling missing values
    df[col]=df[col].fillna(df[col].mean())
for col in df.select_dtypes(exclude=["number"]).columns:
     df[col]=df[col].fillna("Unknown")  
print("number of duplicates:",df.duplicated().sum())        #handling duplicates
print("duplicated rows:")                        
print(df[df.duplicated()])
df=df.drop_duplicates()
#ANALYTICS -------------------------------------------------------------------------
df["Gross_revenue"]=df["Quantity_Sold"]*df["Unit_Price"]    #revenue by transactionbut no discounts into consideration 
print(df["Gross_revenue"].head()) 
Total_revenue=df["Sales_Amount"].sum()                      #calculation total revenue (wth discount if exists)
print("Total_revenue:",Total_revenue)
Total_quantity=df["Quantity_Sold"].sum()                    #calculation of total quantity for all categs
print('Total_quantity:',Total_quantity)
Total_transactions=len(df.index)                            #counting total number of transactions
print("total transactions:",Total_transactions)
categs=df["Product_Category"].value_counts()                #number of transactions for each category
print("transaction per category:")
print(categs)
Revenue_by_category=df.groupby("Product_Category")["Sales_Amount"].sum() #revenue by category
print("Revenue by category:")
print(Revenue_by_category)
print("top 5 products by revenue:")                          #top 5 products per revenue
Top_5_categories=Revenue_by_category.nlargest(5,keep='all')
print(Top_5_categories)
Quantity_sold_by_category=df.groupby("Product_Category")["Quantity_Sold"].sum() #quantity sold by category
print("Quantity sold by category:")
print(Quantity_sold_by_category)
Average_trans_val=Total_revenue/Total_transactions            #average transaction value
print("Average transaction value:",Average_trans_val)
Revenue_by_region=df.groupby("Region")["Sales_Amount"].sum()                                                            # revenue by region
print("revenue by region:",Revenue_by_region)
Revenue_by_year=df.groupby(df["Sale_Date"].dt.year)["Sales_Amount"].sum() #revenue by year
print("revenue by year:")
print(Revenue_by_year)
Revenue_by_month=df.groupby(df["Sale_Date"].dt.to_period("M"))["Sales_Amount"].sum() #revenue by month
print("revenue by month:")
print(Revenue_by_month)