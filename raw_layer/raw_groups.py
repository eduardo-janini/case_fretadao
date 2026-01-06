from .api import fetch
from .ingestion_engine import load_raw_full_refresh

def main():
    data = fetch("groups").get("data", [])
    load_raw_full_refresh("raw_groups", data)
    
if __name__ == "__main__":
    main()