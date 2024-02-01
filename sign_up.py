import flet as ft


user_info = {"name": "", "email": "", "username": "",
             "password": "", "confirm_pass": ""}


def save_info(e):
    global user_info
    name = form.content.controls[0].value
    email = form.content.controls[1].value
    username = form.content.controls[2].value
    password = form.content.controls[3].value
    confirm_pass = form.content.controls[4].value
    if name != "" and email != "" and username != "" and password != "" and confirm_pass != "" and password == confirm_pass:
        user_info["name"] = name
        user_info["email"] = email
        user_info["username"] = username
        user_info["password"] = password
        user_info["confirm_pass"] = confirm_pass
        print(user_info)


back = ft.Container(
    content=ft.Row(
        controls=[
            ft.IconButton(
                icon=ft.icons.ARROW_BACK_IOS_NEW_ROUNDED, icon_color="black"),
            ft.Text("Iniciar sesión", weight=ft.FontWeight.BOLD, size=17)
        ]
    ),
    alignment=ft.Alignment(-1, -1)
)

title = ft.Container(
    content=ft.Text(
        "Registro", theme_style=ft.TextThemeStyle.TITLE_LARGE, size=28),
    alignment=ft.Alignment(0, 0)
)

buttom_submit = ft.Container(
    content=ft.ElevatedButton(
        text="Guardar", width=220, height=35, color="black", on_click=save_info),
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
    # height=570,
    padding=ft.padding.all(20),
    border_radius=10
)

sign_up = ft.Container(
    content=ft.Column(
        controls=[
            back,
            title,
            form
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
)
