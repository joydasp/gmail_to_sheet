import base64
from email.utils import parsedate_to_datetime
from bs4 import BeautifulSoup


def _get_header(headers, name):
    for h in headers:
        if h["name"].lower() == name.lower():
            return h["value"]
    return ""


def _decode_body(payload):
    if "parts" in payload:
        for part in payload["parts"]:
            mime = part.get("mimeType", "")
            data = part.get("body", {}).get("data")
            if not data:
                continue

            decoded = base64.urlsafe_b64decode(data).decode("utf-8", errors="ignore")

            if mime == "text/plain":
                return decoded
            if mime == "text/html":
                return BeautifulSoup(decoded, "html.parser").get_text()

    data = payload.get("body", {}).get("data")
    if data:
        return base64.urlsafe_b64decode(data).decode("utf-8", errors="ignore")

    return ""


MAX_CONTENT_LENGTH = 4000  # safe limit for Google Sheets

def parse_message(message):
    headers = message["payload"]["headers"]

    sender = _get_header(headers, "From")
    subject = _get_header(headers, "Subject")
    date_raw = _get_header(headers, "Date")
    date = parsedate_to_datetime(date_raw).isoformat() if date_raw else ""

    body = _decode_body(message["payload"])

    if len(body) > MAX_CONTENT_LENGTH:
        body = body[:MAX_CONTENT_LENGTH] + "... [TRUNCATED]"

    return {
        "from": sender,
        "subject": subject,
        "date": date,
        "content": body.strip()
    }

