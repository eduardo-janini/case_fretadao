# raw_layer/raw_groups.py
"""
Este módulo é responsável por buscar dados de grupos e carregá-los em um sistema de ingestão.
Funções:
- main(): A função principal que busca os dados de grupos usando a função `fetch` do módulo `api` e, em seguida, carrega esses dados em um sistema de ingestão usando a função `load_raw_full_refresh` do módulo `ingestion_engine`.
O fluxo de execução começa na função `main`, que é chamada quando o módulo é executado diretamente. Os dados são obtidos da API e, se disponíveis, são carregados para a camada de dados bruta chamada "raw_groups".
"""


from .api import fetch
from .ingestion_engine import load_raw_full_refresh

def main():
    data = fetch("groups").get("data", [])
    load_raw_full_refresh("raw_groups", data)
    
if __name__ == "__main__":
    main()