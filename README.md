## End to end project

Dataset -stock, transactional, inventory

Stock data - By analyzing this historical stock data, you can gain insights into the past behavior of the stock, which can help in making informed decisions for future investments.

Transactional data - This dataset is used to analyze customer purchasing behavior, sales performance, product popularity, and the effectiveness of the membership program, among other insights.
Inventory data -  

Tools used - Azure data factory, azure lake Gen 2, azure SQL database, Power BI



## Extract

The csv file in the Azure Lake gen is loaded to azure data factory source.

## Transformation 

Stock – find the percentage of change
transactional – tax (5%), total cost 
Inventory – separate department and category

## Load

The transformed data is loaded into the Azure SQL database 
From the SQL database the data is exported to power BI and visualized 


