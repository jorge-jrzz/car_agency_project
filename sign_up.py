import flet as ft


title = ft.Container(
    content=ft.Text(
        "Registro", theme_style=ft.TextThemeStyle.TITLE_LARGE, size=28),
    alignment=ft.Alignment(0, 0)
)

buttom_submit = ft.Container(
    content=ft.ElevatedButton(
        text="Guardar", width=220, height=35, color="black"),
    alignment=ft.Alignment(0, 0),
    padding=ft.padding.only(top=7)

)

form = ft.Container(
    content=ft.Column(
        controls=[
            ft.TextField(label="Nombre"),
            # ft.TextField(label="Apellido paterno"),
            # ft.TextField(label="Apellido materno"),
            ft.TextField(label="Email", suffix_text="@gmail.com"),
            ft.TextField(label="Nombre de usuario", prefix_text="@"),
            ft.TextField(label="Contraseña", hint_text="Ingresa la contraseña",
                         password=True, can_reveal_password=True),
            ft.TextField(label="Confirmar contraseña", hint_text="Ingresa de nuevo la contraseña",
                         password=True, can_reveal_password=True),
            buttom_submit
        ],
        spacing=15
    ),
    bgcolor="#E8EBF7",
    width=470,
    height=450,
    padding=ft.padding.all(20),
    border_radius=10
)

sign_up = ft.Container(
    content=ft.Column(
        controls=[
            title,
            form
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
)
