import time
from notion_reader import get_latest_entry
from sheets_writer import write_to_sheets
from dotenv import load_dotenv
import os

load_dotenv()


def run_sync():
    entry = get_latest_entry()
    if entry:
        write_to_sheets(entry)
    else:
        print("Нет новых данных для синхронизации.")


