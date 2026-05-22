# 🏆 DataCopa: O Legado da Seleção Canarinho 🇧🇷

## 📖 Visão Geral
O **DataCopa** é um projeto de Ciência de Dados e Machine Learning de ponta a ponta projetado para analisar, extrair padrões e modelar estatisticamente o desempenho da **Seleção Brasileira** nas cinco edições de Copa do Mundo em que se sagrou campeã (1958, 1962, 1970, 1994 e 2002).

A partir de dados históricos estruturados, o projeto une a Engenharia de Dados local (ETL) ao desenvolvimento de modelos preditivos e descritivos para responder: *o que matematicamente definiu o DNA das gerações campeãs do Brasil?*

## 🏗️ Arquitetura do Projeto
O pipeline foi desenhado seguindo uma abordagem *lightweight* (leve) e totalmente local, priorizando a eficiência do código e eliminando a complexidade de infraestruturas em nuvem desnecessárias para o volume atual de dados.

```mermaid
graph LR
    %% Fontes de Dados
    KGL[Kaggle API]
    
    %% Camadas de Armazenamento Local
    RAW[(Local: data/raw/<br>CSVs Originais)]
    PROC[(Local: data/processed/<br>Parquet Otimizado)]
    MODELS[(Local: models/<br>Modelos Treinados .pkl)]
    
    %% Processamento e Interface
    PY_EXT[Extração Python]
    PD((Pandas ETL))
    SKL((Scikit-Learn ML))
    STR[Dashboard Streamlit]

    %% Fluxo de Dados
    KGL -->|Download de CSVs| PY_EXT
    PY_EXT -->|Armazena| RAW
    
    RAW -->|Leitura e Filtros| PD
    PD -->|Feature Engineering| PROC
    
    PROC -->|Treinamento| SKL
    SKL -->|Salva Artefato| MODELS
    
    PROC -->|Consome Dados| STR
    MODELS -->|Consome Modelo| STR
