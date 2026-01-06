# raw_layer/run_all.py
"""
Este módulo é responsável por iniciar o processo de ingestão da camada bruta de dados.
Ele importa funções de vários módulos relacionados a grupos, organizações, usuários,
tickets, métricas de tickets e eventos de SLA de tickets, e executa essas funções em
sequência.
A função principal `main()` imprime uma mensagem de início, chama as funções de ingestão
de dados de cada um dos módulos importados e, ao final, imprime uma mensagem de conclusão
indicando que a ingestão foi realizada com sucesso.
A execução deste módulo ocorre apenas se ele for chamado diretamente, ou seja, se for
executado como o programa principal.
"""


from .raw_groups import main as run_groups
from .raw_organizations import main as run_organizations
from .raw_users import main as run_users
from .raw_tickets import main as run_tickets
from .raw_ticket_metrics import main as run_ticket_metrics
from .raw_ticket_sla_events import main as run_ticket_sla_events


def main():
    print("Starting raw layer ingestion...")

    run_groups()
    run_organizations()
    run_users()
    run_tickets()
    run_ticket_metrics()
    run_ticket_sla_events()

    print("Raw layer ingestion completed successfully.")


if __name__ == "__main__":
    main()
