# raw_layer/raw_ticket_sla_events.py
"""
Este módulo é responsável por ingerir eventos de SLA de tickets a partir de uma API. 
Funções principais:
- `main()`: Função principal que gerencia o fluxo de ingestão dos eventos de SLA. 
    - Obtém o último ponto de verificação (checkpoint) para saber a partir de quando buscar novos eventos.
    - Faz uma chamada à API para buscar os eventos de SLA de tickets, passando o tempo de início se houver um checkpoint.
    - Se não houver novos registros, informa que não há novos tickets para ingerir.
    - Caso haja novos registros, carrega os dados na camada bruta (raw layer) e atualiza o checkpoint com o timestamp máximo dos registros ingeridos.
Constantes:
- `TABLE_NAME`: Nome da tabela onde os eventos de SLA serão armazenados.
- `ENDPOINT`: Endpoint da API que fornece os eventos de SLA.
- `TIME_FIELD`: Campo que representa o timestamp dos eventos.
O arquivo deve ser executado como um script, chamando a função `main()` quando o módulo é executado diretamente.
"""


from .api import fetch
from .ingestion_engine import load_raw_incremental
from .table_schema import get_checkpoint, update_checkpoint

TABLE_NAME = "raw_ticket_sla_events"
ENDPOINT = "ticket_sla_events"
TIME_FIELD = "time"


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

    print(f"Ingested {len(records)} ticket sla events.")


if __name__ == "__main__":
    main()
