# 🏆 DataCopa Pipeline: Modern Data Lakehouse

## 📖 Overview
The **DataCopa Pipeline** is an end-to-end Data Engineering project designed to ingest, process, and serve historical and dynamic data from the FIFA World Cup. 

This project demonstrates the implementation of a **Modern Data Lakehouse architecture** using the **Microsoft Azure** ecosystem and **Apache Spark**, following the Medallion architecture (Bronze, Silver, and Gold layers).

## 🏗️ Architecture

The data flows through a batch processing pipeline, extracting both structured (CSV) and semi-structured (JSON) data, transforming it via PySpark, and serving it for analytics.

```mermaid
graph LR
    %% Data Sources
    KGL[Kaggle API]
    APIF[API-Football]
    PY[Python Extraction]
    
    %% Azure Data Lakehouse
    ADLS[(Azure Data Lake<br>Storage Gen2)]
    DBX((Azure Databricks<br>Apache Spark))
    SYN{Azure Synapse<br>Analytics}
    
    %% Serving
    STR[Streamlit Dashboard]

    %% Flow
    KGL -->|Historical CSVs| PY
    APIF -->|Dynamic JSONs| PY
    PY -->|Raw Upload| ADLS
    
    ADLS <-->|PySpark ETL<br>Bronze/Silver/Gold| DBX
    
    ADLS -->|Read Curated Parquet| SYN
    SYN -->|SQL Queries| STR

    classDef python fill:#306998,stroke:#FFD43B,stroke-width:2px,color:white;
    classDef azure fill:#0078D4,stroke:#005A9E,stroke-width:2px,color:white;
    classDef databricks fill:#FF3621,stroke:#C21A06,stroke-width:2px,color:white;
    classDef frontend fill:#FF4B4B,stroke:#7D2A2A,stroke-width:2px,color:white;
    
    class PY python;
    class ADLS,SYN azure;
    class DBX databricks;
    class STR frontend;
