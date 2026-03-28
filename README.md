# 🛍️ Sales Data Pipeline

> A Data Engineering project automating the ingestion, transformation, and visualization of e-commerce sales data.

---

## 🏗️ Project Architecture

This pipeline follows an **ELT/ETL** pattern using containerized services:

| Stage | Description | Technology |
| --- | --- | --- |
| **Extraction** | Reading data from Excel/CSV source files | Python, Pandas |
| **Transformation** | Cleaning and processing data | Python, Pandas |
| **Loading** | Inserting structured data into relational database | PostgreSQL |
| **Visualization** | Interactive dashboards for business insights | Power BI |

![Dashboard Preview](dashboard/print-dashboard-1.png)

---

## 🛠️ Tech Stack

- **Language:** Python 3.8+
- **Database:** PostgreSQL
- **Containerization:** Docker & Docker Compose
- **BI Tool:** Microsoft Power BI
- **Libraries:** pandas, psycopg2, openpyxl, python-dotenv

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

| Practice | Implementation |
| --- | --- |
| **Secrets Management** | Credentials managed via environment variables |
| **Version Control** | Sensitive files ignored via `.gitignore` |
| **Database Access** | Non-root user with restricted permissions |
| **Network Security** | PostgreSQL port exposed only to localhost |

---

## 🧪 Testing & Validation

After running the ETL, validate data insertion:

Access PostgreSQL container:

    docker exec -it postgres-bi psql -U $POSTGRES_USER -d $POSTGRES_DB

Query inserted data:

    SELECT COUNT(*) FROM produtos;
    SELECT * FROM produtos LIMIT 10;

---

## 📫 Contact

| Platform | Link |
| --- | --- |
| **LinkedIn** | linkedin.com/in/bruno-nogueira-4aa686a3 |
| **Email** | brunogueira182@protonmail.com |
| **GitHub** | github.com/brunonog182 |

---
