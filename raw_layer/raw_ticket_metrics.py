# raw_layer/raw_ticket_metrics.py
"""
Este módulo é responsável por ingerir métricas de tickets a partir de uma API. 
Funções principais:
- `main()`: A função principal que controla o fluxo de ingestão de dados. 
    1. Obtém o último ponto de verificação (checkpoint) para saber a partir de quando buscar novos dados.
    2. Faz uma chamada à API para buscar métricas de tickets, passando o tempo de início se houver um checkpoint.
    3. Se não houver novos registros, informa que não há novos tickets para ingerir.
    4. Caso existam novos registros, carrega os dados de forma incremental.
    5. Atualiza o checkpoint com o timestamp máximo dos registros ingeridos.
    6. Exibe a quantidade de métricas de tickets ingeridas.
Constantes:
- `TABLE_NAME`: Nome da tabela onde as métricas de tickets são armazenadas.
- `ENDPOINT`: Endpoint da API que fornece as métricas de tickets.
- `TIME_FIELD`: Campo que representa o timestamp de criação dos tickets.
O arquivo deve ser executado como um script, iniciando a ingestão de dados quando chamado diretamente.
"""


from .api import fetch
from .ingestion_engine import load_raw_incremental
from .table_schema import get_checkpoint, update_checkpoint

TABLE_NAME = "raw_ticket_metrics"
ENDPOINT = "ticket_metrics"
TIME_FIELD = "created_at"


def main():
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

    max_timestamp = max(
        r[TIME_FIELD] for r in records if r.get(TIME_FIELD)
    )

    update_checkpoint(TABLE_NAME, max_timestamp)

    print(f"Ingested {len(records)} ticket metrics.")


if __name__ == "__main__":
    main()
