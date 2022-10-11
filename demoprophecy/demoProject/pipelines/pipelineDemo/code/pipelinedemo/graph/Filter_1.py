from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pipelinedemo.config.ConfigStore import *
from pipelinedemo.udfs.UDFs import *

def Filter_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.filter((year(col("order_date")) == lit(2019)))
