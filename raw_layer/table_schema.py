# raw_layer/table_schema.py
"""Este módulo contém funções para gerenciar pontos de verificação (checkpoints) em um banco de dados.
Um ponto de verificação é utilizado para rastrear o último registro processado em uma tabela específica.
Funções:
- get_checkpoint(table_name): Recupera a data e hora do último processamento para a tabela especificada.
    Retorna None se não houver registro encontrado.
- update_checkpoint(table_name, last_processed_at): Atualiza ou insere um ponto de verificação para a tabela especificada,
    definindo a data e hora do último processamento. Se a tabela já tiver um ponto de verificação, ele será atualizado."""


from .dbconnection import get_connection

# Recupera o ponto de verificação para a tabela especificada
def get_checkpoint(table_name):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        select last_processed_at
        from ingestion_checkpoint
        where table_name = %s
        """,
        (table_name,)
    )

    row = cur.fetchone()
    cur.close()
    conn.close()

    return row[0] if row else None

# Atualiza ou insere o ponto de verificação para a tabela especificada
def update_checkpoint(table_name, last_processed_at):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        insert into ingestion_checkpoint (table_name, last_processed_at)
        values (%s, %s)
        on conflict (table_name)
        do update set last_processed_at = excluded.last_processed_at
        """,
        (table_name, last_processed_at)
    )

    conn.commit()
    cur.close()
    conn.close()
