import flet as ft
from sign_in import sign_in
from sign_up import sign_up


# this function describes the way to render the page, passing the whole data
def main(page: ft.Page):
    page.title = "Proyecto final"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    def register(e):
        page.clean()
        page.add(sign_up)
        page.update()

    sign_in.content.controls[1].content.controls[3].on_click = register
    page.add(sign_in)

    # def page_resize(e):
    #     print("New page size:", page.window_width, page.window_height)

    # page.on_resize = page_resize


ft.app(target=main)
