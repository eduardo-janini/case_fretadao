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
