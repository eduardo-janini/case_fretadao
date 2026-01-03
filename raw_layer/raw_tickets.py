import requests
import psycopg2
import json

API_URL = "http://localhost:8000/tickets"

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="datawarehouse",
    user="postgres",
    password="admin"
)

cur = conn.cursor()

cur.execute("""
--drop table if exists raw_tickets;   
create table if not exists raw_tickets (payload jsonb);
""")

response = requests.get(API_URL)
response.raise_for_status()

tickets = response.json()
print(tickets["data"])

for ticket in tickets["data"]:
    cur.execute(
        "insert into raw_tickets (payload) values (%s)",
        [json.dumps(ticket)]
    )

conn.commit()
cur.close()
conn.close()
