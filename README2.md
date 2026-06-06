<<<<<<< HEAD
# Projeto de Engenharia de Dados - E-commerce

## Descrição
Este projeto automatiza a extração e transformação de dados de vendas da minha loja.

## Ferramentas Usadas
- Python
- SQL
- Airflow (ou a ferramenta que usou)
- Banco de Dados: PostgreSQL

## Como Rodar
1. Instale as dependências
2. Configure suas variáveis de ambiente
3. Rode o script principal
=======
🚀 End-to-End Sales Data Pipeline for Analytics
                
## 🎯 Business Context

This project reflects real-world data engineering challenges, including data quality, reproducibility, and scalable pipeline design.

The goal is to enable:

- Sales performance monitoring
- Product-level analysis
- Data-driven decision making
- A centralized and reliable data source (Single Source of Truth)

## 💡 Key Highlights

- End-to-end data pipeline (ingestion → transformation → visualization)
- Designed with scalability and reproducibility in mind
- Strong focus on data quality and consistency
- Built using modern data engineering practices

## 🧠 Data Governance Considerations

- Ensures consistency across multiple data sources
- Supports a Single Source of Truth approach
- Prepares the foundation for Master Data Management (MDM)
- Improves data reliability for business decision-making
  
---

## 🏗️ Data Architecture

The pipeline follows a layered architecture:

- **Raw Layer**: Source Excel/CSV files
- **Staging Layer**: Initial cleaned data
- **Curated Layer**: Structured tables in PostgreSQL
- **Analytics Layer**: Power BI dashboards

## 🔄 Pipeline Stages

| Stage          | Description                                      | Technology        |
|----------------|--------------------------------------------------|------------------|
| Extraction     | Reading data from Excel/CSV source files         | Python, Pandas   |
| Transformation | Cleaning and processing data                     | Python, Pandas   |
| Loading        | Inserting structured data into PostgreSQL        | PostgreSQL       |
| Visualization  | Interactive dashboards for business insights     | Power BI         |

## 📊 Dashboard Preview

![Dashboard Preview](dashboard/print-dashboard-1.png)

---

## ⚙️ Pipeline Features

- Data ingestion from heterogeneous sources
- Data cleaning and standardization
- Idempotent load process
- Environment-based configuration
- Containerized execution
- Modular ETL design
- Reproducible local environment using Docker
  
---
## 🛠️ Tech Stack

- **Language:** Python 3.8+
- **Database:** PostgreSQL
- **Containerization:** Docker & Docker Compose
- **BI Tool:** Microsoft Power BI
- **Libraries:** pandas, psycopg2, openpyxl, python-dotenv

---
## 🧩 Data Model

The database follows a simplified analytical model:

- **produtos**: product-level information
- Future improvements include evolving the model into a Star Schema:
    - fact_sales
    - dim_products
    - dim_date

This structure allows efficient querying and supports BI tools.

## ✅ Data Quality Checks

- Null value handling
- Data type validation
- Duplicate removal
- Schema enforcement before loading

---

## 📊 Business Insights (Power BI)

The dashboard provides:

- Revenue trends over time
- Top-performing products
- Sales distribution by category
- Key KPIs (total revenue, average ticket, sales volume)
  
---

## 📂 Project Structure

    sales-data-pipeline/
    ├── docker/            # Docker container configurations
    ├── etl/               # Python scripts for Extraction & Loading
    ├── sql/               # SQL scripts for table creation
    ├── data/              # Source files (Excel/CSV)
    ├── dashboard/         # Power BI files and screenshots
    ├── .gitignore         # Git ignore rules
    ├── .env.example       # Environment variables template
    └── README.md          # Project documentation

---

## 🚀 Getting Started

### 1. Prerequisites

Ensure you have the following installed:

- Docker and Docker Compose
- Python 3.8+
- Power BI Desktop (optional for visualization)

### 2. Environment Configuration

1. Rename the `.env.example` file to `.env` in both `docker/` and root directories.
2. Fill in your credentials.

### 3. Spin Up Database

Navigate to the docker folder and run:

    cd docker
    docker-compose up -d

Verify the container is running:

    docker ps

### 4. Run the ETL Pipeline

Install dependencies and execute the script:

    pip install pandas psycopg2-binary openpyxl python-dotenv
    python etl/load_produtos.py

### 5. Visualize in Power BI

1. Open the `.pbix` file located in the `dashboard/` folder.
2. Go to Home → Transform Data → Data source settings.
3. Update the connection to point to your local PostgreSQL instance.
4. Click Refresh to load the data.

---

## 🔐 Security Best Practices

| Practice           | Implementation                                     |
|------------------|------------------------------------------------------|
| Secrets Management | Credentials managed via environment variables      |
| Version Control    | Sensitive files ignored via .gitignore             |
| Database Access    | Non-root user with restricted permissions          |
| Network Security   | PostgreSQL exposed only to localhost               |

---

## 🧪 Testing & Validation

After running the ETL, validate data insertion:

Access PostgreSQL container:

    docker exec -it postgres-bi psql -U $POSTGRES_USER -d $POSTGRES_DB

Query inserted data:

    SELECT COUNT(*) FROM produtos;
    SELECT * FROM produtos LIMIT 10;

---

## 🚀 Future Improvements

- Incremental data loading
- Data warehouse modeling (Star Schema)
- Workflow orchestration with Apache Airflow
- Data quality monitoring (Great Expectations)
- Cloud deployment (AWS/GCP)

---

## 📫 Contact

| Platform | Link |
| --- | --- |
| **LinkedIn** | linkedin.com/in/bruno-nogueira-4aa686a3 |
| **Email** | brunogueira182@protonmail.com |
| **GitHub** | github.com/brunonog182 |

---
>>>>>>> 0f5f94a5ad0d1da8c222ed69c4aa5adb2e8195fe
