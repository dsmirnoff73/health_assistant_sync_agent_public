import os
import gspread
from google.oauth2.service_account import Credentials

SPREADSHEET_NAME = os.getenv("SPREADSHEET_NAME")
SHEET_NAME = os.getenv("SHEET_NAME", "08_Прогресс")

def write_to_sheets(entry):
    creds_path = os.getenv("GOOGLE_SERVICE_ACCOUNT_FILE")
    creds = Credentials.from_service_account_file(creds_path, scopes=["https://www.googleapis.com/auth/spreadsheets"])
    client = gspread.authorize(creds)
    sheet = client.open_by_key(SPREADSHEET_NAME).worksheet(SHEET_NAME)
    sheet.append_row([
        entry["date"],
        entry["weight"],
        entry["sleep"],
        entry["stress"],
        entry["libido"]
    ])
