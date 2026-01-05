from .api import fetch
from .ingestion_engine import load_raw

def main():
    data = fetch("organizations").get("data", [])
    load_raw("raw_organizations", data)

if __name__ == "__main__":
    main()