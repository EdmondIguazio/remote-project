from ai4d.validation.validators.local import validate
from ai4d.validation.rule import CheckType, ColumnType, DescriptionRule
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

def handler(context):

    spark = SparkSession.builder.getOrCreate()
    df = spark.createDataFrame([
            ("Alice", 25, "Gold"),
            ("Bob", 35, "Silver"),
            ("Charlie", 45, "Bronze"),
        ], ["name", "age", "customer_type"])

    # Define validation rules
    rules = [
         DescriptionRule(
             rule_id=None,
             check="validation",
             for_validation=True,
             for_correction=False,
             table="customers",
             column_name="age",
             column_type=ColumnType.NUMBER,
             operator=CheckType.IN_RANGE,
             value=(18, 65),
             filters=None,
         ),
         DescriptionRule(
             rule_id=None,
             check="validation",
             for_validation=True,
             for_correction=False,
             table="customers",
             column_name="customer_type",
             column_type=ColumnType.STRING,
             operator=CheckType.EQUAL,
             value="Gold",
             filters=F.col("age") >= 30,
         ),
     ]

    # Validate the DataFrame
    result = validate(df, rules, return_error_df=True)
    context.logger.info(f"Validated {result.num_validated} rules, found {result.num_errors} error")
    context.logger.info(f"Validation score: {result.score}")
