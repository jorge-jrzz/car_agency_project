import flet as ft
import logging
from model.db import autenticar_usuario
from view.sign_in import operator_or_management, change_from, buttom_submit, sign_in
from view.home_page_manager import manager
from view.home_page_operator import operator
from view.home_page_admin import administrador

# Configura el logger
logging.basicConfig(level=logging.INFO, filename='logs/logs.txt',
                    filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')


def main(page: ft.Page):
    page.title = "Agencia de Autos"
    page.window_width = 845
    page.window_height = 555
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_center()

    operator_or_management.content.controls[1].on_change = lambda _: change_from(
        _, page)

    def login(e):
        rol = sign_in.content.controls[1].content.controls[0].content.controls[1].value
        rol = "secretaria" if rol is False else "gestion"
        if rol == "gestion":
            rol = sign_in.content.controls[1].content.controls[3].content.controls[1].value
            rol = "gerente" if rol is False else "administrador"

        username = sign_in.content.controls[1].content.controls[1].value
        password = sign_in.content.controls[1].content.controls[2].value

        door = autenticar_usuario(username, password, rol)

        # Agregar log según el resultado del inicio de sesión
        if door:
            logging.info(
                'Inicio de sesion exitoso: Usuario - %s, Rol - %s', username, rol)
        else:
            logging.warning(
                'Inicio de sesion fallido: Usuario - %s, Rol - %s', username, rol)

        if door is True and rol == "secretaria":
            ft.app(target=operator)
        elif door is True and rol == "gerente":
            ft.app(target=manager)
        elif door is True and rol == "administrador":
            ft.app(target=administrador)

    buttom_submit.content.on_click = login

    page.add(sign_in)


if __name__ == "__main__":
    ft.app(target=main)
