import pandas as pd
def calculate_gross_revenue(df):                                #revenue by transaction but no discounts into consideration                                      
   return (df["Quantity_Sold"]*df["Unit_Price"]).sum()    
def calculate_total_revenue(df):                                #calculation total revenue (wth discount if exists)
   return df["Sales_Amount"].sum()                     
def calculate_total_quantity(df):                    #calculation of total quantity for all categs 
   return df["Quantity_Sold"].sum()                    
def calculate_total_number_of_transactions(df):                        #counting total number of transactions
   return len(df.index)                            
def calculate_transactions_by_category(df):                        #number of transactions for each category
   return df["Product_Category"].value_counts()               
def calculate_revenue_by_category(df):                                 #revenue by category
   return df.groupby("Product_Category")["Sales_Amount"].sum()  
def calculate_top_5_categories_per_revenue(df):                  #top 5 categories per revenue
   return df.groupby("Product_Category")["Sales_Amount"].sum().nlargest(5,keep='all')
def calculate_quantity_sold_by_category(df):                       #quantity sold by category
   return df.groupby("Product_Category")["Quantity_Sold"].sum() 
def calculate_average_transaction_value(df):                                #average transaction value    
   total_revenue = calculate_total_revenue(df)
   total_transactions = calculate_total_number_of_transactions(df)
   return total_revenue/total_transactions           
def calculate_revenue_by_region(df):                            #revenue by region
   return df.groupby("Region")["Sales_Amount"].sum()                                                            # revenue by region
def calculate_revenue_by_year(df): 
   df["Sale_Date"]=pd.to_datetime(df["Sale_Date"])                              #revenue by year
   return df.groupby(df["Sale_Date"].dt.year)["Sales_Amount"].sum() 
def calculate_revenue_by_month(df):                                  #revenue by month
   df["Sale_Date"]=pd.to_datetime(df["Sale_Date"])                        
   return df.groupby(df["Sale_Date"].dt.to_period("M"))["Sales_Amount"].sum() 
#LARGE FULL ANALYTICS FUNCTION
def run_analytics(df):
    gross_revenue = calculate_gross_revenue(df)
    total_revenue = calculate_total_revenue(df)
    total_quantity = calculate_total_quantity(df)
    total_transactions = calculate_total_number_of_transactions(df)
    average_trans_val = calculate_average_transaction_value(df)
    transactions_per_categ = calculate_transactions_by_category(df)
    revenue_by_category = calculate_revenue_by_category(df)
    top_5_categories = calculate_top_5_categories_per_revenue(df)
    quantity_sold_by_category = calculate_quantity_sold_by_category(df)
    revenue_by_region = calculate_revenue_by_region(df)
    revenue_by_year = calculate_revenue_by_year(df)
    revenue_by_month = calculate_revenue_by_month(df)
    # Convert index to string so it can safely be returned as JSON
    revenue_by_month.index = revenue_by_month.index.astype(str)
    return  {
            "total_revenue": float(total_revenue),
            "total_quantity": int(total_quantity),
            "total_transactions": int(total_transactions),
            "average_transaction_value": float(average_trans_val),
            "gross_revenue":float(gross_revenue),
            "transactions_per_category": transactions_per_categ.to_dict(),
            "revenue_by_category": revenue_by_category.to_dict(),
            "top_5_categories": top_5_categories.to_dict(),
            "quantity_sold_by_category": quantity_sold_by_category.to_dict(),
            "revenue_by_region": revenue_by_region.to_dict(),
            "revenue_by_year": revenue_by_year.to_dict(),
            "revenue_by_month": revenue_by_month.to_dict()}

