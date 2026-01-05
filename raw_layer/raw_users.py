import requests
import psycopg2
import json
from dbconfig import DB_CONFIG

API_URL = "http://localhost:8000/users"

conn = psycopg2.connect(**DB_CONFIG)
cur = conn.cursor()

cur.execute("""
drop table if exists raw_users cascade;   
create table if not exists raw_users (payload jsonb);
""")

response = requests.get(API_URL)
response.raise_for_status()

users = response.json()

for user in users.get("data", []):
    cur.execute(
        "insert into raw_users (payload) values (%s)",
        [json.dumps(user)]
    )

conn.commit()
cur.close()
conn.close()
