# Walmart Analytics:  Data Transformation and Business Intelligence using Azure and Power BI 

## Project Objective

Efficiently ingest Walmart's diverse datasets into Azure Blob Storage. The data quality is ensured through preliminary cleansing tasks, addressing deduplication and null values. Utilize Azure Databricks for intricate data transformations, Optimize and store the transformed Walmart data in Azure Blob Storage for subsequent analysis and visualization in Power BI, aiming to derive actionable business intelligence insights.
## Overview
1.	Data Ingestion: Azure Databricks ingests raw data directly into Cloud from diverse sources.
2.	Initial Data Cleansing: Azure Databricks performs preliminary cleansing tasks like deduplication and null value handling using pandas.
3.	Data Transformation: The cleansed data is then processed by Azure Databricks, where complex transformations, including tax calculations and category splitting, are conducted.
4.	Processed Data Storage: The transformed data is written back to Azure Blob Storage in an optimized format for further analysis or visualization.
5.	Visualization: Power BI connects to the processed data to create interactive visualizations and reports that provide business intelligence and insights.


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
