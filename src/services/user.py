from src.models import UserModel
from src.repositories import UserRepository
from src.schemas import (
    LoginSchema,
    TokenDataSchema,
    TokenSchema,
    UserCreateSchema,
    UserDBSchema,
    UserUpdateSchema,
    UserResponseSchema,
)
from src.utils import PasswordHasher, TokenHandler


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def add(self, data: UserCreateSchema) -> UserResponseSchema:
        """
        Create a new user in the system.

        Args:
            data (UserCreateSchema): The data for the new user.

        Returns:
            UserResponseSchema: The created user's data.
        """
        model = UserModel(
            **data.model_dump(exclude_unset=True, exclude_none=True)
        )
        model.password = PasswordHasher.hash_password(data.password)
        created_user = self.user_repository.add(model)
        return self.map_to_response(created_user)

    def get(self, user_id: int) -> UserResponseSchema:
        """
        Retrieve a user by their ID.

        Args:
            user_id (int): The ID of the user to retrieve.

        Returns:
            UserResponseSchema | None: The user's data if found, else None.
        """
        user = self.user_repository.get(user_id)
        if user is None:
            raise ValueError("User not found")

        return self.map_to_response(user)

    def list(self) -> list[UserResponseSchema]:
        """
        Retrieve all users in the system.

        Returns:
            list[UserResponseSchema]: A list of all users' data.
        """
        users = self.user_repository.list()
        return [self.map_to_response(user) for user in users]

    def update(
        self,
        user_id: int,
        data: UserUpdateSchema
    ) -> UserResponseSchema:
        """
        Update an existing user's information.

        Args:
            user_id (int): The ID of the user to update.
            data (UserUpdateSchema): The updated user data.

        Returns:
            UserResponseSchema: The updated user's data.
        """
        user = self.user_repository.get(user_id)
        if user is None:
            raise ValueError("User not found")

        for field, value in data.model_dump(
            exclude_unset=True,
            exclude_none=True
        ).items():
            if hasattr(user, field):
                if field == "password":
                    value = PasswordHasher.hash_password(value)
                    setattr(user, field, value)
                elif field == "email":
                    user_with_email = self.user_repository.get_by_email(value)
                    if user_with_email and user_with_email.id != user_id:
                        raise ValueError("Email already in use")
                    setattr(user, field, value)
                else:
                    setattr(user, field, value)

        updated_user = self.user_repository.update(user)
        return self.map_to_response(updated_user)

    def delete(self, user_id: int) -> None:
        """
        Delete a user from the system.

        Args:
            user_id (int): The ID of the user to delete.
        """
        user = self.user_repository.get(user_id)
        if user is None:
            raise ValueError("User not found")

        self.user_repository.delete(user)

    def authenticate(
        self,
        data: LoginSchema | TokenDataSchema
    ) -> UserResponseSchema:
        """
        Authenticate a user using either login credentials or token data.

        Args:
            data (LoginSchema | TokenDataSchema): The login credentials or
            token data.

        Returns:
            UserResponseSchema: The authenticated user's data.
        """
        if isinstance(data, TokenDataSchema):
            user = self.user_repository.get(data.user_id)
            if user is None:
                raise ValueError("User not found")
            return self.map_to_response(user)
        else:
            user = self.user_repository.get_by_email(data.email)
            if user is None:
                raise ValueError("Invalid email or password")

            if not PasswordHasher.verify_password(
                data.password,
                user.password
            ):
                raise ValueError("Invalid email or password")

            return self.map_to_response(user)

    def generate_token(self, user: UserModel) -> TokenSchema:
        """
        Generate a JWT token for the authenticated user.

        Args:
            user (UserModel): The authenticated user.
        Returns:
            TokenSchema: The generated JWT token.
        """
        token_data = {"user_id": user.id}
        token = TokenHandler.create_access_token(data=token_data)
        return TokenSchema(
            access_token=token,
            token_type="bearer"
        )

    def decode_token(self, token: str) -> TokenDataSchema:
        """
        Decode and verify a JWT token.

        Args:
            token (str): The JWT token to decode.
        Returns:
            TokenDataSchema: The decoded token data.
        Raises:
            ValueError: If the token is invalid or expired.
        """
        payload = TokenHandler.verify_token(token)
        token_data = TokenDataSchema.model_validate(payload)
        return token_data

    def map_to_response(self, user: UserModel) -> UserResponseSchema:
        """
        Map a UserModel instance to a UserResponseSchema.

        Args:
            user (UserModel): The user model instance.

        Returns:
            UserResponseSchema: The mapped user response schema.
        """
        db_schema = UserDBSchema.model_validate(user)
        return UserResponseSchema.model_validate(db_schema)
