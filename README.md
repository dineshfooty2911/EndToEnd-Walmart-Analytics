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
Role in Project: Comprehensive Data Processing, Cleansing, Transformation, and data movement
### Value to Project:
*Unified Data Processing Workflow*: By leveraging Databricks for both data cleansing and transformation, the project benefits from a streamlined and integrated data processing workflow. This unified approach simplifies management and improves efficiency.
**Ensures Data Quality:** Databricks' comprehensive data cleansing and transformation processes ensure that the data is of high quality. This is essential for conducting accurate downstream analysis and making informed decisions.
Maximizes Processing Capabilities: The powerful analytics engine of Databricks maximizes data processing capabilities. This allows for efficient handling of large datasets and complex computational tasks, making it ideal for big data projects.
Enhances Analytical Accuracy: The high-quality data obtained from rigorous cleansing and transformation in Databricks leads to more accurate and reliable analytical models and insights. This enhances the overall effectiveness of data-driven strategies.
Efficient Data Movement and Integration: Databricks facilitates efficient data movement and integration. It seamlessly ingests data from various sources and integrates it into a cohesive dataset, ready for analysis. This capability is crucial for projects that rely on diverse data sources, ensuring that data is not only moved efficiently but also harmonized effectively within the Databricks environment.
By focusing on these key areas, Azure Databricks provides a robust and versatile platform for handling all aspects of data management in your project, from ingestion and cleansing to transformation and analysis. This comprehensive approach not only streamlines the data workflow but also ensures the reliability and accuracy of the insights derived from the data.


### Visualization

- Connect Power BI to Azure SQL Database to import the transformed data.
- Design Power BI reports and dashboards to visualize insights from stock, transactional, and inventory data.

### Analysis and Insights

- Analyze historical stock data to gain insights into stock behavior.
- Explore customer purchasing behavior, sales performance, product popularity, and the effectiveness of the membership program using transactional data.
- Gain insights into inventory trends by department and category.
