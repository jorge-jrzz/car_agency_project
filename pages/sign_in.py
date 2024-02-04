import flet as ft


login = {"user": "", "password": ""}
admin = False


def sesion(e):

    global login
    global admin

    user = form.content.controls[0].value
    password = form.content.controls[1].value
    admin = form.content.controls[3].content.controls[1].value

    if user != "" and password != "":
        login["user"] = user
        login["password"] = password
        print(login)
        print(admin)


title = ft.Container(
    content=ft.Text("Inicio de sesión",
                    theme_style=ft.TextThemeStyle.TITLE_LARGE, size=28),
    alignment=ft.Alignment(0, 0)
)

buttom_submit = ft.Container(
    content=ft.ElevatedButton(
        # text="Iniciar sesión", width=220, height=35, color="black", on_click=sesion),
        text="Iniciar sesión", width=220, height=35, color="black"),
    alignment=ft.Alignment(0, 0),
)

client_or_admin = ft.Container(
    content=ft.Row(
        controls=[
            ft.Text("Cliente", weight=ft.FontWeight.W_600),
            ft.Switch(value=False,
                      active_color="#CCCCCC",
                      thumb_color={
                          ft.MaterialState.SELECTED: ft.colors.WHITE,
                          ft.MaterialState.DEFAULT: ft.colors.BLACK,
                      },
                      thumb_icon={
                          ft.MaterialState.SELECTED: ft.icons.ADMIN_PANEL_SETTINGS,
                          ft.MaterialState.DEFAULT: ft.icons.PERSON
                      }
                      ),
            ft.Text("Admin", weight=ft.FontWeight.W_600)
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )
)

new_user = ft.Container(
    ft.Text("Crea una cuenta", weight=ft.FontWeight.BOLD),
    alignment=ft.Alignment(0, 0),
)

form = ft.Container(
    content=ft.Column(
        controls=[
            ft.TextField(label="Username o Email",
                         icon=ft.icons.PERSON_ROUNDED),
            ft.TextField(label="Password", password=True,
                         can_reveal_password=True, icon=ft.icons.PASSWORD_ROUNDED),
            buttom_submit,
            client_or_admin,
            new_user
        ],
        spacing=30
    ),
    bgcolor="#97D8C4",
    width=360,
    height=370,
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
