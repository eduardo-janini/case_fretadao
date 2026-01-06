# raw_layer/raw_tickets.py
"""
Este módulo é responsável por ingerir dados de tickets a partir de uma API.
Funções principais:
- main(): Função principal que busca os tickets mais recentes, carrega os dados
    novos e atualiza o ponto de verificação (checkpoint) para a próxima execução.
Detalhes do funcionamento:
1. Obtém o último ponto de verificação (checkpoint) para a tabela "raw_tickets".
2. Se houver um ponto de verificação, define um parâmetro de tempo de início para
     buscar apenas os tickets atualizados após esse ponto.
3. Faz uma chamada à API para buscar os tickets usando o endpoint "tickets".
4. Se não houver novos tickets, imprime uma mensagem e encerra a execução.
5. Caso contrário, carrega os tickets novos usando a função `load_raw_incremental`.
6. Atualiza o ponto de verificação com o timestamp máximo dos tickets ingeridos.
7. Imprime a quantidade de tickets ingeridos.
Constantes:
- TABLE_NAME: Nome da tabela onde os dados dos tickets são armazenados.
- ENDPOINT: Endpoint da API para buscar os tickets.
- TIME_FIELD: Campo que contém a data de atualização dos tickets.
"""


from .api import fetch
from .ingestion_engine import load_raw_incremental
from .table_schema import get_checkpoint, update_checkpoint

TABLE_NAME = "raw_tickets"
ENDPOINT = "tickets"
TIME_FIELD = "updated_at"


def main():
    # Obtém o último ponto de verificação (checkpoint) para saber a partir de quando buscar novos dados
    last_checkpoint = get_checkpoint(TABLE_NAME)

    params = {}
    if last_checkpoint:
        params["start_time"] = last_checkpoint.isoformat()

    response = fetch(ENDPOINT, params=params)
    records = response.get("data", [])

    if not records:
        print("No new tickets to ingest.")
        return

    load_raw_incremental(TABLE_NAME, records)

    # Atualiza o checkpoint com o timestamp máximo dos registros ingeridos
    max_timestamp = max(
        r[TIME_FIELD] for r in records if r.get(TIME_FIELD)
    )

    update_checkpoint(TABLE_NAME, max_timestamp)

    print(f"Ingested {len(records)} tickets.")


if __name__ == "__main__":
    main()
