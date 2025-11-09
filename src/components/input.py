import flet as ft


class Input(ft.TextField):
    def __init__(self, label: str, password: bool = False):
        super().__init__(
            label=label,
            width=350,
            bgcolor=ft.Colors.WHITE,
            border=ft.border.all(1, ft.Colors.BLACK26),
            color=ft.Colors.BLACK,
            password=password,
            can_reveal_password=password
        )
