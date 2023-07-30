import flet as ft
from flet import *


def main(page: ft.Page):
    page.window_width = 400
    page.window_height = 760
    BG = '#041955'
    FG = '#3450a1'

    content_1 = Container(
        content=Column(
            controls=[
                Row(alignment='spaceBetween',
                    controls=[
                        Container(
                            content=Icon(
                                icons.MENU)),
                        Row(
                            controls=[
                                Icon(icons.SEARCH),
                                Icon(icons.NOTIFICATIONS_OUTLINED)
                            ]
                        )
                    ]
                    )

            ]
        )
    )

    page_1 = Container()
    page_2 = Row(
        controls=[
            Container(
                width=360,
                height=700,
                bgcolor=FG,
                border_radius=35,
                padding=padding.only(
                    top=50, left=20,
                    right=20, bottom=5
                ),
                content=Column(
                    controls=[
                        content_1
                    ]
                )
            )
        ]
    )

    container = Container(
        width=360,
        height=700,
        bgcolor=BG,
        border_radius=35,
        content=Stack(
            controls=[
                page_1,
                page_2
            ]
        )
    )
    page.add(container)


ft.app(target=main)
