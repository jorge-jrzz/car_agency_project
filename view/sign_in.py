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

operator_or_management = ft.Container(
    content=ft.Row(
        controls=[
            ft.Text("Operador", weight=ft.FontWeight.W_600),
            ft.Switch(value=False,
                      active_color="#CCCCCC",
                      thumb_color={
                          ft.MaterialState.SELECTED: ft.colors.WHITE,
                          ft.MaterialState.DEFAULT: ft.colors.BLACK,
                      },
                      thumb_icon={
                          ft.MaterialState.SELECTED: ft.icons.LOCK_PERSON,
                          ft.MaterialState.DEFAULT: ft.icons.CONTACT_PHONE
                      },
                      #   on_change=change_from
                      ),
            ft.Text("Gestión", weight=ft.FontWeight.W_600)
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )
)


manager_or_admin = ft.Container(
    content=ft.Row(
        controls=[
            ft.Text("Gerente", weight=ft.FontWeight.W_600),
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

buttom_submit = ft.Container(
    content=ft.ElevatedButton(
        # text="Iniciar sesión", width=220, height=35, color="black", on_click=sesion),
        text="Iniciar sesión", width=220, height=35, color="black"),
    alignment=ft.Alignment(0, 0),
)

new_user = ft.Container(
    ft.TextButton(text="Crea una cuenta", style=ft.ButtonStyle(
        color="black", bgcolor=None, overlay_color="#C0BEC6")),
    alignment=ft.Alignment(0, 0),
)

form1 = ft.Container(
    content=ft.Column(
        controls=[
            operator_or_management,
            ft.TextField(label="Username o Email",
                         icon=ft.icons.PERSON_ROUNDED),
            ft.TextField(label="Password ola", password=True,
                         can_reveal_password=True, icon=ft.icons.PASSWORD_ROUNDED),
            buttom_submit,
            new_user
        ],
        spacing=30
    ),
    bgcolor="#DBDFE6",
    width=360,
    height=370,
    padding=ft.padding.all(25),
    border_radius=10,
)

form2 = ft.Container(
    content=ft.Column(
        controls=[
            operator_or_management,
            ft.TextField(label="Username o Email",
                         icon=ft.icons.PERSON_ROUNDED),
            ft.TextField(label="Password ola", password=True,
                         can_reveal_password=True, icon=ft.icons.PASSWORD_ROUNDED),
            manager_or_admin,
            buttom_submit,
            new_user
        ],
        spacing=30
    ),
    bgcolor="#DBDFE6",
    width=360,
    height=450,
    padding=ft.padding.all(25),
    border_radius=10,
)

form = form1

sign_in = ft.Container(
    alignment=ft.Alignment(0, 0),
    content=ft.Column(
        controls=[
            title,
            form1
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
)
