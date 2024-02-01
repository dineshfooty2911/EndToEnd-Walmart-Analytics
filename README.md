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

## Data Ingestion in Azure Databricks
*Kaggle Dataset Download:* Accessed the Kaggle platform to acquire the Walmart dataset and prepared the dataset by downloading it to a local environment, gearing up for the data ingestion process.

*Databricks Configuration:* Configured a Databricks workspace, tailoring it for the specific needs of the Walmart dataset processing.

*Direct Data Upload:* Uploaded the Walmart dataset directly into Databricks, bypassing Azure Blob Storage. This direct approach streamlined the process, allowing for immediate access to the data within the Databricks environment.

## Data Cleaning using Databricks:
Leveraging Databricks' robust data processing capabilities, the Walmart dataset underwent thorough cleaning to ensure data quality and reliability. 

The cleaning process involved:

**Null Value Treatment:**
*Identification:* Utilized Databricks’ powerful data processing tools to identify null or missing values within the dataset.

*Handling:* Implemented strategies like imputing default values or removing incomplete rows, tailored to the dataset's characteristics and the project's requirements.

**De-duplication:**

*Detection:* Employed Databricks’ functionalities to detect duplicate entries in the dataset.

*Resolution:* Applied data manipulation techniques to remove or merge duplicates, ensuring the integrity and uniqueness of the dataset.

By directly ingesting the dataset into Databricks, the workflow was significantly simplified, enabling a more efficient data processing pipeline. The advanced data manipulation features of Databricks were fully utilized to clean and prepare the Walmart dataset for subsequent analysis and insights generation. This approach emphasizes the versatility and efficiency of Databricks in handling complex data tasks, from ingestion to cleaning, in a unified environment.

## Data Transformation 

Azure Databricks is also used in advanced transformations. Here's a simplified glimpse of why Databricks is the project virtuoso:

**Maximizes Data Processing Capabilities:**

•	Databricks is engineered to handle complex data processing tasks with ease. Its ability to manage large volumes of data and intricate transformations makes it an ideal choice for comprehensive data analytics.

•	By leveraging the powerful Spark engine, Databricks optimizes data processing, ensuring that analytics are performed efficiently and effectively. This leads to faster insights and more dynamic data manipulation capabilities.

**Enhances Analytical Accuracy:**
•	The initial phase of data cleaning and preparation in Databricks sets the stage for high-quality analytics. By ensuring the data is precise and cleansed, Databricks creates a robust foundation for subsequent analysis.

Azure Databricks serves as a crucial tool in your project, adeptly handling complex transformations and elevating the quality of analytics.

In this project, data transformation plays a pivotal role in refining the raw datasets into forms that are more suitable for analysis. Using Azure Databricks, specific transformation tasks are applied to the Walmart datasets, enhancing their analytical value.

**Objectives of Data Transformation:**
*Enhance Data Accuracy:* Refine and correct the data to improve its accuracy for analysis.
*Facilitate Analysis:* Transform the data into formats that are easier to analyze and interpret.
*Data Integration and Segmentation:* Split and combine data to achieve a more comprehensive analytical view.

### Transformation Tasks:

**Stock Dataset:**
Script Used:
```
df1 = pd.read_parquet("/dbfs/mnt/data/df1.parquet")
df1['Percentage Change'] = (df1['Price'].pct_change() * 100).abs().round(2)
```

**Key Transformations:**
•	Calculate the absolute percentage change in stock price, providing a clearer view of price fluctuations.

•	Conversion of the stock data into a format more conducive for time-series analysis.

Inventory Dataset:
Script Used:
df3 = pd.read_parquet("/dbfs/mnt/data/df3.parquet")
df3['DEPARTMENT'], df3['CATEGORY'] = df3['BREADCRUMBS'].str.split('/', 1).str
Key Transformations:
•	Split 'BREADCRUMBS' into two separate columns, 'DEPARTMENT' and 'CATEGORY', for more granular analysis.
•	This approach simplifies categorical analysis and enhances data clarity.
Transactional Dataset:
Script Used:
df2 = pd.read_parquet("/dbfs/mnt/data/df2.parquet")
df2['Tax (10%)'] = df2['Unit price'] * df2['Quantity'] * 0.10
df2['Total Price'] = df2['Unit price'] * df2['Quantity'] + df2['Tax (10%)']
Key Transformations:
•	Calculation of tax for each transaction, providing a more comprehensive view of the transactional costs.
•	Computation of the total price, including tax, for each transaction, essential for revenue analysis.

These transformation scripts are executed within Databricks notebooks, ensuring a streamlined and automated process. The transformation logic is tailored specifically to the needs of each dataset, demonstrating the flexibility of Databricks.



