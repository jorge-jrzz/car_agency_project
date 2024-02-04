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
            ft.Text("Body")
        ]
    ),
    expand=True
)
