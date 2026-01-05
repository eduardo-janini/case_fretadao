from .api import fetch
from .ingestion_engine import load_raw

def main():
    data = fetch("groups").get("data", [])
    load_raw("raw_groups", data)

if __name__ == "__main__":
    main()