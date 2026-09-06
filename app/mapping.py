import pandas as pd


def column_mapping(df):

    column_mapping = {

        # =========================
        # Quantity sold
        # =========================

        "Quantity_Sold": "Quantity_Sold",
        "Quantity Sold": "Quantity_Sold",
        "quantity_sold": "Quantity_Sold",
        "quantity sold": "Quantity_Sold",
        "QUANTITY_SOLD": "Quantity_Sold",

        "Quantity": "Quantity_Sold",
        "quantity": "Quantity_Sold",
        "QTY": "Quantity_Sold",
        "Qty": "Quantity_Sold",
        "qty": "Quantity_Sold",

        "Qty Sold": "Quantity_Sold",
        "Qty_Sold": "Quantity_Sold",
        "qty sold": "Quantity_Sold",
        "qty_sold": "Quantity_Sold",

        "Units Sold": "Quantity_Sold",
        "Units_Sold": "Quantity_Sold",
        "units sold": "Quantity_Sold",
        "units_sold": "Quantity_Sold",

        "Units": "Quantity_Sold",
        "units": "Quantity_Sold",

        "Number Sold": "Quantity_Sold",
        "Number_Sold": "Quantity_Sold",

        "Items Sold": "Quantity_Sold",
        "Items_Sold": "Quantity_Sold",

        "Units Purchased": "Quantity_Sold",
        "Units_Purchased": "Quantity_Sold",

        "Quantity Sold": "Quantity_Sold",
        "Sold Quantity": "Quantity_Sold",
        "Sold_Quantity": "Quantity_Sold",

        # French
        "Quantité": "Quantity_Sold",
        "Quantite": "Quantity_Sold",
        "Quantité Vendue": "Quantity_Sold",
        "Quantite Vendue": "Quantity_Sold",
        "Quantité_Vendue": "Quantity_Sold",

        # German
        "Menge": "Quantity_Sold",
        "Verkaufte Menge": "Quantity_Sold",
        "Verkaufte_Menge": "Quantity_Sold",


        # =========================
        # Unit price
        # =========================

        "Unit_Price": "Unit_Price",
        "Unit Price": "Unit_Price",
        "unit_price": "Unit_Price",
        "unit price": "Unit_Price",
        "UNIT_PRICE": "Unit_Price",

        "Price": "Unit_Price",
        "price": "Unit_Price",

        "Item Price": "Unit_Price",
        "Item_Price": "Unit_Price",

        "Selling Price": "Unit_Price",
        "Selling_Price": "Unit_Price",

        "Sale Price": "Unit_Price",
        "Sale_Price": "Unit_Price",


        "Product Price": "Unit_Price",
        "Product_Price": "Unit_Price",

        "Price Per Unit": "Unit_Price",
        "Price_Per_Unit": "Unit_Price",

        # French
        "Prix": "Unit_Price",
        "Prix Unitaire": "Unit_Price",
        "Prix_Unitaire": "Unit_Price",
        "Prix de Vente": "Unit_Price",
        "Prix_De_Vente": "Unit_Price",

        # German
        "Preis": "Unit_Price",
        "Stückpreis": "Unit_Price",
        "Stueckpreis": "Unit_Price",


        # =========================
        # Sales amount / revenue
        # =========================

        "Sales_Amount": "Sales_Amount",
        "Sales Amount": "Sales_Amount",
        "sales_amount": "Sales_Amount",
        "sales amount": "Sales_Amount",
        "SALES_AMOUNT": "Sales_Amount",

        "Sales": "Sales_Amount",
        "sales": "Sales_Amount",

        "Revenue": "Sales_Amount",
        "revenue": "Sales_Amount",

        "Total Revenue": "Sales_Amount",
        "Total_Revenue": "Sales_Amount",
        "total revenue": "Sales_Amount",
        "total_revenue": "Sales_Amount",

        "Sales Revenue": "Sales_Amount",
        "Sales_Revenue": "Sales_Amount",

        "Total Sales": "Sales_Amount",
        "Total_Sales": "Sales_Amount",

        "Sales Value": "Sales_Amount",
        "Sales_Value": "Sales_Amount",

        "Sales Total": "Sales_Amount",
        "Sales_Total": "Sales_Amount",

        "Revenue Amount": "Sales_Amount",
        "Revenue_Amount": "Sales_Amount",

        "Net Sales": "Sales_Amount",
        "Net_Sales": "Sales_Amount",

        "Gross Sales": "Sales_Amount",
        "Gross_Sales": "Sales_Amount",

        "Turnover": "Sales_Amount",

        "Amount": "Sales_Amount",

        # French
        "Chiffre d'affaires": "Sales_Amount",
        "Chiffre d Affaires": "Sales_Amount",
        "Chiffre_Affaires": "Sales_Amount",
        "CA": "Sales_Amount",

        "Ventes": "Sales_Amount",
        "Montant des ventes": "Sales_Amount",
        "Montant_Des_Ventes": "Sales_Amount",
        "Revenu": "Sales_Amount",
        "Revenus": "Sales_Amount",

        # German
        "Umsatz": "Sales_Amount",
        "Verkaufsbetrag": "Sales_Amount",
        "Verkaufs_Betrag": "Sales_Amount",


        # =========================
        # Product category
        # =========================

        "Product_Category": "Product_Category",
        "Product Category": "Product_Category",
        "product_category": "Product_Category",
        "product category": "Product_Category",
        "PRODUCT_CATEGORY": "Product_Category",

        "Category": "Product_Category",
        "category": "Product_Category",

        "Product Type": "Product_Category",
        "Product_Type": "Product_Category",

        "Type": "Product_Category",

        "Product Group": "Product_Category",
        "Product_Group": "Product_Category",

        "Department": "Product_Category",
        "Department Name": "Product_Category",
        "Department_Name": "Product_Category",

        "Product Class": "Product_Category",
        "Product_Class": "Product_Category",

        "Product Segment": "Product_Category",
        "Product_Segment": "Product_Category",

        "Product Line": "Product_Category",
        "Product_Line": "Product_Category",

        # French
        "Catégorie": "Product_Category",
        "Categorie": "Product_Category",
        "Catégorie Produit": "Product_Category",
        "Categorie Produit": "Product_Category",
        "Catégorie_Produit": "Product_Category",

        "Type de Produit": "Product_Category",
        "Type_De_Produit": "Product_Category",

        "Département": "Product_Category",
        "Departement": "Product_Category",

        # German
        "Kategorie": "Product_Category",
        "Produktkategorie": "Product_Category",
        "Produkttyp": "Product_Category",


        # =========================
        # Region
        # =========================

        "Region": "Region",
        "region": "Region",
        "REGION": "Region",

        "Area": "Region",
        "area": "Region",

        "Location": "Region",
        "location": "Region",

        "Country": "Region",
        "country": "Region",

        "State": "Region",
        "state": "Region",

        "Territory": "Region",
        "territory": "Region",

        "Market": "Region",
        "market": "Region",

        "Sales Region": "Region",
        "Sales_Region": "Region",

        "Sales Area": "Region",
        "Sales_Area": "Region",

        "Geographic Region": "Region",
        "Geographic_Region": "Region",

        "Zone": "Region",
        "zone": "Region",

        "District": "Region",
        "district": "Region",

        # French
        "Région": "Region",
        "Region": "Region",

        "Zone Géographique": "Region",
        "Zone_Geographique": "Region",

        "Pays": "Region",

        "État": "Region",
        "Etat": "Region",

        # German
        "Region": "Region",
        "Gebiet": "Region",
        "Land": "Region",


        # =========================
        # Sale date
        # =========================

        "Sale_Date": "Sale_Date",
        "Sale Date": "Sale_Date",
        "sale_date": "Sale_Date",
        "sale date": "Sale_Date",
        "SALE_DATE": "Sale_Date",

        "Date": "Sale_Date",
        "date": "Sale_Date",

        "Sales Date": "Sale_Date",
        "Sales_Date": "Sale_Date",
        "sales_date": "Sale_Date",

        "Transaction Date": "Sale_Date",
        "Transaction_Date": "Sale_Date",
        "transaction_date": "Sale_Date",

        "Order Date": "Sale_Date",
        "Order_Date": "Sale_Date",
        "order date": "Sale_Date",

        "Purchase Date": "Sale_Date",
        "Purchase_Date": "Sale_Date",
        "purchase date": "Sale_Date",

        "Invoice Date": "Sale_Date",
        "Invoice_Date": "Sale_Date",

        "Billing Date": "Sale_Date",
        "Billing_Date": "Sale_Date",

        "Created Date": "Sale_Date",
        "Created_Date": "Sale_Date",

        # French
        "Date de Vente": "Sale_Date",
        "Date_De_Vente": "Sale_Date",

        "Date de Transaction": "Sale_Date",
        "Date_De_Transaction": "Sale_Date",

        "Date de Commande": "Sale_Date",
        "Date_De_Commande": "Sale_Date",

        # German
        "Verkaufsdatum": "Sale_Date",
        "Transaktionsdatum": "Sale_Date",
        "Bestelldatum": "Sale_Date",
    }

    return df.rename(columns=column_mapping)