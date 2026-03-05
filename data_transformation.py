from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("SalesTransform").getOrCreate()

df = spark.read.format("delta").load("bronze_sales")

clean_df = df.dropDuplicates()

clean_df.write.format("delta").mode("overwrite").save("silver_sales")
