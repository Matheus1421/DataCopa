graph LR
    subgraph Origens
        A[Kaggle CSVs] -->|Python Script| C
        B[API-Football JSON] -->|Python Script| C
    end

    subgraph AWS Cloud - Data Lakehouse
        C[Upload via Boto3] --> D[(S3: Camada Bronze\nRaw Data)]
        D -->|Leitura PySpark| E((Apache Spark\nAWS Glue))
        E -->|Limpeza e Cast| F[(S3: Camada Silver\nCleaned Data)]
        F -->|Leitura PySpark| G((Apache Spark\nAWS Glue))
        G -->|Joins e Agregações| H[(S3: Camada Gold\nCurated Data)]
        H --> I{Amazon Athena\nSQL Engine}
    end

    subgraph Visualização
        I --> J[Streamlit\nDashboard]
    end

    classDef aws fill:#FF9900,stroke:#232F3E,stroke-width:2px,color:white;
    classDef spark fill:#E25A1C,stroke:#232F3E,stroke-width:2px,color:white;
    classDef storage fill:#3F8624,stroke:#232F3E,stroke-width:2px,color:white;
    
    class D,F,H storage;
    class E,G spark;
    class I aws;
