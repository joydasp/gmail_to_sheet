from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

def get_sheets_service():
    creds = Credentials.from_authorized_user_file(
        "token.json", SCOPES
    )
    return build("sheets", "v4", credentials=creds)


def append_row(service, spreadsheet_id, values):
    service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range="A:D",
        valueInputOption="RAW",
        body={"values": [values]}
    ).execute()
