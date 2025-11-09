import flet as ft

from src.controllers import UserController
from src.schemas import LoginSchema


def main(page: ft.Page):
    controller = UserController()

    page.title = "Login"

    email_input = ft.TextField(label="Email", width=300)
    password_input = ft.TextField(
        label="Password", width=300, password=True, can_reveal_password=True
    )
    message = ft.Text("", color=ft.Colors.RED_300)

    def login_click(e):
        login_data = LoginSchema(
            email=email_input.value, password=password_input.value
        )
        try:
            user = controller.login(login_data)
            message.value = f"Welcome, {user.name}!"
            message.color = ft.Colors.GREEN_300
        except Exception as ex:
            message.value = str(ex)
            message.color = ft.Colors.RED_300
        message.update()

    login_button = ft.ElevatedButton(
        text="Login", on_click=login_click
    )

    create_account_button = ft.TextButton(
        text="Create Account",
        on_click=lambda e: page.go("/register")
    )

    page.add(
        email_input,
        password_input,
        login_button,
        message,
        create_account_button,
    )

    page.update()


ft.app(main)
