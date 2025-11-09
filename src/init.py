from src.core import BaseModel
from src.db import DBConnectionHandler
from src.models import *  # noqa: F401 F403


def initialize_database():
    db_handler = DBConnectionHandler()
    BaseModel.metadata.create_all(db_handler.engine)
