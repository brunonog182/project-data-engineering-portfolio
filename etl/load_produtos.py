import os
import logging
from pathlib import Path

import pandas as pd
import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv


# ==============================
# CONFIGURATION
# ==============================

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

BASE_DIR = Path(__file__).resolve().parent
FILE_PATH = BASE_DIR.parent / "data" / "products.xlsx"


# ==============================
# EXTRACT
# ==============================

def extract() -> pd.DataFrame:
    """Extract data from Excel and standardize column names"""
    logging.info("Starting data extraction...")

    df = pd.read_excel(FILE_PATH)

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    logging.info(f"Columns after standardization: {list(df.columns)}")

    return df


# ==============================
# TRANSFORM
# ==============================

def clean_currency_column(series: pd.Series) -> pd.Series:
    """Clean currency columns and convert to float"""
    return (
        series.astype(str)
        .str.replace(r"[^0-9,.-]", "", regex=True)
        .str.replace(",", ".")
        .replace("", "0")
        .astype(float)
    )


def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Transform raw data into curated format"""
    logging.info("Starting data transformation...")

    df = df.fillna("")

    currency_columns = [
        "unit_cost", "unit_price", "unit_profit",
        "total_cost", "total_price", "total_profit"
    ]

    for col in currency_columns:
        if col in df.columns:
            df[col] = clean_currency_column(df[col])

    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce").fillna(0).astype(int)

    df["entry_date"] = pd.to_datetime(df["entry_date"], errors="coerce")
    df["exit_date"] = pd.to_datetime(df["exit_date"], errors="coerce")

    # Mapping to target schema
    df_transformed = pd.DataFrame({
        "name": df["model"],
        "category": df["type"],
        "price": df["unit_price"],
        "stock": df["quantity"],
        "created_at": df["entry_date"]
    })

    df_transformed = df_transformed.dropna()

    logging.info(f"Records ready for load: {len(df_transformed)}")

    return df_transformed


# ==============================
# LOAD
# ==============================

def get_connection():
    """Create database connection"""
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )


def load(df: pd.DataFrame):
    """Load data into PostgreSQL using bulk insert"""
    logging.info("Starting data load...")

    conn = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Idempotent load (full refresh)
        cursor.execute("TRUNCATE TABLE products RESTART IDENTITY;")

        data_tuples = [
            (
                row.name,
                row.category,
                row.price,
                row.stock,
                None if pd.isna(row.created_at) else row.created_at
            )
            for row in df.itertuples(index=False)
        ]

        insert_query = """
            INSERT INTO products (name, category, price, stock, created_at)
            VALUES %s
        """

        execute_values(cursor, insert_query, data_tuples)

        conn.commit()

        logging.info(f"{len(df)} records successfully loaded.")

    except Exception as e:
        logging.error(f"Error during load: {e}")
        if conn:
            conn.rollback()
        raise

    finally:
        if conn:
            cursor.close()
            conn.close()


# ==============================
# MAIN
# ==============================

def main():
    logging.info("ETL pipeline started")

    df = extract()
    df = transform(df)
    load(df)

    logging.info("ETL pipeline finished successfully")


if __name__ == "__main__":
    main()