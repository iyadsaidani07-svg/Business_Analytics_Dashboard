import pandas as pd
from app.analytics import (
    calculate_gross_revenue,
    calculate_total_revenue,
    calculate_total_quantity,
    calculate_total_number_of_transactions,
    calculate_transactions_by_category,
    calculate_revenue_by_category,
    calculate_top_5_categories_per_revenue,
    calculate_quantity_sold_by_category,
    calculate_average_transaction_value,
    calculate_revenue_by_region,
    calculate_revenue_by_year,
    calculate_revenue_by_month
)
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
        #revenue by transaction but no discounts into consideration
df["gross_revenue"]=calculate_gross_revenue(df)    
print(df["gross_revenue"].head()) 
      #calculation of total revenue with discounts if exists
total_revenue=calculate_total_revenue(df)                    
print("Total_revenue:",total_revenue)
        #calculation of total quantity for all categs
total_quantity=calculate_total_quantity(df)                  
print('Total_quantity:',total_quantity)
  #counting total number of transactions
total_transactions=calculate_total_number_of_transactions(df)                           
print("total transactions:",total_transactions)
      #number of transactions for each category
transactions_per_categ=calculate_transactions_by_category(df)              
print("transaction per category:")
print(transactions_per_categ)
          #revenue by category
revenue_by_category=calculate_revenue_by_category(df) 
print("Revenue by category:")
print(revenue_by_category)
  #top 5 categories per revenue
top_5_categories=calculate_top_5_categories_per_revenue(df)
print("top 5 categories by revenue:")                          
print(top_5_categories)
   #quantity sold by category
quantity_sold_by_category=calculate_quantity_sold_by_category(df) 
print("Quantity sold by category:")
print(quantity_sold_by_category)
    #average transaction value
average_trans_val=calculate_average_transaction_value(df)           
print("Average transaction value:",average_trans_val)
            #revenue by region
revenue_by_region=calculate_revenue_by_region(df)                                                           
print("revenue by region:")
print(revenue_by_region)
            #revenue by year
revenue_by_year=calculate_revenue_by_year(df) 
print("revenue by year:")
print(revenue_by_year)
          #revenue by month
revenue_by_month=calculate_revenue_by_month(df) 
print("revenue by month:")
print(revenue_by_month)