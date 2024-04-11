# Databricks notebook source
# MAGIC %sh
# MAGIC ls /Workspace/Users/jgarmor535w@ieszaidinvergeles.org/SistemasFicheros

# COMMAND ----------

# Import the pandas library
import pandas as pd

# Specify the path to the CSV file
file_path = "/Workspace/Users/jgarmor535w@ieszaidinvergeles.org/customer.csv"

# Read the CSV file using pandas
df = pd.read_csv(file_path, sep="|", header=0)

display(df)
