import flet as ft
import datetime
from model.db import dates_6_months_ago
from model import event
from model import *


clientes = dates_6_months_ago()


def operator(page: ft.Page):
    page.title = "Operador"
    page.window_width = 1175
    page.window_height = 640

# Alertas para llamar a los clientes
    call_numbers = []
    for item, cliente in enumerate(clientes):
        alerta = ft.AlertDialog(
            modal=True,
            title=ft.Text(cliente['telefono']),
            content=ft.Text(f"Cliente: {cliente['name']}"),
            actions=[
                ft.TextButton(
                    "Regresar",
                    # on_click=close_dlgs[item]
                )
            ]
        )
        call_numbers.append(alerta)

# Función para cerrar las diferentes alertas
    close_dlgs = []
    for call in call_numbers:
        def close_dlg(e, call=call):
            call.open = False
            page.update()

        close_dlgs.append(close_dlg)

# Asignar la función de cerrar a cada alerta
    for alertas in call_numbers:
        alertas.actions[0].on_click = close_dlgs[call_numbers.index(alertas)]

# Función para abrir las diferentes alertas
    open_dialogs = []
    for call in call_numbers:
        def open_number_call(e, call=call):
            page.dialog = call
            call.open = True
            page.update()

        open_dialogs.append(open_number_call)

# Botones para llamar a los clientes
    call_buttons = []
    for call in call_numbers:
        call_button = ft.ElevatedButton(
            "Llamar",
            icon=ft.icons.PHONE,
        )
        call_buttons.append(call_button)

    for button in call_buttons:
        button.on_click = open_dialogs[call_buttons.index(button)]

    change_color_funtions = []
    for item, cliente in enumerate(clientes):
        def change_color(e, item=item):
            for tarjeta in cards_clients:
                valor = tarjeta.content.content.controls[1].controls[1].value
                print(valor)
                if valor == "Atendido":
                    print("hola?")
                    tarjeta.content.color = "blue"
                    tarjeta.update()
                    break
                elif tarjeta.content.key == item and valor == "Pendiente":
                    tarjeta.content.color = "red"
                    tarjeta.update()
                    break

        change_color_funtions.append(change_color)


# Dropdowns para seleccionar el estatus de la cita
    dropdowns_select_status = []
    for item, cliente in enumerate(clientes):
        dropdown_status = ft.Dropdown(
            label="Estatus",
            options=[
                ft.dropdown.Option("Pendiente"),
                ft.dropdown.Option("Atendido"),
            ],
            width=200,
            on_change=change_color_funtions[item]
        )
        dropdowns_select_status.append(dropdown_status)


# Date pickers para seleccionar la fecha de la cita
    date_pickers = []
    for item, cliente in enumerate(clientes):
        date_picker = ft.DatePicker(
            confirm_text="Confirmar",
            cancel_text="Cancelar",
            first_date=datetime.datetime(2024, 1, 1),
            last_date=datetime.datetime(2024, 12, 31),
            on_change=lambda _: change_date_funtions[item](_),
        )
        date_pickers.append(date_picker)

# Time pickers para seleccionar la hora de la cita
    time_pickers = []
    for item, cliente in enumerate(clientes):
        time_picker = ft.TimePicker(
            confirm_text="Confirmar",
            cancel_text="Regresar",
            error_invalid_text="Time out of range",
            on_change=lambda _: get_event_data[item](_),
            on_dismiss=lambda _: date_pickers[item].pick_date(),
        )
        time_pickers.append(time_picker)

# Botones para agendar citas
    date_buttons = []
    for item, cliente in enumerate(clientes):
        date_button = ft.ElevatedButton(
            "Agendar",
            icon=ft.icons.EDIT_CALENDAR,
            on_click=lambda _: date_pickers[item].pick_date(),
        )
        date_buttons.append(date_button)

# Funciones para cambiar la fecha y hora de la cita
    change_date_funtions = []
    for item, cliente in enumerate(clientes):
        def change_date(e, date_picker=date_pickers[item], time_picker=time_pickers[item]):
            date = date_picker.value.strftime("%Y-%m-%d")
            time_picker.pick_time()
            return date

        change_date_funtions.append(change_date)

# Funciones para cambiar la hora de la cita
    get_event_data = []
    for item, cliente in enumerate(clientes):
        def change_time(e, time_picker=time_pickers[item], date_picker=date_pickers[item]):
            time = time_picker.value.strftime("%H:%M:%S")
            date = date_picker.value.strftime("%Y-%m-%d")
            print(f"Fecha seleccionada {date}")
            print(f"Hora selecionada {time}")
            # event.create_event(date, time)

        get_event_data.append(change_time)

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

# Crear tarjetas para cada resultado
    cards_clients = []
    for item, cliente in enumerate(clientes):
        carta = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.CALENDAR_MONTH),
                            title=ft.Text(cliente['name']),
                            subtitle=ft.Column([
                                ft.Text(
                                    f"{cliente['marca']}, {cliente['modelo']}, {cliente['year']}, {cliente['color']}, {cliente['propulsion']}"),
                                ft.Text(cliente['email']),
                            ])
                        ),
                        ft.Row(
                            controls=[
                                call_buttons[item],
                                dropdowns_select_status[item],
                                date_buttons[item],
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )
        cards_clients.append(carta)

        # page.add(carta)

    principal = ft.ResponsiveRow()

    for card in cards_clients:
        principal.controls.append(ft.Container(
            card, col={"sm": 6, "md": 6, "xl": 4}))

    for alerta in call_numbers:
        page.overlay.append(alerta)
    for date in date_pickers:
        page.overlay.append(date)
    for time in time_pickers:
        page.overlay.append(time)

    page.add(principal)


# ft.app(target=main)
