import datetime
import flet as ft
from model import event
from model import *


def main(page):
    page.title = "Card Example"
    page.window_width = 1125
    page.window_height = 630

    def change_date(e):
        date = date_picker.value.strftime("%Y-%m-%d")
        # print(f"Date picker changed, value is {date}")
        time_picker.pick_time()
        return date

    def change_time(e):
        time = time_picker.value.strftime("%H:%M:%S")
        date = date_picker.value.strftime("%Y-%m-%d")
        print(f"Date picker changed, value is {date}")
        print(f"Date picker dismissed, value is {time}")
        event.create_event(date, time)

    log_out = ft.Container(
        content=ft.TextButton(text="Cerrar sesión", style=ft.ButtonStyle(
            color="black", bgcolor=None, overlay_color=ft.colors.RED_500)),
        alignment=ft.Alignment(1, -1),
        expand=True
    )

    date_button = ft.ElevatedButton(
        "Agenar",
        icon=ft.icons.EDIT_CALENDAR,
        on_click=lambda _: date_picker.pick_date(),
    )

    date_picker = ft.DatePicker(
        on_change=change_date,
        confirm_text="Confirmar",
        cancel_text="Cancelar",
        first_date=datetime.datetime(2024, 1, 1),
        last_date=datetime.datetime(2024, 12, 31),
    )

    time_picker = ft.TimePicker(
        confirm_text="Confirmar",
        cancel_text="Regresar",
        error_invalid_text="Time out of range",
        help_text="Pick your time slot",
        on_change=change_time,
        on_dismiss=lambda _: date_picker.pick_date(),
    )

    carta = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.CALENDAR_MONTH),
                        title=ft.Text("Jorge Juarez"),
                        subtitle=ft.Column([
                            ft.Text("Chevrolet, Aveo 2019, Rojo, Gasolina"),
                            ft.Text("$ 300,000.00"),
                        ])
                    ),
                    ft.Row(
                        controls=[
                            ft.TextButton("Lammar"),
                            ft.Dropdown(
                                label="Estatus",
                                options=[
                                    ft.dropdown.Option("Pendiente"),
                                    ft.dropdown.Option("Atendido"),
                                ],
                                width=200
                            ),
                            date_button,
                        ],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ),
            width=400,
            padding=10,
        )
    )

    page.overlay.append(date_picker)
    page.overlay.append(time_picker)

    page.add(
        ft.ResponsiveRow(
            controls=[
                log_out,
                ft.Container(
                    carta,
                    col={"sm": 6, "md": 6, "xl": 4},
                ),
                ft.Container(
                    carta,
                    col={"sm": 6, "md": 6, "xl": 4},
                ),
                ft.Container(
                    carta,
                    col={"sm": 6, "md": 6, "xl": 4},
                ),
                ft.Container(
                    carta,
                    col={"sm": 6, "md": 6, "xl": 4},
                )
            ]
        )
    )

    # def page_resize(e):
    #     print("New page size:", page.window_width, page.window_height)

    # page.on_resize = page_resize


ft.app(target=main)
