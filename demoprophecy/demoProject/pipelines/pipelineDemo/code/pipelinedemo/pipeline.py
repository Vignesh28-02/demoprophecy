from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pipelinedemo.config.ConfigStore import *
from pipelinedemo.udfs.UDFs import *
from prophecy.utils import *
from pipelinedemo.graph import *

def pipeline(spark: SparkSession) -> None:
    df_OrdersDataset = OrdersDataset(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "3574/pipelines/pipelineDemo")
    MetricsCollector.start(spark = spark, pipelineId = "3574/pipelines/pipelineDemo")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
