import flet as ft
from pydantic import ValidationError

from src.components import (
    Button,
    TextButton,
    Input,
    CenterContainer,
    VerticalContainer
)
from src.schemas import UserCreateSchema
from src.controllers import UserController


def main(page: ft.Page):
    controller = UserController()

    name = Input(label="Nome")
    email = Input(label="E-mail")
    password = Input(
        label="Senha",
        password=True,
    )
    message = ft.Text("")

    def submit(e):
        try:
            data = UserCreateSchema(
                name=name.value,
                email=email.value,
                password=password.value
            )
            controller.add(data)
            message.value = "Conta criada com sucesso!"
            page.go("/login")
        except ValidationError:
            message.value = "Parece que tem algo de errado com seus dados"
            message.color = ft.Colors.RED_300
        except Exception as ex:
            message.value = str(ex)
            message.color = ft.Colors.RED_300
        message.update()

    page.add(
        CenterContainer(
            VerticalContainer(
                [
                    name, email, password,
                    Button(text="Criar conta", on_click=submit),
                    TextButton(
                        text="Voltar",
                        on_click=lambda e: page.go("/login")
                    ),
                    message
                ],
            ),
        ),


    )
    page.update()
