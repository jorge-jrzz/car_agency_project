import flet as ft
from view.home_page_manager import chart, toggle_data, avg_button, container_ventas


def main(page: ft.Page):
    avg_button.on_click = lambda _: toggle_data(_, chart)
    page.add(avg_button, container_ventas)


ft.app(target=main)
