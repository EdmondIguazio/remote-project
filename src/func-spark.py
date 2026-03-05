from pyspark.sql import SparkSession
from mlrun import get_or_create_ctx

def handler(context):

  # build spark session
  spark = SparkSession.builder.appName("Spark job").getOrCreate()

  spark.stop()
