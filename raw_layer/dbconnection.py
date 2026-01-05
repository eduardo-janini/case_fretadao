import psycopg2
from .dbconfig import DB_CONFIG

def get_connection():
    return psycopg2.connect(**DB_CONFIG)
