import flet as ft


def main(page: ft.Page):
    page.title = "Home View"
    page.add(ft.Text("Welcome to the Home View!"))

    filters = ft.Text("This is where filters would go.")
    page.add(filters)

    todo_list = ft.Text("This is where the to-do list would be displayed.")
    page.add(todo_list)

    add_todo = ft.Text("This is where you can add new to-do items.")
    page.add(add_todo)
    page.update()
