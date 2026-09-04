from fastapi import FastAPI,UploadFile,File,HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from app.analytics import run_analytics
from app.validation import validation
from app.cleaning import clean_data
from app.mapping import column_mapping
app=FastAPI()
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_headers=["*"],allow_methods=["*"])
@app.get("/")
def read_root():
    return {"message":"Business analytics API"}
@app.get("/health")
def health_check():
    return {"status":"ok"}
@app.post("/upload")
def user_uploaded_file(file:UploadFile=File(...)):
    try:
       if file.filename.endswith(('.xlsx', '.xls')):
           df = pd.read_excel(file.file) 
       elif file.filename.endswith(('.csv')):
           df=pd.read_csv(file.file)
       else:
           raise HTTPException(status_code=400,detail="Unsupported file type. Please upload a CSV or Excel file.") 
    except HTTPException:
        raise    
    except Exception:
        raise HTTPException(status_code=400,detail="The file could not be read.")
    df=column_mapping(df)                           #mapping    
    validation_result=validation(df)                #validation
    if validation_result["valid"] :  
                                                    #cleaning
        df=clean_data(df)
                                                    #analytics
        analytics_results= run_analytics(df)
        return {
        "filename": file.filename,

        "data_info": {"rows": len(df.index),"columns": df.shape[1]},

        "validation": validation_result,

        "analytics":analytics_results }                             
    else :
        return {
    "filename": file.filename,
    "data_info": {"rows": len(df.index),"columns": df.shape[1]},
    "validation": validation_result,
    "analytics": None}