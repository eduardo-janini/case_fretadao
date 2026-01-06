# raw_layer/dbconfig.py
"""
Módulo de configuração do banco de dados para a camada raw_layer.
Este módulo contém as credenciais e parâmetros de conexão necessários
para conectar ao banco de dados PostgreSQL da aplicação. As configurações
incluem informações como host, porta, nome do banco de dados, usuário e senha.
Attributes:
    DB_CONFIG (dict): Dicionário contendo as configurações de conexão do banco de dados:
        - host (str): Endereço do servidor do banco de dados (localhost)
        - port (int): Porta do serviço PostgreSQL (5432)
        - database (str): Nome do banco de dados a ser acessado (datawarehouse)
        - user (str): Usuário para autenticação no PostgreSQL (postgres)
        - password (str): Senha para autenticação no PostgreSQL (admin)
Note:
    Este arquivo é utilizado pela camada raw_layer para estabelecer conexões
    com o banco de dados PostgreSQL em um projeto de data warehouse.
    As credenciais devem ser mantidas de forma segura e não devem ser
    expostas em repositórios públicos.
"""

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "datawarehouse",
    "user": "postgres",
    "password": "admin"}