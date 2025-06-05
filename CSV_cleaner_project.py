import pandas as pd
import numpy as np

## ## ## This is a project for data cleaning ## ## ##

## I want to use this data to find out which products are sold the most and bring most revenue, 
## and which products are not so much (ie we can reduce their stock)

filename = "C:\PYTHON STUDY\CSV_cleaner\dirty_cafe_sales.csv"
df = pd.read_csv(filename)

## Checking how sample data looks like:
print(df.head(3))

## Checking how many rows and columns in the dataset:
print("The dataset contains", df.shape[0], " rows and ", df.shape[1], "columns")

## Checking if I have duplicated rows with aim to delete any if exists (result - no duplicated rows):
print(df.loc[df.duplicated(), :])

## Checking unique values for 'Item' column:
print(df["Item"].value_counts(dropna = False))

## For the purpose of this project I can delete these rows where Item is missing, Unknown or error:
linesToDrop = df[(df["Item"] == "UNKNOWN") | (df["Item"] == "ERROR") | (df["Item"].isna())].index
df.drop(linesToDrop , inplace=True)

## Double checking it's deleted:
print(df["Item"].value_counts(dropna = False))

## Checking unique values for 'Quantity', 'Price Per Item', 'Total Spent' columns one by one:
print(df["Quantity"].value_counts(dropna = False))
print(df["Price Per Unit"].value_counts(dropna = False))
print(df["Total Spent"].value_counts(dropna = False))

## Converting 'Quantity' column to Int64:
df["Quantity"] = pd.to_numeric(df["Quantity"], errors = "coerce").astype('Int64')
## Converting 'Proce Per Unit', 'Total Spent' columns numeric data type:
df["Price Per Unit"] = pd.to_numeric(df["Price Per Unit"].str.replace(',','.',regex = False), errors = "coerce")
df["Total Spent"] = pd.to_numeric(df["Total Spent"].str.replace(',','.',regex = False), errors = "coerce")

## Checking for unique combinations of 'Item' and 'Price Per Unit'. If each Item has only one corresponding price, 
## then we can safely fill in missing values in the 'Price Per Unit' column by using the known price for that Item from other rows.
unique_prices = df[['Item', 'Price Per Unit']].dropna().drop_duplicates().sort_values(by = "Item")
print(unique_prices)
df = df.merge(unique_prices, on = "Item", how = "left", suffixes = ("","_new"))
df["Price Per Unit"] = df["Price Per Unit"].fillna(df["Price Per Unit_new"])
df.drop(columns= "Price Per Unit_new", inplace = True)

## We can calculate missing 'Quantity' column values if we have values in both 'Total Spent' and 'Price Per Unit' columns:
filtered = df['Quantity'].isna() & df['Total Spent'].notna() & df['Price Per Unit'].notna()
df.loc[filtered, 'Quantity'] = df['Total Spent'] / df['Price Per Unit']

## We can calculate missing 'Total Spent' column values if we have values in both 'Price Per Unit' and 'Quantity' columns:
filtered = df['Total Spent'].isna() & df['Price Per Unit'].notna() & df['Quantity'].notna()
df.loc[filtered, 'Total Spent'] = df['Price Per Unit'] * df['Quantity']

## After above calculations 
linesToDrop = df[(df["Quantity"].isna()) | (df["Total Spent"].isna())].index
df.drop(linesToDrop , inplace=True)

## Checking unique values in 'Payment Method' column:
print(df["Payment Method"].value_counts(dropna = False))
## For the purpose of this project, the 'Payment Method' column is not needed.
## Since it also contains many missing values, I'll drop the entire column.
df.drop("Payment Method", inplace = True, axis = 1)

## Checking unique values in 'Location' column:
print(df["Location"].value_counts(dropna = False))
## For the purpose of this project, the 'Location' column is not needed.
## Since it also contains many missing values, I'll drop the entire column.
df.drop("Location", inplace = True, axis = 1)

print(df.head(3))

## Checking unique values in 'Transaction Date' column and converting them to datetime:
print(df["Transaction Date"].value_counts(dropna = False))
df["Transaction Date"] = pd.to_datetime(df["Transaction Date"], errors = "coerce")

## Sorting data by 'Transaction ID' column:
df.sort_values(by='Transaction ID', inplace= True)

print(df.dtypes)

## Writing cleaned data to a new file:
df.to_csv("C:\PYTHON STUDY\CSV_cleaner\clean_cafe_sales.csv", index=False)


