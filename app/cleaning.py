import pandas as pd
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