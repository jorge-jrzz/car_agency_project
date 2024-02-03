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
    on_change=lambda e: print("Selected destination:",
                              e.control.selected_index),
)


add_car = ft.Container(
    content=ft.Column(
        controls=[

        ]
    )
)


main_content = ft.Container(
    content=ft.Row(
        controls=[
            rail,
            ft.VerticalDivider(width=1),
            ft.Column([ft.Text("Body!")],
                      alignment=ft.MainAxisAlignment.START),
        ]
    ),
    expand=True
)
