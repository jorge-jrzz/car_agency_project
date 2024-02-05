import datetime
import flet as ft


rail = ft.NavigationRail(
    selected_index=None,
    extended=False,
    label_type=ft.NavigationRailLabelType.ALL,
    min_width=100,
    min_extended_width=400,
    leading=ft.FloatingActionButton(
        icon=ft.icons.DATE_RANGE_ROUNDED, text="Agendar servicio"),
    group_alignment=-0.9,
    destinations=[
        ft.NavigationRailDestination(
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED, selected_icon=ft.icons.DIRECTIONS_CAR_FILLED, label="Agregar carro"
        )
    ],
    # on_change=lambda e: print("Selected destination:",
    #                           e.control.selected_index),
)


# Add date
def change_date(e):
    print(f"Date picker changed, value is {date_picker.value}")


def date_picker_dismissed(e):
    print(f"Date picker dismissed, value is {date_picker.value}")


date_picker = ft.DatePicker(
    on_change=change_date,
    on_dismiss=date_picker_dismissed,
    first_date=datetime.datetime(2023, 10, 1),
    last_date=datetime.datetime(2024, 10, 1),
)

date_button = ft.ElevatedButton(
    "Pick date",
    icon=ft.icons.CALENDAR_MONTH,
    on_click=lambda _: date_picker.pick_date(),
)


# Add time
def change_time(e):
    print(
        f"Time picker changed, value (minute) is {time_picker.value}")


def dismissed(e):
    print(f"Time picker dismissed, value is {time_picker.value}")


time_picker = ft.TimePicker(
    confirm_text="Confirm",
    error_invalid_text="Time out of range",
    help_text="Pick your time slot",
    on_change=change_time,
    on_dismiss=dismissed,
)

time_button = ft.ElevatedButton(
    "Pick time",
    icon=ft.icons.TIME_TO_LEAVE,
    on_click=lambda _: time_picker.pick_time(),
)


buttons_schedule = ft.Container(
    content=ft.Row(
        controls=[
            date_button,
            time_button
        ]
    ),
    alignment=ft.Alignment(1, -1)
)

log_out = ft.Container(
    content=ft.TextButton(text="Cerrar sesión", style=ft.ButtonStyle(
        color="black", bgcolor=None, overlay_color=ft.colors.RED_500)),
    alignment=ft.Alignment(1, -1),
    expand=True
)


from_car = ft.Container(
    content=ft.Column(
        controls=[
            ft.TextField(label="Marca"),
            ft.TextField(label="Módelo"),
            ft.TextField(label="Año", max_length=4),
            ft.TextField(label="Tipo"),
            ft.TextField(label="Placas"),
            ft.Dropdown(
                label="Motor",
                options=[
                    ft.dropdown.Option("Electrico"),
                    ft.dropdown.Option("Gasolina"),
                    ft.dropdown.Option("Disel")
                ]
            ),
            ft.Dropdown(
                label="Motor",
                options=[
                    ft.dropdown.Option("1.4L"),
                    ft.dropdown.Option("1.6L"),
                ]
            )
        ]
    )
)


main_content = ft.Container(
    content=ft.Row(
        controls=[
            rail,
            ft.VerticalDivider(width=1),
            ft.Text(""),
            log_out
        ]
    ),
    expand=True
)
