import requests
import psycopg2
import json
from dbconfig import DB_CONFIG

API_URL = "http://localhost:8000/groups"

conn = psycopg2.connect(**DB_CONFIG)

cur = conn.cursor()

cur.execute("""
drop table if exists raw_groups cascade;   
create table if not exists raw_groups (payload jsonb);
""")

response = requests.get(API_URL)
response.raise_for_status()

groups = response.json()

for group in groups.get("data", []):
    cur.execute(
        "insert into raw_groups (payload) values (%s)",
        [json.dumps(group)]
    )

conn.commit()
cur.close()
conn.close()
