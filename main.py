import flet as ft

from src import initialize_database
from src.views import login_view

initialize_database()

ft.app(login_view)
