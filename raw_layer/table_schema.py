from .dbconnection import get_connection


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
