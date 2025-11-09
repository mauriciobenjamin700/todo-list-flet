from src.repositories import UserRepository
from src.services import UserService

from .db import db


def get_user_service():

    for session in db.get_session():

        return UserService(
            user_repository=UserRepository(
                session=session
            )
        )