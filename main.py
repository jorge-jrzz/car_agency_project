import flet as ft
from pages.sign_in import sign_in
from pages.sign_up import sign_up
from pages.home_page_client import main_content, from_car, date_picker, time_picker, buttons_schedule
from pages.home_page_admin import dates_table


def main(page: ft.Page):
    page.title = "Proyecto final"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    def register(e):
        # Codigo real
        # page.clean()
        # page.add(sign_up)
        # page.update()

        # Codigo ára probar el home page
        page.clean()
        page.add(main_content)
        page.update()

    def identify(e):
        page.clean()
        page.add(sign_in)
        page.update()

    def add_car(e):
        del main_content.content.controls[2]
        main_content.content.controls.append(from_car)
        page.update()

    def schedule_service(e):
        del main_content.content.controls[2]
        main_content.content.controls.append(buttons_schedule)
        page.update()

    sign_in.content.controls[1].content.controls[4].on_click = register
    sign_up.content.controls[0].content.controls[0].on_click = identify

    main_content.content.controls[0].on_change = add_car
    main_content.content.controls[0].leading.on_click = schedule_service

    # page.add(sign_in)
    page.add(dates_table)
    page.overlay.append(date_picker)
    page.overlay.append(time_picker)

    # def page_resize(e):
    #     print("New page size:", page.window_width, page.window_height)

    # page.on_resize = page_resize


ft.app(target=main)
