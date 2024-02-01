import flet as ft


def sesion(e):
    user = form.content.controls[0].value
    password = form.content.controls[1].value
    print(f"User: {user}, Password: {password}")


title = ft.Container(
    content=ft.Text("Inicio de sesión",
                    theme_style=ft.TextThemeStyle.TITLE_LARGE, size=28),
    alignment=ft.Alignment(0, 0)
)

buttom_submit = ft.Container(
    content=ft.ElevatedButton(
        text="Iniciar sesión", width=220, height=35, color="black", on_click=sesion),
    alignment=ft.Alignment(0, 0),
)

new_user = ft.Container(
    ft.Text("Crea una cuenta"),
    alignment=ft.Alignment(0, 0),
    padding=ft.padding.only(top=45),
)

form = ft.Container(
    content=ft.Column(
        controls=[
            ft.TextField(label="Username o Email",
                         icon=ft.icons.PERSON_ROUNDED),
            ft.TextField(label="Password", password=True,
                         can_reveal_password=True, icon=ft.icons.PASSWORD_ROUNDED),
            buttom_submit,
            new_user
        ],
        spacing=30
    ),
    bgcolor="#E8EBF7",
    width=360,
    height=350,
    padding=ft.padding.all(25),
    border_radius=10,
)

sign_in = ft.Container(
    alignment=ft.Alignment(0, 0),
    content=ft.Column(
        controls=[
            title,
            form
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
)
