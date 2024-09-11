import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os


# Carregar variáveis do arquivo .env
load_dotenv()

# Configuração do banco de dados PostgreSQL
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")


# Create the table
def create_table(cursor):
    create_table_query = """
        CREATE TABLE IF NOT EXISTS VENDAS (
            email VARCHAR(255) NOT NULL,
            data TIMESTAMP NOT NULL,
            valor NUMERIC CHECK (valor > 0) NOT NULL,
            quantidade INTEGER CHECK (quantidade > 0) NOT NULL,
            produto VARCHAR(255) NOT NULL
        );
    """
    cursor.execute(create_table_query)

# Establish connection and create table
conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )

cursor = conn.cursor()

# Create enum type and table
create_table(cursor)

# Commit changes and close the connection
conn.commit()
cursor.close()
conn.close()
