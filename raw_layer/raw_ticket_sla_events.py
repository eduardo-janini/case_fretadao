from .api import fetch
from .ingestion_engine import load_raw

def main():
    data = fetch("ticket_sla_events").get("data", [])
    load_raw("raw_ticket_sla_events", data)

if __name__ == "__main__":
    main()