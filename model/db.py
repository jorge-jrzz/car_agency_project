import sqlite3
from datetime import datetime, timedelta


class DatabaseSingleton:
    database_file = "db/database.db"

    def __init__(self):
        self._connection = sqlite3.connect("db/database.db")

    @property
    def connection(self):
        return self._connection

    #
    # def __new__(cls):
    #     if not cls._instance:
    #         cls._instance = super(DatabaseSingleton, cls).__new__(cls)
    #         cls._instance.connection = sqlite3.connect(cls.database_file)
    #     return cls._instance

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada")

    def __del__(self):
        self.close_connection()


def autenticar_usuario(username, password, rol):
    print(username, password, rol)
    # Obtener la instancia del Singleton
    db_instance = DatabaseSingleton()

    # Obtener la conexión a la base de datos
    connection = db_instance.connection

    try:
        # Ejecutar una consulta para verificar las credenciales
        query = "SELECT * FROM personal WHERE username=? AND password=? AND tipoUser=?"
        cursor = connection.cursor()
        cursor.execute(query, (username, password, rol))
        resultado = cursor.fetchone()

        # Verificar si se encontró el usuario
        if resultado:
            nombre_usuario, _, rol, turno = resultado
            print(
                f"Usuario autenticado: {nombre_usuario}, Rol: {rol}, Turno: {turno}")
            return True
        else:
            print("Autenticación fallida.")
            return False
    finally:
        db_instance.close_connection()


def dates_6_months_ago():
    db_instance = DatabaseSingleton()

    connection = db_instance.connection

    # Calcular la fecha de hace 6 meses desde hoy
    fecha_hace_6_meses = datetime.now() - timedelta(days=182)

    # Ejecutar la consulta SQL para obtener clientes con su última cita hace 6 meses
    query = "SELECT * FROM clientes WHERE UltimaCita <= ?;"
    cursor = connection.cursor()
    cursor.execute(query, (fecha_hace_6_meses.strftime('%Y-%m-%d'),))
    resultados = cursor.fetchall()

    # column_names = [description[0] for description in cursor.description]

    # resultados = [dict(zip(column_names, row)) for row in cursor.fetchall()]

    db_instance.close_connection()

    return resultados


def get_personal():
    db_instance = DatabaseSingleton()

    connection = db_instance.connection

    # Ejecutar una consulta para obtener los datos
    cursor = connection.cursor()
    cursor.execute("SELECT username, tipoUser, Turno FROM personal")
    personal = cursor.fetchall()

    db_instance.close_connection()

    return personal
