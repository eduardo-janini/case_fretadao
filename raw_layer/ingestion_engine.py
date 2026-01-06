# raw_layer/ingestion_engine.py
"""
Este módulo contém funções para carregar dados em uma tabela de banco de dados PostgreSQL usando uma conexão definida em um módulo separado.
Funções:
- load_raw_incremental(table_name, records): 
    Carrega registros incrementais em uma tabela especificada. Se a tabela não existir, ela será criada. Os registros são inseridos como objetos JSONB.
- load_raw_full_refresh(table_name, records): 
    Realiza uma atualização completa da tabela especificada, truncando-a antes de inserir novos registros. Assim como na função anterior, os registros são inseridos como objetos JSONB.
"""


import json
from .dbconnection import get_connection

# Realiza uma carga incremental, inserindo novos registros na tabela
def load_raw_incremental(table_name, records):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(f"""
        create table if not exists {table_name} (payload jsonb);
    """)

    for record in records:
        cur.execute(
            f"insert into {table_name} (payload) values (%s)",
            [json.dumps(record)]
        )

    conn.commit()
    cur.close()
    conn.close()

# Realiza uma carga completa, truncando a tabela antes de inserir novos dados
def load_raw_full_refresh(table_name, records):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(f"""
        create table if not exists {table_name} (
            payload jsonb
        );
    """)

    cur.execute(f"truncate table {table_name};")

    for record in records:
        cur.execute(
            f"insert into {table_name} (payload) values (%s)",
            [json.dumps(record)]
        )

    conn.commit()
    cur.close()
    conn.close()