import flet as ft

from src.components import Header
from src.core import constants
from src.schemas import UserResponseSchema


def main(page: ft.Page):
    page.title = "Home View"

    user_data = page.client_storage.get(constants.USER_DATA)
    user = UserResponseSchema.model_validate(user_data)

    header = Header(
        title=f"Seja bem-vindo({user.name}) ao Todo List Flet",
        subtitle="Gerencie suas tarefas de forma simples e eficiente!",
        expand=True
    )

    page.add(header)

    filters = ft.Text("This is where filters would go.")
    page.add(filters)

    todo_list = ft.Text("This is where the to-do list would be displayed.")
    page.add(todo_list)

    add_todo = ft.Text("This is where you can add new to-do items.")
    page.add(add_todo)
    page.update()
