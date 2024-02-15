import flet as ft
from model.db import get_personal


def administrador(page: ft.Page):
    page.title = "Administrador"
    page.window_width = 815
    page.window_height = 700
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.ALWAYS

    personal = get_personal()

# Boton para cerrar sesion
    log_out = ft.ElevatedButton(
        "Cerrar sesión",
        icon=ft.icons.LOGOUT,
        color="red",
        on_click=lambda _: page.window_destroy()
    )

    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Username")),
            ft.DataColumn(ft.Text("Rol")),
            ft.DataColumn(ft.Text("Turno")),
            # ft.DataColumn(ft.Text("Dropdown")),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(row[0])),
                    ft.DataCell(ft.Text(str(row[1]))),
                    ft.DataCell(ft.Text(row[2])),
                    # ft.DataCell(ft.Dropdown(
                    #     options=dropdown_options, height=20)),
                ],
            ) for row in personal
        ],
        width=page.width  # Establecer el ancho de la tabla al ancho de la pantalla
    )

    page.add(log_out, tabla)


if __name__ == "__main__":
    ft.app(target=administrador)
