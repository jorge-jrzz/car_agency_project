import flet as ft


def main(page: ft.Page):
    page.title = "Proyecto final"
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_center()
    # page.window_full_screen = True
    page.window_width = 1410

    # Abre el diaogo para agregar o modificar el precio de determinado servicio

    def open_give_status(e):
        page.dialog = give_status
        give_status.open = True
        page.update()


# Cierra el dialogo para ingresar el precio


    def cancel_status(e):
        give_status.open = False
        page.update()

# Cierra y confirma el precio del servicio

    def confirm_status(e):
        give_status.open = False
        status = give_status.content.controls[1].value
        home_page_secretary.content.controls[0].rows[0].cells[7].content.value = status
        # home_page_admin.content.controls[0].rows[0].cells[6].content.value = price
        print(status)
        page.update()

    log_out = ft.Container(
        content=ft.TextButton(text="Cerrar sesión", style=ft.ButtonStyle(
            color="black", bgcolor=None, overlay_color=ft.colors.RED_500)),
        alignment=ft.Alignment(1, -1),
        expand=True
    )

    edit_status = ft.IconButton(
        icon=ft.icons.FREE_CANCELLATION_ROUNDED,
        icon_color="orange",
        icon_size=20,
        tooltip="Cambiar el estado del servicio",
        on_click=open_give_status
    )

    give_status = ft.AlertDialog(
        modal=True,
        title=ft.Text("Estado del servicio"),
        content=ft.Column(
            controls=[
                ft.Text("Modifica el estado del servicio"),
                ft.Dropdown(
                    label="Estado",
                    hint_text="Selecciona el estado",
                    options=[
                        ft.dropdown.Option("Agendado"),
                        ft.dropdown.Option("En proceso"),
                        ft.dropdown.Option("Realizado"),
                        ft.dropdown.Option("Pausado"),
                        ft.dropdown.Option("Rembolso"),
                    ],
                    autofocus=True,
                )
            ],
            height=100
        ),
        actions=[
            ft.TextButton("Cancelar", on_click=cancel_status),
            ft.TextButton("Confirmar", on_click=confirm_status),
        ],
        actions_alignment=ft.MainAxisAlignment.CENTER,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    dates_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID cita")),
            ft.DataColumn(ft.Text("Cliente")),
            ft.DataColumn(ft.Text("Correo electronico")),
            ft.DataColumn(ft.Text("Automovil")),
            ft.DataColumn(ft.Text("Problema")),
            ft.DataColumn(ft.Text("Hora servicio")),
            ft.DataColumn(ft.Text("Precio")),
            ft.DataColumn(ft.Text("Estado")),
            ft.DataColumn(ft.Text("Editar estado")),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("e324")),
                    ft.DataCell(ft.Text("John Smith")),
                    ft.DataCell(ft.Text("john12s@gmail.com")),
                    ft.DataCell(ft.Text("Nissan Aveo")),
                    ft.DataCell(ft.Text("Cambio de balatas")),
                    ft.DataCell(ft.Text("11:18:00")),
                    ft.DataCell(ft.Text("$3124")),
                    ft.DataCell(ft.Text("-")),
                    ft.DataCell(edit_status)
                ],
            )
        ]
    )

    home_page_secretary = ft.Container(
        content=ft.Row(
            controls=[
                dates_table,
                log_out
            ]
        )
    )

    page.add(home_page_secretary)

    # def page_resize(e):
    #     print("New page size:", page.window_width, page.window_height)

    # page.on_resize = page_resize


ft.app(target=main)
