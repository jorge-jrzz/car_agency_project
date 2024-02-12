import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']
TOKEN_PICKLE = 'token.pickle'


# def test(date, time):
#     start_datetieme = f"{date}T{time}-06:00"
#     init_hour = datetime.combine(
#         datetime.strptime(date, "%Y-%m-%d"), datetime.strptime(time, "%H:%M:%S").time())
#     modified_time = init_hour + timedelta(minutes=90)
#     modified_time_str = modified_time.strftime("%H:%M:%S")
#     end_datetime = f"{date}T{modified_time_str}-06:00"
#     print("start", start_datetieme)
#     print("end", end_datetime)


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


# def create_event(date, time):

#     # Convertir la fecha y la hora en cadena para el formato de fecha y hora de Google Calendar
#     start_datetieme = f"{date}T{time}-06:00"
#     init_hour = datetime.combine(
#         datetime.strptime(date, "%Y-%m-%d"), datetime.strptime(time, "%H:%M:%S").time())
#     modified_time = init_hour + timedelta(minutes=90)
#     modified_time_str = modified_time.strftime("%H:%M:%S")
#     end_datetime = f"{date}T{modified_time_str}-06:00"

#     try:
#         # Autenticar y obtener las credenciales
#         creds = authenticate_google_calendar()

#         service = build("calendar", "v3", credentials=creds)

#         # Crear un evento
#         event = {
#             'summary': 'Evento creado desde Python',
#             'location': 'Universidad Autónoma Metropolitana Unidad Cuajimalpa, Vasco de Quiroga 4871, Contadero, Cuajimalpa de Morelos, 05348 Ciudad de México, CDMX, México',
#             'description': 'A chance to hear more about Google\'s developer products.',
#             'start': {
#                 'dateTime': start_datetieme,
#                 'timeZone': 'America/Mexico_City',
#             },
#             'end': {
#                 'dateTime': end_datetime,
#                 'timeZone': 'America/Mexico_City',
#             },
#             'attendees': [
#                 {'email': 'eduardo.glez7828@gmail.com'},
#             ],
#         }

#         event = service.events().insert(calendarId='primary', body=event).execute()
#         print(f'Evento creado: {event.get("htmlLink")}')

#     except HttpError as error:
#         print(f"An error occurred: {error}")


# if __name__ == '__main__':
#     create_event()
