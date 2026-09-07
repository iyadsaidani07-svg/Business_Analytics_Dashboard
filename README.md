# Business Analytics Dashboard



A Python and FastAPI application that allows users to upload sales datasets in CSV or Excel format and automatically performs data validation, cleaning, and business analytics.

## Live Demo

The deployed application is available here:

https://business-analytics-dashboard-zdtd.onrender.com/

## Features



* Upload CSV and Excel sales datasets

* Automatically map different column names to standard column names

* Validate required columns

* Clean uploaded data

* Convert numerical columns to numeric values

* Handle missing values

* Remove negative numerical values

* Remove duplicate rows

* Calculate business analytics

* Return results through a FastAPI API

* Automated API tests with pytest



## Project Structure



```text

business\_analytics\_dashboard/

├── app/

│   ├── \_\_init\_\_.py

│   ├── api.py

│   ├── analytics.py

│   ├── cleaning.py

│   ├── mapping.py

│   └── validation.py

│

├── data/

│   └── sales\_data.csv

│

├── tests/

│   └── test\_api.py

│

├── README.md

├── requirements.txt

└── pytest.ini

```



## Technologies



* Python

* FastAPI

* Pandas

* OpenPyXL

* Pytest

* HTTPX



## Installation



Install the required dependencies using:



```bash

pip install -r requirements.txt

```



## Running the API



Start the FastAPI application with:



```bash

uvicorn app.api:app --reload

```



The API will start on the local server.



FastAPI also provides interactive API documentation through Swagger UI.



## Uploading a Dataset



The main endpoint is:



```text

POST /upload

```



It accepts:



* CSV files

* Excel files (`.xlsx` and `.xls`)



The uploaded dataset goes through the following pipeline:



```text

File Upload

         ↓

File Reading

         ↓

Column Mapping

         ↓

Validation

         ↓

Data Cleaning

         ↓

Analytics

         ↓

JSON Response

```



## Required Data



The application expects the following standardized columns:



* `Quantity_Sold`

* `Unit_Price`

* `Sales_Amount`

* `Product_Category`

* `Region`

* `Sale_Date`



Different column names can be mapped automatically to these standard names.



## Data Cleaning



The cleaning process includes:



* Converting numerical columns to numeric values

* Converting categorical columns to string values

* Removing rows containing negative numerical values

* Handling missing values

* Removing duplicate rows



## Analytics



The application calculates several business metrics, including:



* Total revenue

* Total quantity sold

* Total number of transactions

* Average transaction value

* Gross revenue

* Transactions by category

* Revenue by category

* Top 5 categories by revenue

* Quantity sold by category

* Revenue by region

* Revenue by year

* Revenue by month



## Testing



Automated tests are located in the `tests/` directory.



Run the tests with:



```bash

pytest

```



The tests cover:



* Health endpoint

* Valid CSV uploads

* Invalid datasets

* Unsupported file extensions

* Unreadable files



## Project Status



The backend provides a complete basic pipeline for uploading sales datasets, validating and cleaning the data, and generating business analytics through a FastAPI API.


The project is deployed and available through the live demo above.
