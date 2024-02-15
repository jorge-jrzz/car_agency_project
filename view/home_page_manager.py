import flet as ft


class State:
    toggle = True


s = State()

data = [3, 2, 5, 3.1, 4, 3, 4, 7, 7.8, 4, 10]


def average(datos):
    return sum(datos) / len(datos)


def manager(page: ft.Page):
    page.title = "Gerente"
    page.window_width = 1060
    page.window_height = 525
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_center()

    # Boton para cerrar sesion
    log_out = ft.ElevatedButton(
        "Cerrar sesión",
        icon=ft.icons.LOGOUT,
        color="red",
        on_click=lambda _: page.window_destroy()
    )

    data_1 = [
        ft.LineChartData(
            data_points=[
                ft.LineChartDataPoint(0, data[0]),
                ft.LineChartDataPoint(1.5, data[1]),
                ft.LineChartDataPoint(3, data[2]),
                ft.LineChartDataPoint(4.5, data[3]),
                ft.LineChartDataPoint(6, data[4]),
                ft.LineChartDataPoint(7.5, data[5]),
                ft.LineChartDataPoint(9, data[6]),
                ft.LineChartDataPoint(10.5, data[7]),
                ft.LineChartDataPoint(12, data[8]),
                ft.LineChartDataPoint(13.5, data[9]),
                ft.LineChartDataPoint(15, data[10]),
            ],
            stroke_width=5,
            color=ft.colors.CYAN,
            curved=True,
            stroke_cap_round=True,
        )
    ]

    data_2 = [
        ft.LineChartData(
            data_points=[
                ft.LineChartDataPoint(0, average(data)),
                ft.LineChartDataPoint(1.5, average(data)),
                ft.LineChartDataPoint(3, average(data)),
                ft.LineChartDataPoint(4.5, average(data)),
                ft.LineChartDataPoint(6, average(data)),
                ft.LineChartDataPoint(7.5, average(data)),
                ft.LineChartDataPoint(9, average(data)),
                ft.LineChartDataPoint(10.5, average(data)),
                ft.LineChartDataPoint(12, average(data)),
                ft.LineChartDataPoint(13.5, average(data)),
                ft.LineChartDataPoint(15, average(data))
            ],
            stroke_width=5,
            color=ft.colors.CYAN,
            curved=True,
            stroke_cap_round=True,
        )
    ]

    chart = ft.LineChart(
        data_series=data_1,
        border=ft.border.all(3, ft.colors.with_opacity(
            0.2, ft.colors.ON_SURFACE)),
        horizontal_grid_lines=ft.ChartGridLines(
            interval=1, color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE), width=1
        ),
        vertical_grid_lines=ft.ChartGridLines(
            interval=1, color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE), width=1
        ),
        left_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=0,
                    label=ft.Text("$0K", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=2,
                    label=ft.Text("$10K", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=4,
                    label=ft.Text("$20K", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=6,
                    label=ft.Text("$30K", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=8,
                    label=ft.Text("$40K", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=10,
                    label=ft.Text("$50K", size=14, weight=ft.FontWeight.BOLD),
                )

            ],
            labels_size=50,
        ),
        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=0,
                    label=ft.Container(
                        ft.Text(
                            "ENE",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.with_opacity(
                                0.5, ft.colors.ON_SURFACE),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
                ft.ChartAxisLabel(
                    value=3,
                    label=ft.Container(
                        ft.Text(
                            "FEB",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.with_opacity(
                                0.5, ft.colors.ON_SURFACE),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
                ft.ChartAxisLabel(
                    value=6,
                    label=ft.Container(
                        ft.Text(
                            "MAR",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.with_opacity(
                                0.5, ft.colors.ON_SURFACE),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
                ft.ChartAxisLabel(
                    value=9,
                    label=ft.Container(
                        ft.Text(
                            "ABR",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.with_opacity(
                                0.5, ft.colors.ON_SURFACE),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
                ft.ChartAxisLabel(
                    value=12,
                    label=ft.Container(
                        ft.Text(
                            "MAY",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.with_opacity(
                                0.5, ft.colors.ON_SURFACE),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
                ft.ChartAxisLabel(
                    value=15,
                    label=ft.Container(
                        ft.Text(
                            "JUN",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.with_opacity(
                                0.5, ft.colors.ON_SURFACE),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
            ],
            labels_size=32,
        ),
        tooltip_bgcolor=ft.colors.with_opacity(0.8, ft.colors.BLUE_GREY),
        min_y=0,
        max_y=10,
        min_x=0,
        max_x=15,
        # animate=5000,
        expand=True,
    )

    container_ventas = ft.Container(chart, padding=ft.padding.all(20))

    def toggle_data(e, chart):
        if s.toggle:
            chart.data_series = data_2
            chart.interactive = False
        else:
            chart.data_series = data_1
            chart.interactive = True
        s.toggle = not s.toggle
        chart.update()

    avg_button = ft.ElevatedButton(
        "Promedio", on_click=lambda _: toggle_data(_, chart))

    page.add(log_out, avg_button, container_ventas)


if __name__ == "__main__":
    ft.app(target=manager)
