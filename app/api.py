from fastapi import FastAPI
import pandas as pd
from analytics import (
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
app=FastAPI()
@app.get("/")
def read_root():
    return {"message":"Business analytics API"}
@app.get("/health")
def health_check():
    return {"status":"ok"}
@app.get("/get_data")
def data_summary():
    df=pd.read_csv("../data/sales_data.csv")
    rows=len(df.index)
    columns=df.shape[1]
    return {"rows":rows,
             "columns":columns}
@app.get("/analytics")
def welcome_to_analytics():
    df=pd.read_csv("../data/sales_data.csv")
    return {"welcome":"please choose what type of analytics you want"}
#REAL ANALYTICS
@app.get("/analytics/general_info")
def totals_and_avg_calculated():
    df=pd.read_csv("../data/sales_data.csv")
    gross_revenue=calculate_gross_revenue(df)
    total_revenue=calculate_total_revenue(df)                    
    total_quantity=calculate_total_quantity(df)                  
    total_transactions=calculate_total_number_of_transactions(df)   
    average_trans_val=calculate_average_transaction_value(df)                          
    return {"total_revenue":float(total_revenue),
             "total_quantity":int(total_quantity),
             "total_transactions":int(total_transactions),
             "average_transaction_value":float(average_trans_val),
             "gross_revenue(no discounts)":gross_revenue.to_dict()}
@app.get("/analytics/by_category")
def data_by_category_calculated():
    df=pd.read_csv("../data/sales_data.csv")
    transactions_per_categ=calculate_transactions_by_category(df)
    revenue_by_category=calculate_revenue_by_category(df) 
    top_5_categories=calculate_top_5_categories_per_revenue(df)
    quantity_sold_by_category=calculate_quantity_sold_by_category(df) 
    return {"transactions_per_category":transactions_per_categ.to_dict(),
            "revenue_by_category":revenue_by_category.to_dict(),
            "top_5_categories":top_5_categories.to_dict(),
            "quantity_sold_by_category":quantity_sold_by_category.to_dict()}
@app.get("/analytics/by_region")
def data_by_region_calculated():
    df=pd.read_csv("../data/sales_data.csv")
    revenue_by_region=calculate_revenue_by_region(df)
    return {"revenue_by_region":revenue_by_region.to_dict()} 
@app.get("/analytics/by_year")
def data_by_year_calculated():
    df=pd.read_csv("../data/sales_data.csv")
    revenue_by_year=calculate_revenue_by_year(df)
    return {"revenue_by_year":revenue_by_year.to_dict()} 
@app.get("/analytics/by_month")
def data_by_month_calculated():
    df=pd.read_csv("../data/sales_data.csv")
    revenue_by_month=calculate_revenue_by_month(df)
    revenue_by_month.index=revenue_by_month.index.astype(str)
    return {"revenue_by_month":revenue_by_month.to_dict()} 
