import json
from .dbconnection import get_connection

def load_raw(table_name, records):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(f"""
        drop table if exists {table_name} cascade;
        --create table {table_name} (payload jsonb);
    """)

    # for record in records:
    #     cur.execute(
    #         f"insert into {table_name} (payload) values (%s)",
    #         [json.dumps(record)]
    #     )

    conn.commit()
    cur.close()
    conn.close()
