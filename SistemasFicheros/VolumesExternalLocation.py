# Databricks notebook source
# MAGIC %sql
# MAGIC /*Crear el esquema*/
# MAGIC CREATE SCHEMA volumenes.json;
# MAGIC /*Crear el volumen con la dirección de abfss*/
# MAGIC CREATE EXTERNAL VOLUME volumenes.json.files
# MAGIC LOCATION 'abfss://volumes@externalnovacjm.dfs.core.windows.net/volume01'

# COMMAND ----------

# Load json file into dataframe
df = spark.read.json("/Volumes/volumenes/json/files/response.json")

