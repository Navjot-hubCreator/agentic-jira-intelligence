# data.py

TICKETS = {
    "JIRA-101": {
        "id": "JIRA-101",
        "title": "Implement AML transaction monitoring system",
        "description": "Build real-time AML monitoring for banking transactions",
        "date": "2026-04-01",
        "type": "backend"
    },
    "JIRA-102": {
        "id": "JIRA-102",
        "title": "UI dashboard redesign",
        "description": "Improve dashboard UX for compliance team",
        "date": "2026-04-05",
        "type": "ui"
    },
    "JIRA-103": {
        "id": "JIRA-103",
        "title": "ETL pipeline optimization",
        "description": "Optimize data pipelines for reporting",
        "date": "2026-04-10",
        "type": "etl"
    }
}


def get_ticket_data(ticket_id):
    return TICKETS.get(ticket_id, {})