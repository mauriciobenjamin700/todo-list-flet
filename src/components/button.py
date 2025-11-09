from typing import Callable
import flet as ft


class Button(ft.ElevatedButton):
    def __init__(
        self,
        text: str,
        on_click: Callable,
        width: int = 350,
        bgcolor=ft.Colors.BLUE_700,
        color=ft.Colors.WHITE,
    ):
        super().__init__(
            text=text,
            on_click=on_click,
            width=width,
            bgcolor=bgcolor,
            color=color,
        )


class TextButton(ft.TextButton):
    def __init__(
        self,
        text: str,
        on_click: Callable,
        width: int = 350,
    ):
        super().__init__(
            text=text,
            on_click=on_click,
            width=width,
        )
