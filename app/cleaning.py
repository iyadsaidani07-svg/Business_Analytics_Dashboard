import pandas as pd
def convert_numeric_columns(df):
    numeric_columns = ["Quantity_Sold","Unit_Price","Sales_Amount"]
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df
def convert_non_numeric_columns(df):
    non_numeric_columns = ["Product_Category","Region"]
    for col in non_numeric_columns:
        df[col] = df[col].astype("string")
    return df
def no_negatives_in_numerical_columns(df):
    num_cols=df.select_dtypes(include=["number"])              
    rows_with_negs=df[(num_cols<0).any(axis=1)]
    df= df.drop(rows_with_negs.index)   
    return df 
def handling_missing_values(df):
    for col in df.select_dtypes(include=["number"]).columns:    
       df[col]=df[col].fillna(df[col].mean())
    for col in df.select_dtypes(exclude=["number"]).columns:
       df[col]=df[col].fillna("Unknown")  
    return df   
def handling_duplicates(df):
    df=df.drop_duplicates()
    return df
def clean_data(df):
    df = convert_numeric_columns(df)
    df = convert_non_numeric_columns(df)
    df = no_negatives_in_numerical_columns(df)
    df = handling_missing_values(df)
    df = handling_duplicates(df)
    return df