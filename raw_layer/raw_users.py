from .api import fetch
from .ingestion_engine import load_raw

def main():
    data = fetch("users").get("data", [])
    load_raw("raw_users", data)

if __name__ == "__main__":
    main()