import flet as ft
from pages.home_page_client import main_content, from_car


def main(page: ft.Page):
    page.title = "Proyecto final"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    def add_car(e):
        del main_content.content.controls[2]
        main_content.content.controls.append(from_car)
        page.update()

    # main_content.content.controls[0].leading.on_click = add_car
    main_content.content.controls[0].on_change = add_car

    page.add(main_content)

    # def page_resize(e):
    #     print("New page size:", page.window_width, page.window_height)

    # page.on_resize = page_resize


ft.app(target=main)
