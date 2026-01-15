from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]

def get_gmail_service():
    creds = Credentials.from_authorized_user_file(
        "token.json", SCOPES
    )
    service = build("gmail", "v1", credentials=creds)
    return service


def fetch_unread_messages(service):
    response = service.users().messages().list(
        userId="me",
        q="is:unread"
    ).execute()

    return response.get("messages", [])

def mark_as_read(service, message_id):
    service.users().messages().modify(
        userId="me",
        id=message_id,
        body={"removeLabelIds": ["UNREAD"]}
    ).execute()
