from .api import fetch
from .ingestion_engine import load_raw_full_refresh

def main():
    data = fetch("organizations").get("data", [])
    load_raw_full_refresh("raw_organizations", data)

if __name__ == "__main__":
    main()