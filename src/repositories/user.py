from sqlalchemy import select
from sqlalchemy.orm import Session


from src.core import BaseRepository
from src.models import UserModel


class UserRepository(BaseRepository[UserModel]):
    """
    Repository class for User model, extending BaseRepository.

    Provides database operations specific to User entities.

    Args:
        session (Session): SQLAlchemy session for database interactions.

    Methods:
        - add
        - get_by_email
        - list
        - update
        - delete
    """
    def __init__(self, session: Session):
        super().__init__(session, UserModel)

    def add(self, instance: UserModel) -> UserModel:
        """
        Add a new User instance to the database.

        Args:
            instance (UserModel): The User instance to add.

        Returns:
            UserModel: The added User instance.
        """

        existing_user = self.get_by_email(instance.email)

        if existing_user:
            raise ValueError(
                "Já existe um usuário com este email."
            )

        self.session.add(instance)
        self.session.commit()
        self.session.refresh(instance)
        return instance

    def get_by_email(self, email: str) -> UserModel | None:
        """
        Retrieve a User instance by its email.

        Args:
            email (str): The email of the user to retrieve.

        Returns:
            UserModel | None: The retrieved User instance or None if not found.
        """
        stmt = select(self.model).where(self.model.email == email)
        result = self.session.execute(stmt).scalar_one_or_none()
        return result
