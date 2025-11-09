import flet as ft

from src.components import Button, TextButton, Input
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
        data = UserCreateSchema(
            name=name.value,
            email=email.value,
            password=password.value
        )
        try:
            controller.add(data)
            message.value = "Conta criada com sucesso!"
            page.go("/login")
        except Exception as ex:
            message.value = str(ex)
        message.update()

    page.add(
        ft.Container(
            ft.Column(
                [
                    name, email, password,
                    Button(text="Criar conta", on_click=submit),
                    TextButton(
                        text="Voltar",
                        on_click=lambda e: page.go("/login")
                    ),
                    message
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            expand=True,
            bgcolor=ft.Colors.BLACK54,
            alignment=ft.alignment.center,
        ),


    )
    page.update()
