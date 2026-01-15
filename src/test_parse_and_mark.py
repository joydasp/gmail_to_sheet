from gmail_service import get_gmail_service, fetch_unread_messages, mark_as_read
from email_parser import parse_message

service = get_gmail_service()
messages = fetch_unread_messages(service)

print(f"Unread emails: {len(messages)}")

for msg in messages[:3]:
    full_msg = service.users().messages().get(
        userId="me", id=msg["id"], format="full"
    ).execute()

    parsed = parse_message(full_msg)

    print("FROM:", parsed["from"])
    print("SUBJECT:", parsed["subject"])
    print("DATE:", parsed["date"])
    print("CONTENT:", parsed["content"][:200])
    print("-" * 50)

    mark_as_read(service, msg["id"])
