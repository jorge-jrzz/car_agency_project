import flet as ft
from pages.sign_in import sign_in
from pages.sign_up import sign_up
from pages.home_page_client import main_content, from_car, date_picker, time_picker, buttons_schedule
from pages.home_page_admin import dates_table, give_price, edit_price


def main(page: ft.Page):
    page.title = "Proyecto final"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    page.add(main_content)

    # def page_resize(e):
    #     print("New page size:", page.window_width, page.window_height)

    # page.on_resize = page_resize


ft.app(target=main)
