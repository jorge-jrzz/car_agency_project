import flet as ft


def main(page):
    page.title = "Card Example"

    carta = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.ALBUM),
                        title=ft.Text("The Enchanted Nightingale"),
                        subtitle=ft.Text(
                            "Music by Julie Gable. Lyrics by Sidney Stein."
                        ),
                    ),
                    ft.Row(
                        [ft.TextButton("Buy tickets"),
                         ft.TextButton("Listen")],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ),
            width=400,
            padding=10,
        )
    )
    page.add(
        ft.ResponsiveRow(
            controls=[
                ft.Container(
                    carta,
                    col={"sm": 6, "md": 4, "xl": 2},
                ),
                ft.Container(
                    carta,
                    col={"sm": 6, "md": 4, "xl": 2},
                ),
                ft.Container(
                    carta,
                    col={"sm": 6, "md": 4, "xl": 2},
                ),
                ft.Container(
                    carta,
                    col={"sm": 6, "md": 4, "xl": 2},
                )
            ]
        )
    )


ft.app(target=main)
