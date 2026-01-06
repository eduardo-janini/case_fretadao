# raw_layer/dbconnection.py
"""
Database Connection Module
Este módulo é responsável por gerenciar a conexão com o banco de dados PostgreSQL.
Fornece uma função utilitária para obter uma conexão ativa com o banco de dados
utilizando as configurações definidas no módulo dbconfig.
Módulos importados:
    - psycopg2: Driver PostgreSQL para Python
    - .dbconfig: Módulo local contendo as configurações de banco de dados (DB_CONFIG)
Funções:
    get_connection(): Retorna uma nova conexão com o banco de dados PostgreSQL
                     usando as credenciais e parâmetros definidos em DB_CONFIG.
Uso:
    conn = get_connection()
    cursor = conn.cursor()
    # Executar queries...
    conn.close()
"""


import psycopg2
from .dbconfig import DB_CONFIG

def get_connection():
    return psycopg2.connect(**DB_CONFIG)
