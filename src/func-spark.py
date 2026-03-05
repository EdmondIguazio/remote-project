from pyspark.sql import SparkSession
from mlrun import get_or_create_ctx
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

def handler(context):

  # build spark session
  spark = SparkSession.builder.appName("Spark job").getOrCreate()

  schema = StructType([
    StructField("id",     IntegerType(), False),
    StructField("name",   StringType(),  True),
    StructField("age",    IntegerType(),  True),
    StructField("salary", DoubleType(),   True),
    StructField("city",   StringType(),   True),
  ])

  data = [
    (1, "Alice",   30, 75000.0, "New York"),
    (2, "Bob",     25, 55000.0, "London"),
    (3, "Charlie", 35, 90000.0, "San Francisco"),
    (4, "Diana",   28, 62000.0, "Berlin"),
    (5, "Eve",     42, 110000.0, "Tokyo"),
  ]

  df = spark.createDataFrame(data, schema=schema)

  df.show()
  
  spark.stop()
