import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']
TOKEN_PICKLE = 'token.pickle'


def authenticate_google_calendar():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("model/token.json"):
        creds = Credentials.from_authorized_user_file(
            "model/token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "model/credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("model/token.json", "w") as token:
            token.write(creds.to_json())
    return creds


def create_event(event):
    try:
        # Autenticar y obtener las credenciales
        creds = authenticate_google_calendar()

        service = build("calendar", "v3", credentials=creds)

        # Crear un evento
        cita = service.events().insert(calendarId='primary', body=event).execute()
        print(f'Evento creado: {cita.get("htmlLink")}')

    except HttpError as error:
        print(f"An error occurred: {error}")
