import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv
import re

# Carrega variáveis de ambiente
load_dotenv()

# Caminho para o Excel
base_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_path, '..', 'data', 'produtos.xlsx')


def extract():
    """Extrai os dados do Excel e padroniza os nomes das colunas"""
    df = pd.read_excel(file_path)

    # Padroniza colunas: remove espaços, deixa minúsculas e substitui espaços por underline
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    print("Colunas após padronização:", df.columns.tolist())
    
    return df


def clean_money_column(col):
    """Remove R$, espaços e converte para float"""
    return col.astype(str).str.replace(r'[^0-9,.-]', '', regex=True).str.replace(',', '.').replace('', '0').astype(float)


def transform(df):
    """Transforma dados: tipos corretos e limpeza de valores"""
    df = df.fillna('')  # Preenche NaN temporariamente para evitar erros de conversão

    # Limpeza das colunas monetárias
    money_cols = [
        'custo_unit', 'venda_unit', 'lucro_unit',
        'custo_total', 'venda_total', 'lucro_total'
    ]
    for col in money_cols:
        df[col] = clean_money_column(df[col])

    # Converte quantidade para inteiro
    df['qtde'] = df['qtde'].astype(int)

    # Datas: converte strings para datetime e NaT para None
    df['data_entrada'] = pd.to_datetime(df['data_entrada'], errors='coerce')
    df['data_saida'] = pd.to_datetime(df['data_saida'], errors='coerce')

    return df


def load(df):
    """Carrega os dados no PostgreSQL"""
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    cursor = conn.cursor()

    # Limpa tabela antes de inserir (evita duplicidade)
    cursor.execute("TRUNCATE TABLE produtos;")
    conn.commit()

    for _, row in df.iterrows():
        cursor.execute("""
INSERT INTO produtos (
    cod, tipo, qtde, modelo, tamanho,
    custo_unit, venda_unit, lucro_unit,
    custo_total, venda_total, lucro_total,
    data_entrada, data_saida
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
""", (
            row['cod'],
            row['tipo'],
            row['qtde'],
            row['modelo'],
            row['tamanho'],
            row['custo_unit'],
            row['venda_unit'],
            row['lucro_unit'],
            row['custo_total'],
            row['venda_total'],
            row['lucro_total'],
            row['data_entrada'] if not pd.isna(row['data_entrada']) else None,
            row['data_saida'] if not pd.isna(row['data_saida']) else None
        ))

    conn.commit()
    cursor.close()
    conn.close()


def main():
    df = extract()
    df = transform(df)
    load(df)
    print("ETL finalizado com sucesso!")


if __name__ == "__main__":
    main()