
from datetime import datetime, timedelta

# Hora en formato de cadena
hora_original_str = "09:00:00"

# Convertir la cadena a un objeto datetime (usando una fecha ficticia)
fecha_ficticia = datetime(2024, 2, 15)
hora_original = datetime.combine(
    fecha_ficticia, datetime.strptime(hora_original_str, "%H:%M:%S").time())

datetime.strptime(hora_original_str, "%H:%M:%S")

# Agregar una hora
hora_modificada = hora_original + timedelta(hours=1)

# Convertir la hora modificada a formato de cadena
hora_modificada_str = hora_modificada.strftime("%H:%M:%S")

print("Hora original:", hora_original_str)
print("Hora modificada (con una hora agregada):", hora_modificada_str)
