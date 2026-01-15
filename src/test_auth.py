from google_auth_oauthlib.flow import InstalledAppFlow
import os

SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/spreadsheets"
]


print("📂 Current working directory:", os.getcwd())

flow = InstalledAppFlow.from_client_secrets_file(
    "credentials/credentials.json",
    SCOPES
)

creds = flow.run_local_server(port=0)

token_path = os.path.join(os.getcwd(), "token.json")

with open(token_path, "w") as f:
    f.write(creds.to_json())

print("✅ OAuth login successful!")
print("📄 token.json written to:", token_path)
print("📁 Files in CWD:", os.listdir(os.getcwd()))
