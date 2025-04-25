# Configuração do Elasticsearch para PoC com Databricks

## 1. Criar índice logs-api
PUT logs-api
{
  "mappings": {
    "properties": {
      "timestamp": { "type": "date" },
      "level": { "type": "keyword" },
      "message": { "type": "text" },
      "service": { "type": "keyword" }
    }
  }
}

## 2. Ingestar dados
curl -X POST "http://localhost:9200/logs-api/_bulk" -H 'Content-Type: application/json' --data-binary @elastic/log-sample.json

## 3. Validar
curl "http://localhost:9200/logs-api/_search?pretty"
