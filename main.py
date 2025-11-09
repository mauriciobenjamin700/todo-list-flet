import flet as ft

from src import initialize_database, main_app

initialize_database()

ft.app(main_app)
