import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def connect():
    creds = None
    SCOPE = "https://www.googleapis.com/auth/tasks"

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPE)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists("credentials.json"):
                raise FileNotFoundError('File with credentials must be in same folder and be named credentials.json')
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPE
            )
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    try:
        service = build("tasks", "v1", credentials=creds)
        return service
    except HttpError as err:
        print(err)