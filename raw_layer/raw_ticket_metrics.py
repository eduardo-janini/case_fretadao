import requests
import psycopg2
import json
from .dbconfig import DB_CONFIG

API_URL = "http://localhost:8000/ticket_metrics"

conn = psycopg2.connect(**DB_CONFIG)

cur = conn.cursor()

cur.execute("""
drop table if exists raw_ticket_metrics cascade;   
create table if not exists raw_ticket_metrics (payload jsonb);
""")

response = requests.get(API_URL)
response.raise_for_status()

ticket_metrics = response.json()

for ticket_metric in ticket_metrics.get("data", []):
    cur.execute(
        "insert into raw_ticket_metrics (payload) values (%s)",
        [json.dumps(ticket_metric)]
    )

conn.commit()
cur.close()
conn.close()
