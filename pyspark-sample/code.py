from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("ReadCSV").getOrCreate()

# Define the path to your CSV file
file_path = "/Users/boni.nugraha/Downloads/pyspark-poc/datacamp_courses.csv"

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
df.write.format("csv").option("header", True).save(
    "/Users/boni.nugraha/Downloads/pyspark-poc/datacamp_courses_edited.csv"
)


# Stop the SparkSession
spark.stop()
