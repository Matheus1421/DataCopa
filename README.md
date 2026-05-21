# 🏆 DataCopa: Brazil's World Cup Legacy 

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
    
    %% Storage Layers (Local)
    RAW[(Local: data/raw/<br>JSON & CSV)]
    PROC[(Local: data/processed/<br>Parquet)]
    
    %% Processing & UI
    PY_EXT[Python Extraction]
    PD((Pandas ETL))
    STR[Streamlit Dashboard]

    %% Flow
    KGL -->|Historical CSVs| PY_EXT
    APIF -->|Dynamic JSONs| PY_EXT
    PY_EXT -->|Save| RAW
    
    RAW -->|Read| PD
    PD -->|Clean & Filter Brazil| PROC
    
    PROC -->|Load Local Data| STR

    %% Styles
    classDef source fill:#306998,stroke:#FFD43B,stroke-width:2px,color:white;
    classDef storage fill:#3F8624,stroke:#232F3E,stroke-width:2px,color:white;
    classDef process fill:#E25A1C,stroke:#232F3E,stroke-width:2px,color:white;
    classDef frontend fill:#FF4B4B,stroke:#7D2A2A,stroke-width:2px,color:white;
    
    class KGL,APIF,PY_EXT source;
    class RAW,PROC storage;
    class PD process;
    class STR frontend;
