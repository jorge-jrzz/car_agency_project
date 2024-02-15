import flet as ft

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
        text="Iniciar sesión", width=220, height=35, color="black"),
    alignment=ft.Alignment(0, 0),
)


def change_from(e, page):
    operator = sign_in.content.controls[1].content.controls[0].content.controls[1].value
    if operator is True:
        sign_in.content.controls[1] = form2
    else:
        sign_in.content.controls[1] = form1
    page.update()


form1 = ft.Container(
    content=ft.Column(
        controls=[
            operator_or_management,
            ft.TextField(label="Username o Email",
                         icon=ft.icons.PERSON_ROUNDED),
            ft.TextField(label="Password", password=True,
                         can_reveal_password=True, icon=ft.icons.PASSWORD_ROUNDED),
            buttom_submit,
        ],
        spacing=30
    ),
    bgcolor="#DBDFE6",
    width=360,
    height=350,
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
        ],
        spacing=30
    ),
    bgcolor="#DBDFE6",
    width=360,
    height=400,
    padding=ft.padding.all(25),
    border_radius=10,
)

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
