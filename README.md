# End-to-End Data Analysis Project

## Project Objective

The objective of this end-to-end project is to analyze historical stock data, customer purchasing behavior, sales performance, and inventory trends using a dataset consisting of three CSV files: stock, transactional, and inventory. The project aims to extract, transform, and load (ETL) data from these CSV files using Azure Data Factory and then visualize the insights gained from the analysis in Power BI.

## Key Objectives

### Data Extraction

- Extract data from the stock, transactional, and inventory CSV files stored in Azure Data Lake Gen2 using Azure Data Factory.

### Data Transformation

- Apply transformations to the datasets to derive meaningful insights.
  - For stock data, calculate the percentage change in stock prices.
  - For transactional data, apply a 5% tax and calculate the total cost of transactions.
  - For inventory data, separate the data based on department and category.

### Data Loading

- Load the transformed data into Azure SQL Database using Azure Data Factory.

### Visualization

- Connect Power BI to Azure SQL Database to import the transformed data.
- Design Power BI reports and dashboards to visualize insights from stock, transactional, and inventory data.

### Analysis and Insights

- Analyze historical stock data to gain insights into stock behavior.
- Explore customer purchasing behavior, sales performance, product popularity, and the effectiveness of the membership program using transactional data.
- Gain insights into inventory trends by department and category.
