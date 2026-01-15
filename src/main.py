from gmail_service import get_gmail_service, fetch_unread_messages, mark_as_read
from email_parser import parse_message
from sheets_service import get_sheets_service, append_row

SPREADSHEET_ID = "1f5x4w_lfg7Vycssyv6Ah4MEjLH8udZBBmuDZ51G3XdQ"

gmail = get_gmail_service()
sheets = get_sheets_service()

messages = fetch_unread_messages(gmail)[:10]

print(f"Processing {len(messages)} unread emails")

for msg in messages:
    full_msg = gmail.users().messages().get(
        userId="me", id=msg["id"], format="full"
    ).execute()

    parsed = parse_message(full_msg)

    append_row(
        sheets,
        SPREADSHEET_ID,
        [
            parsed["from"],
            parsed["subject"],
            parsed["date"],
            parsed["content"]
        ]
    )

    mark_as_read(gmail, msg["id"])

print("✅ Emails successfully logged to Google Sheets")
