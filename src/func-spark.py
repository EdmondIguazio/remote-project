from pyspark.sql import SparkSession
from mlrun import get_or_create_ctx

def handler(context):

  # build spark session
  spark = SparkSession.builder.appName("Spark job").getOrCreate()

  # read csv
  df = spark.read.load('iris.csv', format="csv",
                       sep=",", header="true")
  
  # sample for logging
  df_to_log = df.describe().toPandas()
  
  # log final report
  context.log_dataset("df_sample",
                       df=df_to_log,
                       format="csv")
  spark.stop()
