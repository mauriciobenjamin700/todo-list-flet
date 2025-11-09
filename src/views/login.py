import flet as ft

from src.controllers import UserController
from src.schemas import LoginSchema


def main(page: ft.Page):
    controller = UserController()

    page.title = "Login"

    email_input = ft.TextField(
        label="E-mail",
        width=350,
        bgcolor=ft.Colors.WHITE,
        border=ft.border.all(1, ft.Colors.BLACK26),
        color=ft.Colors.BLACK,

    )
    password_input = ft.TextField(
        label="Senha",
        width=350,
        bgcolor=ft.Colors.WHITE,
        border=ft.border.all(1, ft.Colors.BLACK26),
        color=ft.Colors.BLACK,
        password=True, can_reveal_password=True
    )
    message = ft.Text("", color=ft.Colors.RED_300)

    def login_click(e):
        login_data = LoginSchema(
            email=email_input.value, password=password_input.value
        )
        try:
            user = controller.login(login_data)
            message.value = f"Bem vindo(a), {user.name}!"
            message.color = ft.Colors.GREEN_300
        except Exception as ex:
            message.value = str(ex)
            message.color = ft.Colors.RED_300
        message.update()

    login_button = ft.ElevatedButton(
        text="Entrar",
        on_click=login_click,
        width=350,
        bgcolor=ft.Colors.BLUE_700,
        color=ft.Colors.WHITE,
    )

    create_account_button = ft.TextButton(
        text="Não tem conta ainda? Crie uma agora!",
        on_click=lambda e: page.go("/register"),
        width=350,
    )

    page.add(
        ft.Container(
            ft.Container(
                ft.Column(
                    [
                        ft.Container(
                            email_input,
                            margin=ft.margin.only(bottom=10),
                        ),
                        ft.Container(
                            password_input,
                            margin=ft.margin.only(bottom=10),
                        ),
                        ft.Container(
                            login_button,
                            margin=ft.margin.only(bottom=10),
                        ),
                        ft.Container(
                            message,
                            margin=ft.margin.only(bottom=10),
                        ),
                        ft.Container(
                            create_account_button,
                            margin=ft.margin.only(bottom=10),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                alignment=ft.alignment.center,
                # bgcolor=ft.Colors.BLUE_GREY_50,
                # border=ft.border.all(1, ft.Colors.WHITE70),
                # padding=ft.padding.all(30),
                # border_radius=ft.border_radius.all(10),
            ),
            expand=True,
            alignment=ft.alignment.center,
            bgcolor=ft.Colors.BLACK54,
            # border=ft.border.all(1, ft.Colors.WHITE70)
        )
    )

    page.update()
