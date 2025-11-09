import flet as ft
from src.views import login_view, register_view


def main(page: ft.Page):
    page.title = "Meu App"

    def route_change(e):
        # Limpa a página antes de carregar a nova view
        page.controls.clear()

        if page.route == "/" or page.route == "/login":
            login_view(page)
        elif page.route == "/register":
            register_view(page)
        else:
            page.add(ft.Text("Rota não encontrada"))

        page.update()

    page.on_route_change = route_change

    # inicia na rota atual ou na rota raiz
    if not page.route or page.route == "/":
        page.go("/login")
    else:
        page.go(page.route)
