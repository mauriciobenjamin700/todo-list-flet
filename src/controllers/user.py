from src.dependencies import get_user_service
from src.schemas import (
    LoginSchema,
    UserCreateSchema,
    UserResponseSchema,
    UserUpdateSchema
)
from src.services import UserService


class UserController:
    """
    Controller for user-related operations.

    Attributes:
        user_service (UserService): Service for user operations.

    Methods:
        - add
        - get
        - update
        - delete
        - login
    """
    def __init__(self, user_service: UserService = get_user_service()):
        self.user_service = user_service

    def add(self, data: UserCreateSchema) -> UserResponseSchema:
        return self.user_service.add(data)

    def get(self, user_id: int) -> UserResponseSchema:
        return self.user_service.get(user_id)

    def update(
        self, user_id: int, data: UserUpdateSchema
    ) -> UserResponseSchema:
        return self.user_service.update(user_id, data)

    def delete(self, user_id: int) -> None:
        self.user_service.delete(user_id)

    def login(self, data: LoginSchema) -> UserResponseSchema:
        return self.user_service.authenticate(data)
