# 🏆 DataCopa: Brazil's World Cup Legacy 🇧🇷

## 📖 Overview
The **DataCopa Pipeline** is an end-to-end Data Engineering project dedicated to analyzing the historical and statistical performance of the **Brazilian National Team** across FIFA World Cup history. 

By implementing a **Modern Data Lakehouse** architecture on **Microsoft Azure**, this pipeline ingests historical datasets and dynamic API feeds to provide deep insights into goals, match results, and historical trends of the only five-time world champions.

## 🏗️ Architecture
The project follows the **Medallion Architecture** (Bronze, Silver, and Gold layers), ensuring high data quality and reliability through each stage of the transformation process.

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
