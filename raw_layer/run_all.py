from .raw_groups import main as run_groups
from .raw_organizations import main as run_organizations
from .raw_users import main as run_users
from .raw_tickets import main as run_tickets
from .raw_ticket_metrics import main as run_ticket_metrics
from .raw_ticket_sla_events import main as run_ticket_sla_events


def main():
    print("Starting raw layer ingestion...")

    run_groups()
    run_organizations()
    run_users()
    run_tickets()
    run_ticket_metrics()
    run_ticket_sla_events()

    print("Raw layer ingestion completed successfully.")


if __name__ == "__main__":
    main()
