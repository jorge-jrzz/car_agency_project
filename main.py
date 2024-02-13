import flet as ft
from view.sign_in import sign_in, form1, form2
from view.home_page_manager import home_page_client, from_car, date_picker, time_picker, buttons_schedule
from view.home_page_admin import home_page_admin, give_price, edit_price
import view.home_page_operator as home_page_operator


def main(page: ft.Page):
    page.title = "Proyecto final"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    # page.window_full_screen = True

    operator = False

    def god(e):
        operator = sign_in.content.controls[1].content.controls[0].content.controls[1].value
        # form = True if form == "Operador" else False

        user = sign_in.content.controls[1].content.controls[1].value
        password = sign_in.content.controls[1].content.controls[2].value

        if operator is False:
            # type_user = sign_in.content.controls[1].content.controls[0].content.controls[1].value
            type_user = "Operador"
            print(type_user)
            print(user)
            print(password)
            if user == "admin" and password == "pass":
                page.clean()
                page.vertical_alignment = ft.MainAxisAlignment.START
                page.add(home_page_operator)
                page.update()
        else:
            type_user = "Gestión"
            type_user2 = sign_in.content.controls[1].content.controls[3].content.controls[1].value
            print(type_user)
            print(type_user2)
            print(user)
            print(password)

        # door_o = user == "admin" and password == "pass"
        # door_s = user == "secretary" and password == "pass"

        # if door_a and admin:
        #     page.clean()
        #     page.vertical_alignment = ft.MainAxisAlignment.NONE
        #     page.add(home_page_admin)
        #     page.update()
        # elif door_s and admin:
        #     page.clean()
        #     page.vertical_alignment = ft.MainAxisAlignment.NONE
        #     page.add(home_page_secretary)
        #     page.update()
        # elif door_a:
        #     page.clean()
        #     page.add(home_page_client)
        #     page.update()


# Cambia el formulario de inicio de sesion

    def change_from(e):
        operator = sign_in.content.controls[1].content.controls[0].content.controls[1].value
        if operator is True:
            sign_in.content.controls[1] = form2
        else:
            sign_in.content.controls[1] = form1
        page.update()


# Carga la pagina para iniciar sesion

    def identify(e):
        page.clean()
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.add(sign_in)
        page.update()


# Carga el formulario para registrar un nuevo carro del cliente (home page client)

    def add_car(e):
        home_page_client.content.controls[2] = from_car
        page.update()


# Carga el formulario para registrar una cita para servicio del carro (home page client)

    def schedule_service(e):
        home_page_client.content.controls[2] = buttons_schedule
        page.update()


# Abre el diaogo para agregar o modificar el precio de determinado servicio (home page admin)

    def open_give_price(e):
        page.dialog = give_price
        give_price.open = True
        page.update()


# Cierra el dialogo para ingresar el precio (home page admin)

    def cancel_price(e):
        give_price.open = False
        page.update()


# Cierra y confirma el precio del servicio (home page admin)

    def confirm_price(e):
        give_price.open = False
        price = give_price.content.controls[1].value
        home_page_admin.content.controls[0].rows[0].cells[6].content.value = price
        print(price)
        page.update()

# # Abre el dialogo para cambiar el estado del servicio (home page secretary)

#     def open_give_status(e):
#         page.dialog = give_status
#         give_status.open = True
#         page.update()

# # Cierra el dialogo de cambio de status del servicio (home page secretary)

#     def cancel_status(e):
#         give_status.open = False
#         page.update()

# # Cierra y confirma el status del servicio (home page secretary)

#     def confirm_status(e):
#         give_status.open = False
#         status = give_status.content.controls[1].value
#         home_page_operator.content.controls[0].rows[0].cells[7].content.value = status
#         print(status)
#         page.update()

# Interaccion con la aplicacion completa sin necesidad de la BD
    if operator is False:
        sign_in.content.controls[1].content.controls[3].content.on_click = god
    else:
        sign_in.content.controls[1].content.controls[4].content.on_click = god

# Cambio entre los formularios de inicio de sesion
    sign_in.content.controls[1].content.controls[0].content.controls[1].on_change = change_from


# Cambio entre el formulario de agregar un carro al usuario y egendar una cita para servicio (home page client)
    home_page_client.content.controls[0].on_change = add_car
    home_page_client.content.controls[0].leading.on_click = schedule_service

# Cerrar sesión (home page client)
    home_page_client.content.controls[3].content.on_click = identify

# Cerrar sesión (home page admin)
    home_page_admin.content.controls[1].content.on_click = identify

# Cerrar sesión (home page secretary)
    # home_page_operator.content.controls[1].content.on_click = identify

# Edicion de precio en la pagina del administrador
    edit_price.on_click = open_give_price
    give_price.actions[0].on_click = cancel_price
    give_price.actions[1].on_click = confirm_price

# # Edición del status del servicio (home page secretary)
#     edit_status.on_click = open_give_status
#     give_status.actions[0].on_click = cancel_status
#     give_status.actions[1].on_click = confirm_status

# Principal
    # page.add(sign_in)
    page.overlay.append(date_picker)
    page.overlay.append(time_picker)

    page.add(
        sign_in
        # ft.ResponsiveRow(
        #     controls=[
        #         home_page_operator.log_out,
        #         ft.Container(
        #             home_page_operator.carta,
        #             col={"sm": 6, "md": 6, "xl": 4},
        #         ),
        #         ft.Container(
        #             home_page_operator.carta,
        #             col={"sm": 6, "md": 6, "xl": 4},
        #         ),
        #         ft.Container(
        #             home_page_operator.carta,
        #             col={"sm": 6, "md": 6, "xl": 4},
        #         ),
        #         ft.Container(
        #             home_page_operator.carta,
        #             col={"sm": 6, "md": 6, "xl": 4},
        #         )
        #     ]
        # )
    )

    # def page_resize(e):
    #     print("New page size:", page.window_width, page.window_height)

    # page.on_resize = page_resize


ft.app(target=main)
