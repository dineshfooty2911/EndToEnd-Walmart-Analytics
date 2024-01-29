# Databricks notebook source
import pandas as pd
df1 = pd.read_parquet("/dbfs/mnt/data/df1.parquet")


# Replace negative and zero values with NaN or zero (depending on your preference)
df1['Percentage Change'] = (df1['Price'].pct_change() * 100).abs().round(2)
df1.head()

# COMMAND ----------


df3 = pd.read_parquet("/dbfs/mnt/data/df3.parquet")
df3['DEPARTMENT'], df3['CATEGORY'] = df3['BREADCRUMBS'].str.split('/', 1).str
df3

# COMMAND ----------

df2 = pd.read_parquet("/dbfs/mnt/data/df2.parquet")
# Calculate the tax for each item
df2['Tax (10%)'] = df2['Unit price'] * df2['Quantity'] * 0.10

# Calculate the total price (unit price * quantity + tax)
df2['Total Price'] = df2['Unit price'] * df2['Quantity'] + df2['Tax (10%)']
df2

# COMMAND ----------

# Split the 'BREADCRUMBS' column into 'DEPARTMENT' and 'CATEGORY' based on the first '/'
df3[['DEPARTMENT', 'CATEGORY']] = df3['BREADCRUMBS'].str.split('/', n=1, expand=True)

# If the BREADCRUMBS contain more than one '/', you might want to split by comma
# df3[['DEPARTMENT', 'CATEGORY']] = df3['BREADCRUMBS'].str.split(',', n=1, expand=True)
df3.drop('BREADCRUMBS', axis=1, inplace=True)
df3

# COMMAND ----------

from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder.getOrCreate()

# Your DataFrame object
df1 = spark.createDataFrame(df1) 

# Save DataFrame as a Parquet table

df1.write.format("parquet").saveAsTable("StockData")

# COMMAND ----------

from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder.getOrCreate()

# Your DataFrame object
df2 = spark.createDataFrame(df2) 

# Save DataFrame as a Parquet table

df2.write.format("parquet").saveAsTable("TransactionalData")

# COMMAND ----------

from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder.getOrCreate()

# Your DataFrame object
df3 = spark.createDataFrame(df3) 

# Save DataFrame as a Parquet table

df1.write.format("parquet").saveAsTable("InventoryData")
