# Car agency project for DSAGE

## Descripción

El objetivo de este proyecto es repasar, recapitular y poner en juego varios de los conocimientos y habilidades adquiridos durante el curso.
Se tiene que desarrollar un pequeño sistema (en Python o Java) que nos permita agendar citas para una agencia automotriz que realiza el servicio de mantenimiento a los autos que fueron adquiridos en la agencia. El servicio se realiza cada 10 mil kilómetros o cada 6 meses (lo que suceda primero) y se debe de recordar al cliente para que haga una la cita de servicio (para ello, el sistema debe de "saber", es decir, tener escrito en su base de datos, cuando fue la última cita).

## Requerimientos:

- [x] El sistema será una aplicación local (no en red, aunque se puede conectar a un servidor) y los actores que pueden acceder al sistema serán 10 secretarias (que son las que realizan las llamadas al cliente y ingresan los datos al sistema, turno matutino (de 8 a 15 horas) y vespertino (de 15 a 18 horas) de lunes a sábado y donde el sábado sólo se tiene turno matutino), un administrador y un gerente.

- [x] Use en general el patrón Modelo, Vista controlador.

- [x] Deberá tener un módulo de autenticación de usuarios que dan su nombre de usuario y contraseña para ingresar al sistema. En esta parte debes de realizar pruebas unitarias y mostrar los resultados de los assertions. Referencia donde se hacen pruebas al módulo de autenticación: PRUEBAS UNITARIAS en [JAVA (JUNIT 5)](https://www.youtube.com/watch?v=74sClDEYSQ4).

- [x] Deberá de tener acceso a un objeto tipo Calendario (podrás usar Google-calendar, explicando como conectaste el plug-in de este producto). Este objeto debe de tener un método que llama y despliega una interfaz gráfica del calendario para realizar el apartado de la cita. Las citas deberán de escribirse en una base de datos.

- [ ] Las citas se pueden de dar de alta o cancelar así como modificar y deberán tener la siguiente información (REQUISITOS DE INFORMACIÓN): clave del vehículo, nombre del propietario del vehículo, teléfono, marca (ejemplo Toyota), modelo (ejemplo: Yaris) año, color y si es híbrido, a gasolina o eléctrico, fecha, hora y costo.

- [x] Todas la actividad de citas deberá de tener un log (archivo histórico de movimientos o data base log) que nos escribe el fecha, la hora y el movimiento realizado (ALTA, CANCELACION O MODIFICACIÓN DE CITA), clave del vehículo, marca, modelo y quien fue la secretaria (o persona con acceso al sistema) que lo realizó. Este log debe ser totalmente independiente del archivo de citas y de preferencia deberá de ser escrito en otro disco o en un servidor remoto.

- [x] Se deberá de contar con objetos tipo Robot-calendar que verifican las citas que tendrán que ser programas para esta semana: el Robot-calendar revisa las citas realizadas hace seis meses (en la semana ocurrida hace seis meses) y las separa en un archivo con todos sus datos: tipo de auto, clave del vehículo etc. Tan pronto como el operario (o secretaria) ingresa al sistema, el sistema usando el controlador y un robot- calendar informa en una ventana pop-up (de despliegue repentino, en español) cuales son las citas que el robot encontró que deberían ser programadas esta semana el teléfono y nombre del cliente para que el operario (o secretaria llame al cliente y se agende la cita).

- [x] Use al menos tres patrones de diseño distintos (como singleton, factory, prototype por poner un ejemplo) en su desarrollo y explique donde fueron usados y porque. Se recomienda al menos usar 3 pero puede usar más patrones si lo considera necesario.

- [x] Haga varias pruebas unitarias para verificar que los módulos de altas, cambios y cancelación de citas funciona bien.

- [x] Para hacer las pruebas sobre la base ¿que debemos de hacer? ¿simular datos? o usar HashMap ¿podría ser un recurso útil? ¿ esto es cierto? explique.

- [x] El sistema debe de permitir hacer un concentrado de cuantos clientes tuvimos esta semana y poder desplegar estas estadísticas. Esto es muy útil para hacer una especie de ley de conservación: si hace seis meses tuve 52 clientes esta semana debo de tener al menos 52 clientes o al menos algo muy aproximado (normalmente tengo cada vez más porque se adquieren cada vez más autos).

- [ ] Simula al caso de los clientes que cada 3 meses tienen un recorrido de 10 mil kilómetros y requieren servicio (estos los puedes detectar al principio sólo si el cliente te lo notifica).

- [x] Escribe un manual de usuario de tu sistema y haz un algunos diagramas UML que ilustren los pormenores del sistema. Especifica que Arquitectura utilizaste y que patrones de diseño.

## Screenshots

![login](/screenshots/login.png)
![operator_page](/screenshots/operator_page.png)
![manager_page](/screenshots/manager_page.png)
![admin_page](/screenshots/admin_page.png)

## Autors

- [Jorge Juarez](https://github.com/jorge-jrzz)
- [Eduardo Gonzales](https://github.com/EduardoGog)
