# raw_layer/raw_users.py
"""
Este módulo é responsável por buscar dados de usuários e carregá-los em um sistema de ingestão de dados.
Funções:
- main(): A função principal que busca os dados de usuários através da função 'fetch' e os carrega usando 'load_raw_full_refresh'.
O fluxo de execução começa na função main, que chama a função 'fetch' para obter os dados dos usuários. 
Os dados são então passados para a função 'load_raw_full_refresh' para serem armazenados na camada de dados brutos.
"""


from .api import fetch
from .ingestion_engine import load_raw_full_refresh

def main():
    data = fetch("users").get("data", [])
    load_raw_full_refresh("raw_users", data)

if __name__ == "__main__":
    main()