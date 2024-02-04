import flet as ft


def open_give_price(e):
    page.dialog = give_price
    give_price.open = True
    page.update()


def cancel_price(e):
    give_price.open = False
    page.update()


def confirm_price(e):
    give_price.open = False
    price = give_price.content.controls[1].value
    dates_table.rows[0].cells[6].content.value = price
    print(price)
    page.update()


edit_price = ft.IconButton(
    icon=ft.icons.EDIT_SQUARE,
    icon_color="green",
    icon_size=20,
    tooltip="Ingresa el precio del servicio",
    on_click=open_give_price
)

give_price = ft.AlertDialog(
    modal=True,
    title=ft.Text("Precio"),
    content=ft.Column(
        controls=[
            ft.Text("Ingresa el precio del servicio"),
            ft.TextField(label="money")
        ]
    ),
    actions=[
        ft.TextButton("Confirmar", on_click=confirm_price),
        ft.TextButton("Cancelar", on_click=cancel_price),
    ],
    actions_alignment=ft.MainAxisAlignment.END,
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
        ft.DataColumn(ft.Text("Editar precio")),
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
                ft.DataCell(ft.Text("-")),
                ft.DataCell(edit_price)
            ],
        )
    ]
)
