from .api import fetch
from .ingestion_engine import load_raw

def main():
    data = fetch("tickets").get("data", [])
    load_raw("raw_tickets", data)

if __name__ == "__main__":
    main()