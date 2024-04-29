import pyspark.sql.functions as F
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, concat, lit

# Initialize a SparkSession
spark = SparkSession.builder.appName("ParquetColumnRemoval").getOrCreate()

# Read the original Parquet file
df = spark.read.parquet("/home/ubuntu/Downloads/spline-poc-spark/datacamp_courses.parquet")

# Column to remove
column_to_remove = "_c5"

# Select the desired columns (excluding the one you want to remove)
df_filtered = df.select([col for col in df.columns if col != column_to_remove])
# Append new string into one of the column
df_edited = df_filtered.withColumn("_c0_edited", concat(col("_c0"), lit("_edited")))
# Save the modified DataFrame as a new Parquet file
df_edited.write.mode("overwrite").parquet("/home/ubuntu/Downloads/spline-poc-spark/output_with_c0_edited.parquet")

# Stop the Spark session
spark.stop()

