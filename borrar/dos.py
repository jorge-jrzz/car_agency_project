import flet as ft
from uno import button_clicked, b, t


def si(page: ft.Page):
    page.title = "Text button with 'click' event"

    # Crea un botón y configura 'button_clicked' como su controlador de eventos
    b.on_click = lambda _: button_clicked(_, page)

    # Añade el botón a la página
    page.add(b, t)


ft.app(target=si)
