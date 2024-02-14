import flet as ft
import datetime
import random
from model.db import dates_6_months_ago
from model.cita_builder import CitaBuilder
from model.event import create_event


# Función para generar un costo de servicio aleatorio entre 1500 y 3500
def generate_random_cost():
    return random.randint(1500, 3500)


# Obtener los clientes que han tenido una cita en los últimos 6 meses
clientes = dates_6_months_ago()


def operator(page: ft.Page):
    page.title = "Operador"
    page.window_width = 1175
    page.window_height = 640
    page.window_center()

# Boton para cerrar sesion
    log_out = ft.ElevatedButton(
        "Cerrar sesión",
        icon=ft.icons.LOGOUT,
        on_click=lambda _: page.window_destroy()
    )

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
                )
            ]
        )
        call_numbers.append(alerta)

# Función para cerrar las diferentes alertas, y poner en "Pendiente" la cita
    close_dlgs = []
    for item, cliente in enumerate(clientes):
        def close_dialog(e, item=item, alerta=call_numbers[item]):
            alerta.open = False
            dropdowns_select_status[item].value = "Pendiente"
            dropdowns_select_status[item].border_color = "orange"
            page.update()
        close_dlgs.append(close_dialog)

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

# Asignar la función de abrir a cada botón
    for button in call_buttons:
        button.on_click = open_dialogs[call_buttons.index(button)]

# Funciones para cambiar el color de las tarjetas dependiendo del estatus de la cita
    # change_color_funtions = []
    # for item, cliente in enumerate(clientes):
    #     def change_color(e, item=item):
    #         for tarjeta in cards_clients:
    #             valor = tarjeta.content.content.controls[1].controls[1].value
    #             print(valor)
    #             if valor == "Atendido":
    #                 print("hola?")
    #                 tarjeta.content.color = "blue"
    #                 tarjeta.update()
    #                 break
    #             elif tarjeta.content.key == item and valor == "Pendiente":
    #                 tarjeta.content.color = "red"
    #                 tarjeta.update()
    #                 break

    #     change_color_funtions.append(change_color)


# Dropdowns para seleccionar el estatus de la cita
    dropdowns_select_status = []
    for item, cliente in enumerate(clientes):
        dropdown_status = ft.Dropdown(
            disabled=True,
            label="Estatus",
            border_width=2,
            options=[
                ft.dropdown.Option("Pendiente"),
                ft.dropdown.Option("Atendido"),
            ],
            width=200,
        )
        dropdowns_select_status.append(dropdown_status)


# Time pickers para seleccionar la hora de la cita
    time_pickers = []
    for item, cliente in enumerate(clientes):
        time_picker = ft.TimePicker(
            confirm_text="Confirmar",
            cancel_text="Regresar",
            error_invalid_text="Time out of range",
            on_change=lambda _: get_event_data[item](_),
            on_dismiss=lambda _, item=item: date_pickers[item].pick_date(),
        )
        # print(time_picker.on_change)
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

# Funciones para cambiar la hora de la cita

    get_event_data = []

    for item, cliente in enumerate(clientes):
        # nombre = cliente['name']
        # print(f"Cliente: {clientes[item]['name']}")

        def change_time(e, time_picker=time_pickers[item], date_picker=date_pickers[item]):
            time = time_picker.value.strftime("%H:%M:%S")
            date = date_picker.value.strftime("%Y-%m-%d")
            print(f"Fecha seleccionada {date}")
            print(f"Hora selecionada {time}")
        # Obtener los datos de la tarjeta que esta marcada como "Pendiente"
            for tarjeta in cards_clients:
                valor = tarjeta.content.content.controls[1].controls[1].value
                if valor == "Pendiente":
                    name_client = tarjeta.content.content.controls[0].title.value
                    print(f"Cliente: {name_client}")
                    description = tarjeta.content.content.controls[0].subtitle.controls[0].value
                    print(f"Descripcion: {description}")
                    email = tarjeta.content.content.controls[0].subtitle.controls[1].value
                    print(f"Email: {email}")

                    builder = CitaBuilder(name_client)
                    cita = (
                        builder
                        .add_description(description)
                        .add_cost(generate_random_cost())
                        .add_start_datetime(date, time)
                        .add_attendee(email)
                        .build()
                    )

                    body_date = cita.to_dict_for_calendar()
                    create_event(body_date)

                    tarjeta.content.content.controls[1].controls[1].value = "Atendido"
                    tarjeta.content.content.controls[1].controls[1].border_color = "green"
                    tarjeta.update()
                    break

        get_event_data.append(change_time)


# Funciones para cambiar la fecha y hora de la cita
    change_date_funtions = []
    for item, cliente in enumerate(clientes):
        # def change_date(e, date_picker=date_pickers[item], time_picker=time_pickers[item]):
        def change_date(e, date_picker=date_pickers[item], time_picker=time_pickers[item]):
            date = date_picker.value.strftime("%Y-%m-%d")
            time_picker.pick_time()
            return date

        change_date_funtions.append(change_date)

# Añadir funcionalidad a los time pickers
    # for picker, time in enumerate(time_pickers):
    #     time_pickers[picker].on_change = lambda _, picker=picker: get_event_data[picker](
    #         _, picker)

    # date_picker = ft.DatePicker(
    #     on_change=change_date,
    #     confirm_text="Confirmar",
    #     cancel_text="Cancelar",
    #     first_date=datetime.datetime(2024, 1, 1),
    #     last_date=datetime.datetime(2024, 12, 31),
    # )

    # time_picker = ft.TimePicker(
    #     confirm_text="Confirmar",
    #     cancel_text="Regresar",
    #     error_invalid_text="Time out of range",
    #     help_text="Pick your time slot",
    #     on_change=lambda _: change_time(_, time_picker=time_picker,
    #                                     date_picker=date_picker),
    #     on_dismiss=lambda _: date_picker.pick_date(),
    # )

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

    page.add(log_out, principal)


if __name__ == "__main__":
    ft.app(target=operator)
