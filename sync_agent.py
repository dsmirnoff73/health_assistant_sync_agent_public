import time
from notion_reader import get_latest_entry
from sheets_writer import write_to_sheets
from dotenv import load_dotenv
import os

load_dotenv()
print("🔍 NOTION_TOKEN:", os.getenv("NOTION_TOKEN")[:12], "...")
print("📄 NOTION_DATABASE_ID:", os.getenv("NOTION_DATABASE_ID"))

def run_sync():
    entry = get_latest_entry()
    if entry:
        write_to_sheets(entry)
    else:
        print("Нет новых данных для синхронизации.")

if __name__ == "__main__":
    run_sync()
