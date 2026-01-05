import requests
import psycopg2
import json
from dbconfig import DB_CONFIG 

API_URL = "http://localhost:8000/tickets"

conn = psycopg2.connect(**DB_CONFIG)

cur = conn.cursor()

cur.execute("""
drop table if exists raw_tickets cascade;   
create table if not exists raw_tickets (payload jsonb);
""")

response = requests.get(API_URL)
response.raise_for_status()

tickets = response.json()

for ticket in tickets.get("data", []):
    cur.execute(
        "insert into raw_tickets (payload) values (%s)",
        [json.dumps(ticket)]
    )

conn.commit()
cur.close()
conn.close()
