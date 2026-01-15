from gmail_service import get_gmail_service, fetch_unread_messages

service = get_gmail_service()
messages = fetch_unread_messages(service)

print(f"Unread emails found: {len(messages)}")

for msg in messages[:5]:
    print("Message ID:", msg["id"])
