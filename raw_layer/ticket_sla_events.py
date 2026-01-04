import requests
import psycopg2
import json

API_URL = "http://localhost:8000/ticket_sla_events"

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="datawarehouse",
    user="postgres",
    password="admin"
)

cur = conn.cursor()

cur.execute("""
--drop table if exists raw_ticket_sla_events cascade;   
create table if not exists raw_ticket_sla_events (payload jsonb);
""")

response = requests.get(API_URL)
response.raise_for_status()

ticket_sla_events = response.json()

for ticket_sla_event in ticket_sla_events.get("data", []):
    cur.execute(
        "insert into raw_ticket_sla_events (payload) values (%s)",
        [json.dumps(ticket_sla_event)]
    )

conn.commit()
cur.close()
conn.close()
