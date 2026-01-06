# raw_layer/drop_tables.py
"""
Este módulo contém a função `reset_raw_layer`, que é responsável por redefinir a camada bruta de dados em um banco de dados. 
A função realiza as seguintes operações:
1. Estabelece uma conexão com o banco de dados utilizando a função `get_connection`.
2. Para cada tabela listada em `RAW_TABLES`, executa um comando SQL para remover a tabela, se existir, utilizando a cláusula `cascade` para garantir que todas as dependências sejam removidas.
3. Limpa a tabela `ingestion_checkpoint`, que é utilizada para rastrear o progresso da ingestão de dados.
4. Comita as alterações no banco de dados e fecha a conexão.
Ao final, imprime uma mensagem indicando que a redefinição da camada bruta foi concluída.
O script é executado diretamente quando chamado como o programa principal.
"""


from .dbconnection import get_connection

RAW_TABLES = [
    "raw_tickets",
    "raw_ticket_metrics",
    "raw_ticket_sla_events",
    "raw_users",
    "raw_groups",
    "raw_organizations",
]


def reset_raw_layer():
    conn = get_connection()
    cur = conn.cursor()

    for table in RAW_TABLES:
        cur.execute(f"drop table if exists {table} cascade;")

    # limpa checkpoints também
    cur.execute("delete from ingestion_checkpoint;")

    conn.commit()
    cur.close()
    conn.close()

    print("Raw layer reset completed.")


if __name__ == "__main__":
    reset_raw_layer()
