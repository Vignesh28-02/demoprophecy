from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pipelinedemo.config.ConfigStore import *
from pipelinedemo.udfs.UDFs import *

def OrdersDatasetOutput(spark: SparkSession, in0: DataFrame):
    in0.write\
        .option("header", True)\
        .option("sep", ",")\
        .mode("error")\
        .option("separator", ",")\
        .option("header", True)\
        .csv("dbfs:/Prophecy/vickyviji3546@gmail.com/")
