import flet as ft
from src.schemas import UserCreateSchema
from src.controllers import UserController


def main(page: ft.Page):
    controller = UserController()

    name = ft.TextField(label="Nome", width=350)
    email = ft.TextField(label="E-mail", width=350)
    password = ft.TextField(
        label="Senha",
        width=350,
        password=True,
        can_reveal_password=True
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
        ft.Column(
            [
                name, email, password,
                ft.ElevatedButton(text="Criar conta", on_click=submit),
                ft.TextButton(
                    text="Voltar",
                    on_click=lambda e: page.go("/login")
                ),
                message
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    page.update()
