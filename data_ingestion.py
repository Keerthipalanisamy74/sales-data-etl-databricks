from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SalesETL").getOrCreate()

df = spark.read.option("header",True).csv("sales_raw.csv")

df.write.format("delta").mode("overwrite").save("bronze_sales")
