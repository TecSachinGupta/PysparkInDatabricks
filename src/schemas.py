# Databricks notebook source
from pyspark.sql.types import StructType, StructField, StringType, LongType, DateType

# COMMAND ----------

product_schema = StructType([
    StructField("product_id", LongType(), False), \
    StructField("product_name", StringType(), False), \
    StructField("price", LongType(), False)
])

# COMMAND ----------

sales_schema = "order_id bigint, product_id bigint, seller_id bigint, date date, num_pieces_sold bigint, bill_raw_text string"

# COMMAND ----------

sellers_schema = "seller_id bigint, seller_name string, daily_target bigint"
