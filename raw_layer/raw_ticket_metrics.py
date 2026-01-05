from .api import fetch
from .ingestion_engine import load_raw

def main():
    data = fetch("ticket_metrics").get("data", [])
    load_raw("raw_ticket_metrics", data)

if __name__ == "__main__":
    main()