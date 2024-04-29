from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("ReadCSV").getOrCreate()

# Define the path to your CSV file
file_path = "/home/ubuntu/Downloads/spline-poc-spark/datacamp_courses.csv"

# Read the CSV file into a DataFrame
df = spark.read.csv(file_path)

# Optionally, specify additional options while reading the file
# For example, to specify that the first row contains column names:
# df = spark.read.csv(file_path, header=True)

# View the first few rows of the DataFrame
df.show(5)

# Use the DataFrame for further analysis
# Assuming you already have a SparkSession and DataFrame (df) created...

# Save the DataFrame as a CSV file
df.write.mode("overwrite").parquet("/home/ubuntu/Downloads/spline-poc-spark/datacamp_courses.parquet")

# Stop the SparkSession
spark.stop()
