import logging
from model.db import autenticar_usuario

def login(username, password, rol):
    logging.info(f'Intento de inicio de sesión: Usuario - {username}, Rol - {rol}')
    door = autenticar_usuario(username, password, rol)
    if door:
        return rol
    else:
        logging.warning(f'Intento de inicio de sesión fallido: Usuario - {username}, Rol - {rol}')
        return None
