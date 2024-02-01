# Walmart Analytics:  Data Transformation and Business Intelligence using Azure and Power BI 

## Project Objective

Efficiently ingest Walmart's diverse datasets into Azure Blob Storage. The data quality is ensured through preliminary cleansing tasks, addressing deduplication and null values. Utilize Azure Databricks for intricate data transformations, Optimize and store the transformed Walmart data in Azure Blob Storage for subsequent analysis and visualization in Power BI, aiming to derive actionable business intelligence insights.
## Overview
1.	Data Ingestion: Azure Databricks ingests raw data directly into Cloud from diverse sources.
2.	Initial Data Cleansing: Azure Databricks performs preliminary cleansing tasks like deduplication and null value handling using pandas.
3.	Data Transformation: The cleansed data is then processed by Azure Databricks, where complex transformations, including tax calculations and category splitting, are conducted.
4.	Processed Data Storage: The transformed data is written back to Azure Blob Storage in an optimized format for further analysis or visualization.
5.	Visualization: Power BI connects to the processed data to create interactive visualizations and reports that provide business intelligence and insights.

## FlowChart
[flowdiagram.jpg](https://github.com/dineshfooty2911/EndToEnd-Walmart-Analytics/blob/b9498651ee004672f02cc06b9e1a24b254537f60/flowdiagram.jpg)
## Azure services used in the project.

### Azure Databricks
**Role in Project:** Comprehensive Data Processing, Cleansing, Transformation, and data movement
### Value to Project:
*Unified Data Processing Workflow*: By leveraging Databricks for both data cleansing and transformation, the project benefits from a streamlined and integrated data processing workflow. This unified approach simplifies management and improves efficiency.

*Ensures Data Quality:* Databricks' comprehensive data cleansing and transformation processes ensure that the data is of high quality. This is essential for conducting accurate downstream analysis and making informed decisions.

*Maximizes Processing Capabilities:* The powerful analytics engine of Databricks maximizes data processing capabilities. This allows for efficient handling of large datasets and complex computational tasks, making it ideal for big data projects.

*Enhances Analytical Accuracy:* The high-quality data obtained from rigorous cleansing and transformation in Databricks leads to more accurate and reliable analytical models and insights. This enhances the overall effectiveness of data-driven strategies.

*Efficient Data Movement and Integration:* Databricks facilitates efficient data movement and integration. It seamlessly ingests data from various sources and integrates it into a cohesive dataset, ready for analysis. This capability is crucial for projects that rely on diverse data sources, ensuring that data is not only moved efficiently but also harmonized effectively within the Databricks environment.

By focusing on these key areas, Azure Databricks provides a robust and versatile platform for handling all aspects of data management in your project, from ingestion and cleansing to transformation and analysis. This comprehensive approach not only streamlines the data workflow but also ensures the reliability and accuracy of the insights derived from the data.


 # Data Understanding
Each dataset is unique and offers distinct insights into Walmart's operations.

### 1.Stock Data:
**Data Description**: The dataset provides a detailed view of stock price fluctuations over time.
**Columns:** 
•	Date: The date of the stock record (datetime format).
•	Price: The closing price of the stock for the given date (numeric).
•	Open: The opening price of the stock on that day (numeric).
•	High: The highest price of the stock on that day (numeric).
•	Low: The lowest price of the stock on that day (numeric).
•	Vol: The volume of stocks traded on that day(numeric).
•	Percentage Change: The percentage change in the stock price compared to the previous day (numeric).
### 2.Inventory Data: 
**Data Description**: This dataset provides the information about the inventory, including product assortment and pricing.
**Columns:**  
•	Index: A numerical index or identifier for the record.
•	SHIPPING_LOCATION: The numeric code representing the location of shipping.
•	PRODUCT_NAME: The name of the product (string).
•	BRAND: The brand of the product (string).
•	PRICE_RETAIL: The retail price of the product (numeric).
•	PRODUCT_SIZE: The size of the product (numeric, assumed to be in standard units).
•	DEPARTMENT: The department to which the product belongs (string).
•	CATEGORY: The specific category of the product (string).
### 3. Transactional Data:
**Data Description:**  This dataset offers a comprehensive overview of sales transactions, encompassing customer demographics, purchasing details, and financials.
**Columns:** 
•	Invoice ID: A unique identifier for each transaction (string).
•	Branch: The branch of Walmart where the transaction occurred (string).
•	City: The city in which the branch is located (string).
•	Customer type: Type of customer (e.g., Normal, Member) (string).
•	Gender: Gender of the customer (string).
•	Product line: The line of product purchased (string).
•	Unit price: Price per unit of the product (numeric).
•	Quantity: The number of units purchased (numeric).
•	Date: The date of the transaction (datetime format).
•	Payment: The mode of payment used (string).
•	Tax (10%): The tax applied to the transaction (numeric).
•	Total Price: The total price of the transaction, including tax (numeric).
### Value to Project:
•	Comprehensive Analysis: These datasets collectively offer a multifaceted view of Walmart's operations, from stock levels and inventory management to customer transactions.
•	Data-Driven Insights: Understanding these datasets allows for deeper analysis and more accurate business intelligence insights, such as inventory optimization, sales trends, and customer behavior analysis.
•	Quality Control: Assessing the quality of these datasets upfront aids in ensuring the reliability of any conclusions drawn from the data.
•	By thoroughly understanding these datasets, we lay the groundwork for meaningful data analysis, ensuring that the insights derived are both accurate and actionable.

- Gain insights into inventory trends by department and category.
