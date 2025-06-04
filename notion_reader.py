import os
from notion_client import Client

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")
notion = Client(auth=NOTION_TOKEN)

def get_latest_entry():
    response = notion.databases.query(
        database_id=DATABASE_ID,
        sorts=[{"timestamp": "created_time", "direction": "descending"}],
        page_size=1
    )
    results = response.get("results", [])
    if not results:
        return None

    row = results[0]["properties"]
    return {
        "date": results[0]["created_time"],
        "weight": row.get("Вес", {}).get("number"),
        "sleep": row.get("Сон", {}).get("number"),
        "stress": row.get("Стресс", {}).get("number"),
        "libido": row.get("Либидо", {}).get("number")
    }
