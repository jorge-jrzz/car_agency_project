import flet as ft
from pages.sign_in import sign_in
from pages.sign_up import sign_up
from pages.home_page_client import home_page_client, from_car, date_picker, time_picker, buttons_schedule
from pages.home_page_admin import home_page_admin, give_price, edit_price
from pages.home_page_secretary import home_page_secretary, give_status, edit_status


def main(page: ft.Page):
    page.title = "Proyecto final"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_full_screen = True

    def god(e):
        user = sign_in.content.controls[1].content.controls[0].value
        password = sign_in.content.controls[1].content.controls[1].value
        admin = sign_in.content.controls[1].content.controls[3].content.controls[1].value

        door_a = user == "admin" and password == "pass"
        door_s = user == "secretary" and password == "pass"

        if door_a and admin:
            page.clean()
            page.vertical_alignment = ft.MainAxisAlignment.NONE
            page.add(home_page_admin)
            page.update()
        elif door_s and admin:
            page.clean()
            page.vertical_alignment = ft.MainAxisAlignment.NONE
            page.add(home_page_secretary)
            page.update()
        elif door_a:
            page.clean()
            page.add(home_page_client)
            page.update()


# Carga la pagina para registrarse


    def register(e):
        page.clean()
        page.vertical_alignment = ft.MainAxisAlignment.NONE
        page.add(sign_up)
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
# La idea es que tambien se obtenga el ID del servicio/cita para guardar en la DB el precio de esa cita en especifico en esta función

    def confirm_price(e):
        give_price.open = False
        price = give_price.content.controls[1].value
        home_page_admin.content.controls[0].rows[0].cells[6].content.value = price
        print(price)
        page.update()

# Abre el dialogo para cambiar el estado del servicio (home page secretary)

    def open_give_status(e):
        page.dialog = give_status
        give_status.open = True
        page.update()

# Cierra el dialogo de cambio de status del servicio (home page secretary)

    def cancel_status(e):
        give_status.open = False
        page.update()

# Cierra y confirma el status del servicio (home page secretary)
# La idea es que tambien se obtenga el ID del servicio/cita para guardar en la DB el status de esa cita en especifico en esta función

    def confirm_status(e):
        give_status.open = False
        status = give_status.content.controls[1].value
        home_page_secretary.content.controls[0].rows[0].cells[7].content.value = status
        print(status)
        page.update()

# Interaccion con la aplicacion completa sin necesidad de la BD
    sign_in.content.controls[1].content.controls[2].content.on_click = god

# Cambio entre las paginas de registro e iniciar secion
    sign_in.content.controls[1].content.controls[4].content.on_click = register
    sign_up.content.controls[0].content.controls[0].on_click = identify

# Cambio entre el formulario de agregar un carro al usuario y egendar una cita para servicio (home page client)
    home_page_client.content.controls[0].on_change = add_car
    home_page_client.content.controls[0].leading.on_click = schedule_service

# Cerrar sesión (home page client)
    home_page_client.content.controls[3].content.on_click = identify

# Cerrar sesión (home page admin)
    home_page_admin.content.controls[1].content.on_click = identify

# Cerrar sesión (home page secretary)
    home_page_secretary.content.controls[1].content.on_click = identify

# Edicion de precio en la pagina del administrador
    edit_price.on_click = open_give_price
    give_price.actions[0].on_click = cancel_price
    give_price.actions[1].on_click = confirm_price

# Edición del status del servicio (home page secretary)
    edit_status.on_click = open_give_status
    give_status.actions[0].on_click = cancel_status
    give_status.actions[1].on_click = confirm_status

# Principal
    page.add(sign_in)
    page.overlay.append(date_picker)
    page.overlay.append(time_picker)

    # def page_resize(e):
    #     print("New page size:", page.window_width, page.window_height)

    # page.on_resize = page_resize


ft.app(target=main)
