# raw_layer/raw_organizations.py
"""
Este módulo é responsável por buscar dados de organizações e carregá-los em um sistema de ingestão.
Funções:
- main(): A função principal que busca os dados de organizações usando a função 'fetch' do módulo 'api' 
    e, em seguida, carrega esses dados usando a função 'load_raw_full_refresh' do módulo 'ingestion_engine'.
O fluxo de execução começa ao chamar a função main, que obtém os dados e os processa para armazenamento.
"""


from .api import fetch
from .ingestion_engine import load_raw_full_refresh

def main():
    data = fetch("organizations").get("data", [])
    load_raw_full_refresh("raw_organizations", data)

if __name__ == "__main__":
    main()