# Retorna dados enriquecidos ao Elasticsearch

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("ReturnToElasticsearch") \
    .config("spark.es.nodes", "localhost") \
    .config("spark.es.port", "9200") \
    .config("spark.es.nodes.wan.only", "true") \
    .getOrCreate()

# Lê os dados enriquecidos
df = spark.read.csv("dbfs:/tmp/logs_enriched", header=True)

# Escreve no índice logs-enriched
df.write.format("org.elasticsearch.spark.sql") \
    .option("es.resource", "logs-enriched/_doc") \
    .mode("overwrite") \
    .save()
