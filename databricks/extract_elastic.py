# Extrai dados do Elasticsearch usando PySpark

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("ExtractFromElasticsearch") \
    .config("spark.es.nodes", "localhost") \
    .config("spark.es.port", "9200") \
    .config("spark.es.nodes.wan.only", "true") \
    .getOrCreate()

# Lê o índice logs-api
df = spark.read.format("org.elasticsearch.spark.sql").load("logs-api/_doc")
df.show(truncate=False)

# Salva temporariamente os dados
df.write.mode("overwrite").json("dbfs:/tmp/logs_raw")
