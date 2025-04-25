# Script PySpark para extrair logs do Elasticsearch

from pyspark.sql import SparkSession

# Inicializa a sessão Spark
spark = SparkSession.builder \
    .appName("ExtractFromElasticsearch") \
    .config("spark.es.nodes", "localhost") \
    .config("spark.es.port", "9200") \
    .config("spark.es.nodes.wan.only", "true") \
    .getOrCreate()

# Lê dados do Elasticsearch (índice de exemplo: logs-api)
df = spark.read.format("org.elasticsearch.spark.sql") \
    .load("logs-api/_doc")

# Exibe dados
df.show(truncate=False)

# Salva localmente para simular enriquecimento
df.write.mode("overwrite").json("dbfs:/tmp/logs_raw")

