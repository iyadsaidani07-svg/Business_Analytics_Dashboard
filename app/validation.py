import pandas as pd
def validation(df):
    required_columns=["Quantity_Sold","Unit_Price","Sales_Amount","Product_Category","Region","Sale_Date"]
    present_columns=df.columns
    if set(required_columns).issubset(set(present_columns)):        
        return {"valid": True,"missing_columns": []}
    else:
        missing_columns=[item for item in required_columns if item not in present_columns]
        return {"valid": False,"missing_columns": missing_columns}