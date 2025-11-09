from subprocess import run

from src import initialize_database


initialize_database()

run(["uv", "run", "flet", "run", "--web", "--port", "8080", "app.py"])
