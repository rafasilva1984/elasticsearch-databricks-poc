# Enriquecimento dos logs com regras simples

from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col

spark = SparkSession.builder.appName("EnrichLogs").getOrCreate()

# Lê logs brutos
df = spark.read.json("dbfs:/tmp/logs_raw")

# Classificação por tipo de erro
df_enriched = df.withColumn(
    "classificacao",
    when(col("message").contains("timeout"), "TimeoutError")
    .when(col("message").contains("null pointer"), "NullPointer")
    .when(col("message").contains("refused"), "ConnectionRefused")
    .otherwise("Outros")
)

df_enriched.show(truncate=False)
df_enriched.write.mode("overwrite").csv("dbfs:/tmp/logs_enriched", header=True)
