# Databricks notebook source
# MAGIC %sql
# MAGIC /*Crear un volumne*/
# MAGIC CREATE CATALOG volumenes;
# MAGIC CREATE SCHEMA volumenes.csv;
# MAGIC CREATE VOLUME volumenes.csv.files;

# COMMAND ----------

df = spark.read.option("header","True").option("delimiter", "|").csv("/Volumes/volumenes/csv/files/inventory.csv")
display(df)


# COMMAND ----------

# Filter dataframe by specific column value
filtered_df = df.filter(df.inventory_id == 17)
display(filtered_df)


# COMMAND ----------

# Write the dataframe as a CSV file with header and pipe separator to volume
filtered_df.write.option("header", "True").option("delimiter", "|").csv("/Volumes/volumenes/csv/files/inventory_output.csv")
