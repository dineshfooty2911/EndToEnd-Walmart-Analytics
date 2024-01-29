# Databricks notebook source
# MAGIC %fs

# COMMAND ----------

import pandas as pd
    
df1 = pd.read_csv("/dbfs/FileStore/shared_uploads/sarul013@uottawa.ca/walmart_Stock.csv") #stockdata

# COMMAND ----------

df1

# COMMAND ----------

#to check repeated data 
column_to_check = 'Date'  # Replace with the name of your column
duplicates = df1[df1.duplicated(column_to_check, keep=False)] #checking if duplicates exists 
df_unique = df1.drop_duplicates(subset=[column_to_check], keep='first')
df1['Date'] = pd.to_datetime(df1['Date'], format='%d-%b-%y')
df_sorted = df1.sort_values(by='Date', ascending=True)
null_values = df1.isnull().sum()
print(null_values)
df_sorted

# COMMAND ----------

df2 = pd.read_csv("/dbfs/FileStore/shared_uploads/sarul013@uottawa.ca/walmart_Transactional.csv")

# COMMAND ----------

df2 = pd.read_csv("/dbfs/FileStore/shared_uploads/sarul013@uottawa.ca/walmart_Transactional-1.csv")
df2.head()

# COMMAND ----------

column_to_check = 'Invoice ID'  # Replace with the name of your column
duplicates = df2[df2.duplicated(column_to_check, keep=False)] #checking if duplicates exists 
print(duplicates)
null_values = df2.isnull().sum()
print(null_values)


# COMMAND ----------

df3 = pd.read_csv("/dbfs/FileStore/shared_uploads/sarul013@uottawa.ca/Walmart_inventorydata.csv") 
df3.head()
null_values = df2.isnull().sum()
print(null_values)


# COMMAND ----------

from pyspark.sql import SparkSession
import pandas as pd

# Create a SparkSession
spark = SparkSession.builder.getOrCreate()

# Assuming df1 is a pandas DataFrame
if 'df1' in locals() or 'df1' in globals():
    # Convert pandas DataFrame to PySpark DataFrame
    spark_df1 = spark.createDataFrame(df_sorted)

    # Now save the PySpark DataFrame as a parquet file
    spark_df1.write.mode('overwrite').format("parquet").save("/mnt/data/df1.parquet")
else:
    print("DataFrame 'df1' does not exist.")


# COMMAND ----------

from pyspark.sql import SparkSession
import pandas as pd

# Create a SparkSession
spark = SparkSession.builder.getOrCreate()

# Assuming df1 is a pandas DataFrame
if 'df2' in locals() or 'df2' in globals():
    # Convert pandas DataFrame to PySpark DataFrame
    spark_df1 = spark.createDataFrame(df2)

    # Now save the PySpark DataFrame as a parquet file
    spark_df1.write.mode('overwrite').format("parquet").save("/mnt/data/df2.parquet")
else:
    print("DataFrame 'df2' does not exist.")

# COMMAND ----------

from pyspark.sql import SparkSession
import pandas as pd

# Create a SparkSession
spark = SparkSession.builder.getOrCreate()

# Assuming df1 is a pandas DataFrame
if 'df3' in locals() or 'df3' in globals():
    # Convert pandas DataFrame to PySpark DataFrame
    spark_df3 = spark.createDataFrame(df3)

    # Now save the PySpark DataFrame as a parquet file
    spark_df3.write.mode('overwrite').format("parquet").save("/mnt/data/df3.parquet")
else:
    print("DataFrame 'df3' does not exist.")
