def sync_issue(issue_id: str, status: str) -> dict:
    return {
        "issue_id": issue_id,
        "status": status,
        "synced": True,
        "note": "Mock Linear sync completed.",
    }
