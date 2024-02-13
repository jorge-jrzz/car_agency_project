import flet as ft

# Primero, consulta la base de datos
# Esto es solo un ejemplo, reemplaza con tu propia lógica de consulta


resultados = [
    {
        'ref': '1',
        'nombre': 'Producto 1',
        'descripcion': 'Descripción del producto 1',
        'precio': '100',
    },
    {
        'ref': '2',
        'nombre': 'Producto 2',
        'descripcion': 'Descripción del producto 2',
        'precio': '200',
    },
    # Agrega más diccionarios aquí para más tarjetas
]


# Ahora, 'tarjetas' es una lista de tarjetas que puedes usar en tu aplicación


def main(page: ft.Page):

    # page.update()

    # Luego, crea una lista para almacenar las tarjetas
    tarjetas = []

    def change_color(e, item, llave):
        for container, tarjeta in enumerate(tarjetas):
            valor = tarjeta.content.content.content.controls[1].controls[0].value
            print(valor)
            # print(tarjeta.content.key)
            if tarjeta.content.key == llave and item == container and valor == "Atendido":
                tarjeta.content.color = "blue"
                tarjeta.update()
                break
            elif tarjeta.content.key == llave and item == container and valor == "Pendiente":
                tarjeta.content.color = "red"
                tarjeta.update()
                break

    def return_dropdown_status(item, llave):
        dropdown_status = ft.Dropdown(
            label="Estatus",
            options=[
                ft.dropdown.Option("Pendiente"),
                ft.dropdown.Option("Atendido"),
            ],
            width=200,
            on_change=lambda _: change_color(
                _, item, llave)
        )
        return dropdown_status

    # Itera sobre los resultados de la base de datos
    for item, resultado in enumerate(resultados):
        # Crea una tarjeta para cada resultado
        tarjeta = ft.Card(
            key=resultado['ref'],
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.CALENDAR_MONTH),
                            title=ft.Text(resultado['nombre']),
                            subtitle=ft.Column([
                                ft.Text(resultado['descripcion']),
                                ft.Text(resultado['precio']),
                            ])
                        ),
                        ft.Row(
                            controls=[
                                return_dropdown_status(
                                    item=item, llave=resultado['ref'])
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )
        # Añade la tarjeta a la lista
        tarjetas.append(ft.Container(tarjeta, col={"sm": 6, "md": 6, "xl": 4}))

    # print(resultados[1]['ref'])

    page.add(
        tarjetas[0],
        tarjetas[1]
    )


ft.app(target=main)
