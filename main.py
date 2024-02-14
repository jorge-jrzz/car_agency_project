import flet as ft
from model.db import DatabaseSingleton, autenticar_usuario
from view.sign_in import operator_or_management, change_from, buttom_submit, sign_in
from view.home_page_manager import chart, toggle_data, avg_button, container_ventas
from view.home_page_operator import (
    operator
)


def main(page: ft.Page):
    page.title = "Proyecto final"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

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
        if door is True and rol == "secretaria":
            # page.window_close()
            # page.clean()
            ft.app(target=operator)
            page.update()
        elif door is True and rol == "gerente":
            page.clean()
            page.add(avg_button, container_ventas)

    buttom_submit.content.on_click = login

    avg_button.on_click = lambda _: toggle_data(_, chart)

    page.add(sign_in)

    # def page_resize(e):
    #     print("New page size:", page.window_width, page.window_height)

    # page.on_resize = page_resize


ft.app(target=main)
