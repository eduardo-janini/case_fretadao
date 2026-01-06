from .api import fetch
from .ingestion_engine import load_raw_incremental
from .table_schema import get_checkpoint, update_checkpoint

TABLE_NAME = "raw_ticket_sla_events"
ENDPOINT = "ticket_sla_events"
TIME_FIELD = "time"


def main():
    last_checkpoint = get_checkpoint(TABLE_NAME)

    params = {}
    if last_checkpoint:
        params["start_time"] = last_checkpoint.isoformat()

    response = fetch(ENDPOINT, params=params)
    records = response.get("data", [])

    if not records:
        print("No new tickets to ingest.")
        return

    load_raw_incremental(TABLE_NAME, records)

    max_timestamp = max(
        r[TIME_FIELD] for r in records if r.get(TIME_FIELD)
    )

    update_checkpoint(TABLE_NAME, max_timestamp)

    print(f"Ingested {len(records)} ticket sla events.")


if __name__ == "__main__":
    main()
