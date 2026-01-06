import json
from .dbconnection import get_connection

def load_raw_incremental(table_name, records):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(f"""
        create table if not exists {table_name} (payload jsonb);
    """)

    for record in records:
        cur.execute(
            f"insert into {table_name} (payload) values (%s)",
            [json.dumps(record)]
        )

    conn.commit()
    cur.close()
    conn.close()

def load_raw_full_refresh(table_name, records):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(f"""
        create table if not exists {table_name} (
            payload jsonb
        );
    """)

    cur.execute(f"truncate table {table_name};")

    for record in records:
        cur.execute(
            f"insert into {table_name} (payload) values (%s)",
            [json.dumps(record)]
        )

    conn.commit()
    cur.close()
    conn.close()