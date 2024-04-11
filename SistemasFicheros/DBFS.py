# Databricks notebook source
dbutils.help()

# COMMAND ----------

display(dbutils.fs.ls("dbfs:/"))

# COMMAND ----------

display(dbutils.fs.ls("dbfs:/databricks-datasets/adult/"))

# COMMAND ----------

display(dbutils.fs.head("dbfs:/databricks-datasets/adult/adult.data"))

# COMMAND ----------

df = spark.read.csv("dbfs:/databricks-datasets/adult/adult.data", header=False, inferSchema=True)
display(df)

# COMMAND ----------

df = spark.read.option("header","True").option("delimiter", "|").csv("dbfs:/FileStore/tables/customer.csv")
display(df)
