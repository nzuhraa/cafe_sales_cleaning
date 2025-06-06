Cafe Sales Data Cleaning Project

Project Description
This project focuses on cleaning and preparing a raw sales dataset from a cafe for further analysis. The original data contains inconsistencies such as missing values, incorrect types, and invalid entries.

Goal
The aim is to clean the data to identify:
Which items are sold the most
Which items generate the most revenue
What items are underperforming (for stock optimization)

Data Cleaning Steps
Removed rows with missing or invalid product names (UNKNOWN, ERROR, or NaN)
Converted columns to proper types
Filled missing prices based on known values for the same items (previously making sure that there is only 1 associated price per item)
Recalculated missing quantities or total spent values where possible
Removed columns with too many missing values or irrelevant for the analysis (e.g. Payment Method, Location)
Sorted by Transaction ID
Exported the cleaned dataset to a new CSV file

Files
dirty_cafe_sales.csv: Raw data
clean_cafe_sales.csv: Cleaned output
CSV_cleaner_project.py: Python code for cleaning the data

Tools Used
Python (Pandas, NumPy)
LibreOffice (for viewing CSV)
Git & GitHub (for version control)
