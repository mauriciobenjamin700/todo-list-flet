from typing import Callable
import flet as ft


class Button(ft.ElevatedButton):
    """
    A styled button with predefined width and colors.
    """
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
    """
    A styled text button with predefined width.
    """
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
