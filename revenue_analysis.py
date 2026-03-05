from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

spark = SparkSession.builder.appName("RevenueAnalysis").getOrCreate()

df = spark.read.format("delta").load("silver_sales")

revenue = df.groupBy("product").agg(sum("amount").alias("total_revenue"))

revenue.write.format("delta").mode("overwrite").save("gold_sales")
