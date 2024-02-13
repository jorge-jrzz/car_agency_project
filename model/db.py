import sqlite3


class DatabaseSingleton:
    _instance = None

    def __new__(cls, database_file="db/database.db"):
        if not cls._instance:
            cls._instance = super(DatabaseSingleton, cls).__new__(cls)
            cls._instance.connection = sqlite3.connect(database_file)
        return cls._instance

    def get_connection(self):
        return self.connection


def autenticar_usuario(username, password, rol):
    # Obtener la instancia del Singleton
    db_instance = DatabaseSingleton()

    # Obtener la conexión a la base de datos
    connection = db_instance.get_connection()

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


# Ejemplo de uso para autenticar a un usuario
usuario = "RaulAdm"
contrasena = "admin2345"
rol = "administrador"

autenticar_usuario(usuario, contrasena, rol)
