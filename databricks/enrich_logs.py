# Script PySpark para enriquecer logs com regras simples ou ML
from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col

# Cria a sessão
spark = SparkSession.builder.appName("EnrichLogs").getOrCreate()

# Lê os logs extraídos
df = spark.read.json("dbfs:/tmp/logs_raw")

# Enriquecimento: classificação simples por tipo de erro
df_enriched = df.withColumn(
    "classificacao",
    when(col("message").contains("timeout"), "TimeoutError")
    .when(col("message").contains("null pointer"), "NullPointer")
    .when(col("message").contains("refused"), "ConnectionRefused")
    .otherwise("Outros")
)

# Exibe resultados
df_enriched.show(truncate=False)

# Salva como CSV de exemplo
df_enriched.write.mode("overwrite").csv("dbfs:/tmp/logs_enriched", header=True)

