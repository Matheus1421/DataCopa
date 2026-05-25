# 🏆 Copa Dados Pipeline

## 📖 Sobre o Projeto

O **Copa Dados Pipeline** é um projeto de análise de dados focado no histórico da :contentReference[oaicite:0]{index=0} em Copas do Mundo.  
A proposta do projeto é construir um pipeline completo de dados capaz de transformar informações brutas em insights visuais e interativos sobre o desempenho da equipe ao longo das edições do torneio.

O pipeline realiza o processamento da camada `raw` até a geração de dados tratados e prontos para análise, permitindo explorar métricas históricas relevantes como:

- ⚽ **Desempenho Geral:** evolução de vitórias, gols marcados, derrotas e saldo ao longo das Copas.
- 🎯 **Artilharia:** análise de protagonismo ofensivo e dependência de jogadores decisivos.
- 🟨 **Disciplina:** histórico de cartões e comportamento tático da equipe.
- 📊 **Visualização Interativa:** dashboards modernos com gráficos dinâmicos e experiência de navegação fluida.

O resultado final é apresentado em um **Dashboard Interativo** desenvolvido com **Streamlit**, utilizando uma interface em **Dark Mode** inspirada nas cores oficiais da Seleção Brasileira.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.10+
- **Processamento de Dados:** Pandas
- **Visualização de Dados:** Plotly
- **Dashboard:** Streamlit
- **Configuração de Tema:** `.streamlit/config.toml`

---

## 🚀 Como Executar o Projeto

### ✅ Pré-requisitos

Antes de iniciar, certifique-se de possuir:

- Python 3.10 ou superior instalado
- `pip` configurado
- Ambiente virtual recomendado (`venv`)

---

### 1️⃣ Clone o Repositório

```bash
git clone https://github.com/SEU_USUARIO/copa-dados-pipeline.git
cd copa-dados-pipeline
```

---

### 2️⃣ Crie e Ative o Ambiente Virtual

#### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Instale as Dependências

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Execute o Dashboard

A partir da raiz do projeto, execute:

```bash
streamlit run src/app.py
```

O dashboard será iniciado automaticamente no navegador:

```text
http://localhost:8501
```

---

## 📁 Estrutura do Projeto

```text
copa-dados-pipeline/
├── .streamlit/              # Configurações visuais do Streamlit
│   └── config.toml
│
├── data/
│   ├── raw/                 # Dados brutos
│   └── processed/           # Dados tratados pelo pipeline
│
├── notebooks/               # Exploração e análises (EDA)
│
├── src/
│   └── app.py               # Aplicação principal do dashboard
│
├── requirements.txt         # Dependências do projeto
└── README.md                # Documentação do projeto
```

---

## 📊 Funcionalidades

- Dashboard interativo com filtros dinâmicos
- Visualizações históricas das campanhas do Brasil
- Pipeline de tratamento de dados automatizado
- Interface moderna em Dark Mode
- Gráficos responsivos com Plotly

---

## 🎯 Objetivos do Projeto

Este projeto foi desenvolvido com o objetivo de:

- Praticar conceitos de **Engenharia de Dados**
- Aplicar técnicas de **Análise Exploratória de Dados (EDA)**
- Desenvolver dashboards interativos com foco em UX/UI
- Consolidar conhecimentos em Python e visualização de dados
- Criar um projeto de portfólio com aplicação prática

---

## 🤝 Contribuições

Contribuições são bem-vindas!

Caso tenha sugestões de melhorias, novas métricas ou correções, fique à vontade para:

- Abrir uma *issue*
- Enviar um *pull request*
- Compartilhar feedbacks

---

## 👨‍💻 Autor

Projeto desenvolvido por **Matheus da Fonseca Marques**.
