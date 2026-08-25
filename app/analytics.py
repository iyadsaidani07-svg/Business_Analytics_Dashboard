def calculate_gross_revenue(df):                                #revenue by transaction but no discounts into consideration                                      
   return df["Quantity_Sold"]*df["Unit_Price"]    
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
def calculate_top_5_categories_per_revenue(df):                  #top 5 products per revenue
   return df.groupby("Product_Category")["Sales_Amount"].sum().nlargest(5,keep='all')
def calculate_quantity_sold_by_category(df):                       #quantity sold by category
   return df.groupby("Product_Category")["Quantity_Sold"].sum() 
def calculate_average_transaction_value(df):                                #average transaction value    
   total_revenue = calculate_total_revenue(df)
   total_transactions = calculate_total_number_of_transactions(df)
   return total_revenue/total_transactions           
def calculate_revenue_by_region(df):                            #revenue by region
   return df.groupby("Region")["Sales_Amount"].sum()                                                            # revenue by region
def calculate_revenue_by_year(df):                              #revenue by year
   return df.groupby(df["Sale_Date"].dt.year)["Sales_Amount"].sum() 
def calculate_revenue_by_month(df):                             #revenue by month
   return df.groupby(df["Sale_Date"].dt.to_period("M"))["Sales_Amount"].sum() 

