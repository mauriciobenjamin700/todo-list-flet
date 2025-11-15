import flet as ft
from logging import Logger
from pydantic import ValidationError
from time import sleep

from src.components import (
    Button,
    CenterContainer,
    VerticalContainer,
    TextButton,
    Input
)
from src.controllers import UserController
from src.core import constants
from src.schemas import LoginSchema


LOGGER = Logger(__name__, level="INFO")


def main(page: ft.Page):
    controller = UserController()

    page.title = "Login"

    email_input = Input(
        label="E-mail",
    )
    password_input = Input(
        label="Senha",
        password=True,
    )
    message = ft.Text("", color=ft.Colors.RED_300)

    def login_click(e):
        try:
            login_data = LoginSchema(
                email=email_input.value, password=password_input.value
            )
            user = controller.login(login_data)
            message.value = f"Bem vindo(a), {user.name}!"
            message.color = ft.Colors.GREEN_300
            message.update()
            sleep(2)
            page.go(constants.HOME_PAGE)

        except ValidationError as ve:
            message.value = "Parece que tem algo de errado com seu e-mail"
            message.color = ft.Colors.RED_300
            LOGGER.error(f"Validation error during login: {ve}")

        except Exception as ex:
            message.value = str(ex)
            message.color = ft.Colors.RED_300
        message.update()

    login_button = Button(
        text="Entrar",
        on_click=login_click,
    )

    create_account_button = TextButton(
        text="Não tem conta ainda? Crie uma agora!",
        on_click=lambda e: page.go(constants.REGISTER_PAGE),
    )

    page.add(
        CenterContainer(
            VerticalContainer(
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
                ),
            ),
        )
    page.update()
