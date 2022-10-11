from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pipelinedemo.config.ConfigStore import *
from pipelinedemo.udfs.UDFs import *

def OrdersDataset(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("order_id", StringType(), True), StructField("customer_id", StringType(), True), StructField("order_status", StringType(), True), StructField("order_category", StringType(), True), StructField("order_date", StringType(), True), StructField("amount", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/Prophecy/vickyviji3546@gmail.com/OrdersDatasetInput.csv")
