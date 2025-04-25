# Elasticsearch + Databricks PoC

Esta prova de conceito demonstra como integrar **Elasticsearch** e **Databricks** para:

- Extrair logs indexados no Elasticsearch
- Enriquecer com PySpark (usando regras simples ou ML)
- Retornar os dados enriquecidos ao Elasticsearch
- Visualizar insights via Kibana

---

## 📌 Objetivo

Unir a velocidade de busca do Elasticsearch com o poder de processamento do Databricks, criando uma arquitetura de observabilidade inteligente.

---

## 🛠️ Passo a passo para executar a PoC

### 🔹 Pré-requisitos
- Elasticsearch rodando localmente ou acessível por IP
- Databricks Workspace ativo (com cluster Spark)
- Conector Elasticsearch para Spark instalado no cluster

---

### 🔁 Etapas

 1. Criar o índice no Elasticsearch
=======
#### 1. Criar o índice no Elasticsearch
Execute via Kibana Dev Tools ou API:

```json
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

2. Ingerir os logs de exemplo

curl -X POST "http://localhost:9200/logs-api/_bulk" -H 'Content-Type: application/json' --data-binary @elastic/log-sample.json


3. No Databricks, execute os scripts na seguinte ordem:
(a) extract_elastic.py – extrai os dados e salva em /tmp/logs_raw

(b) enrich_logs.py – aplica regras e salva como /tmp/logs_enriched

(c) return_to_elastic.py – envia os dados tratados ao índice logs-enriched

Alternativamente, execute o notebook LogAnalysisDatabricks.ipynb que contém todas as etapas agrupadas.

4. Visualize os dados enriquecidos no Kibana
Crie index pattern: logs-enriched

Explore os campos, incluindo classificacao

=======
```

---

#### 2. Ingerir os logs de exemplo

```bash
curl -X POST "http://localhost:9200/logs-api/_bulk" -H 'Content-Type: application/json' --data-binary @elastic/log-sample.json
```

---

#### 3. No Databricks, execute os scripts na seguinte ordem:

(a) `extract_elastic.py` – extrai os dados e salva em `/tmp/logs_raw`  
(b) `enrich_logs.py` – aplica regras e salva como `/tmp/logs_enriched`  
(c) `return_to_elastic.py` – envia os dados tratados ao índice `logs-enriched`

> Alternativamente, execute o notebook `LogAnalysisDatabricks.ipynb` que contém todas as etapas agrupadas.

---

#### 4. Visualize os dados enriquecidos no Kibana

- Crie index pattern: `logs-enriched`
- Explore os campos, incluindo `classificacao`

---

## 📦 Estrutura do Projeto

```
elasticsearch-databricks-poc/
├── elastic/
│   ├── log-sample.json
│   └── elastic-config.md
├── databricks/
│   ├── extract_elastic.py
│   ├── enrich_logs.py
│   ├── return_to_elastic.py
│   └── notebooks/
│       └── LogAnalysisDatabricks.ipynb
├── data/enriched_sample.csv
└── assets/architecture-diagram.png


=======
```

## 📎 Links

- GitHub: [rafasilva1984](https://github.com/rafasilva1984)
- LinkedIn: [Rafael Silva](https://linkedin.com/in/rafael-silva-leader-coordenador)
- Medium: [rafaelldasilva](https://medium.com/@rafaelldasilva)

---

#Elasticsearch #Databricks #Observabilidade #DataOps #BigData #MachineLearning
