import flet as ft

log_out = ft.Container(
    content=ft.TextButton(text="Cerrar sesión", style=ft.ButtonStyle(
        color="black", bgcolor=None, overlay_color=ft.colors.RED_500)),
    alignment=ft.Alignment(1, -1),
    expand=True
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
                        ft.Text("$ 300,000.00")
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
                        ft.TextButton("Agendar"),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                ),
            ]
        ),
        width=400,
        padding=10,
    )
)


# edit_status = ft.IconButton(
#     icon=ft.icons.FREE_CANCELLATION_ROUNDED,
#     icon_color="orange",
#     icon_size=20,
#     tooltip="Cambiar el estado del servicio",
#     # on_click=open_give_status
# )


# give_status = ft.AlertDialog(
#     modal=True,
#     title=ft.Text("Estado del servicio"),
#     content=ft.Column(
#         controls=[
#             ft.Text("Modifica el estado del servicio"),
#             ft.Dropdown(
#                 label="Estado",
#                 hint_text="Selecciona el estado",
#                 options=[
#                     ft.dropdown.Option("Agendado"),
#                     ft.dropdown.Option("En proceso"),
#                     ft.dropdown.Option("Realizado"),
#                     ft.dropdown.Option("Pausado"),
#                     ft.dropdown.Option("Rembolso"),
#                 ],
#                 autofocus=True,
#             )
#         ],
#         height=100
#     ),
#     actions=[
#         ft.TextButton("Cancelar"),
#         ft.TextButton("Confirmar"),
#         # ft.TextButton("Cancelar", on_click=cancel_status),
#         # ft.TextButton("Confirmar", on_click=confirm_status),
#     ],
#     actions_alignment=ft.MainAxisAlignment.CENTER,
#     on_dismiss=lambda e: print("Modal dialog dismissed!"),
# )


# dates_secretary_table = ft.DataTable(
#     columns=[
#         ft.DataColumn(ft.Text("ID cita")),
#         ft.DataColumn(ft.Text("Cliente")),
#         ft.DataColumn(ft.Text("Correo electronico")),
#         ft.DataColumn(ft.Text("Automovil")),
#         ft.DataColumn(ft.Text("Problema")),
#         ft.DataColumn(ft.Text("Hora servicio")),
#         ft.DataColumn(ft.Text("Precio")),
#         ft.DataColumn(ft.Text("Estado")),
#         ft.DataColumn(ft.Text("Editar estado")),
#     ],
#     rows=[
#         ft.DataRow(
#             cells=[
#                 ft.DataCell(ft.Text("e324")),
#                 ft.DataCell(ft.Text("John Smith")),
#                 ft.DataCell(ft.Text("john12s@gmail.com")),
#                 ft.DataCell(ft.Text("Nissan Aveo")),
#                 ft.DataCell(ft.Text("Cambio de balatas")),
#                 ft.DataCell(ft.Text("11:18:00")),
#                 ft.DataCell(ft.Text("$3124")),
#                 ft.DataCell(ft.Text("-")),
#                 ft.DataCell(edit_status)
#             ],
#         )
#     ]
# )


# home_page_operator = ft.Container(
#     content=ft.Row(
#         controls=[
#             dates_secretary_table,
#             log_out
#         ]
#     )
# )
