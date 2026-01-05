import requests
import psycopg2
import json
from .dbconfig import DB_CONFIG

API_URL = "http://localhost:8000/organizations"

conn = psycopg2.connect(**DB_CONFIG)

cur = conn.cursor()

cur.execute("""
drop table if exists raw_organizations cascade;   
create table if not exists raw_organizations (payload jsonb);
""")

response = requests.get(API_URL)
response.raise_for_status()

organizations = response.json()

for organization in organizations.get("data", []):
    cur.execute(
        "insert into raw_organizations (payload) values (%s)",
        [json.dumps(organization)]
    )

conn.commit()
cur.close()
conn.close()
