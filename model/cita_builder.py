from datetime import datetime, timedelta
from pprint import pprint


class CitaBuilder:
    def __init__(self, cliente):
        self.cita = Cita(cliente)

    def add_description(self, datos_carro):
        self.cita.description = datos_carro
        return self

    def add_cost(self, costo):
        self.cita.cost = costo
        return self

    def _start_datetime(self, date, time):
        start_datetieme = f"{date}T{time}-06:00"
        return start_datetieme

    def add_start_datetime(self, date, time):
        self.cita.start_datetime = self._start_datetime(date, time)
        return self

    def add_attendee(self, correo_cliente):
        self.cita.attendee = correo_cliente
        return self

    def build(self):
        return self.cita


class Cita:
    def __init__(self, client):
        self.client = client
        self.description = ""
        self.cost = 0
        self.start_datetime = ""
        self.end_datetime = ""
        self.attendee = ""

    def _end_datetime(self, start_datetime):
        date_og = start_datetime[:10]
        all_date = start_datetime.replace("T", " ").replace("-06:00", "")
        init_hour = datetime.strptime(all_date, "%Y-%m-%d %H:%M:%S")
        modified_time = init_hour + timedelta(minutes=90)
        modified_time_str = modified_time.strftime("%H:%M:%S")
        end_datetime = f"{date_og}T{modified_time_str}-06:00"

        return end_datetime

    def to_dict_for_calendar(self):
        return {
            'summary': f'Servicio para {self.client}',
            'location': 'Universidad Autónoma Metropolitana Unidad Cuajimalpa, Vasco de Quiroga 4871, Contadero, Cuajimalpa de Morelos, 05348 Ciudad de México, CDMX, México',
            'description': self.description,
            'start': {
                'dateTime': self.start_datetime,
                'timeZone': 'America/Mexico_City',
            },
            'end': {
                'dateTime': self._end_datetime(self.start_datetime),
                'timeZone': 'America/Mexico_City',
            },
            'attendees': [
                {'email': self.attendee},
            ],
        }


# Ejemplo de uso:
# cliente_nombre = "Juancho Pancho"
# builder = CitaBuilder(cliente_nombre)
# cita = (
#     builder
#     .add_description("Nissan Tsuru 2005")
#     .add_cost(2003.50)
#     .add_start_datetime("2024-02-18", "12:30:00")
#     .add_attendee("correo@cliente.com")
#     .build()
# )

# body_date = cita.to_dict_for_calendar()

# pprint(body_date)

# event.create_event(body_date)
