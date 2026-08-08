import os, json
os.environ['HERMES_HOME'] = r'C:\Users\nutsdevs\AppData\Local\hermes\profiles\bess'
os.environ['GOOGLE_TOKEN_PATH'] = r'C:\Users\nutsdevs\AppData\Local\hermes\profiles\bess\google_token.json'

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

token_path = os.environ['GOOGLE_TOKEN_PATH']
creds = Credentials.from_authorized_user_file(token_path)
if creds.expired and creds.refresh_token:
    creds.refresh(Request())
    with open(token_path, 'w') as f: f.write(creds.to_json())

drive_svc = build('drive', 'v3', credentials=creds)
folder_id = "1GjfqDCjyH60ERuMTrfjgTDopSOV-KG1h"

media = MediaFileUpload(
    r"D:\hermes-bess-project\docs\legalai_master_project_blueprint.md",
    mimetype='text/markdown',
    resumable=True
)

file_metadata = {
    'name': '📋 LegalAI Thailand — Master Project Blueprint',
    'parents': [folder_id],
    'mimeType': 'application/vnd.google-apps.document'
}

uploaded = drive_svc.files().create(
    body=file_metadata,
    media_body=media,
    fields='id,webViewLink'
).execute()

print(f"✅ https://docs.google.com/document/d/{uploaded['id']}/edit")
