import pyspark.sql.functions as F
from pyspark.sql import SparkSession

# Initialize a SparkSession
spark = SparkSession.builder.appName("ParquetColumnRemoval").getOrCreate()

# Read the original Parquet file
df = spark.read.parquet("/home/ubuntu/Downloads/spline-poc-spark/datacamp_courses.parquet")

# Column to remove
column_to_remove = "_c5"

# Select the desired columns (excluding the one you want to remove)
df_filtered = df.select([col for col in df.columns if col != column_to_remove])

# Save the modified DataFrame as a new Parquet file
df_filtered.write.mode("overwrite").parquet("/home/ubuntu/Downloads/spline-poc-spark/output.parquet")

# Stop the Spark session
spark.stop()

