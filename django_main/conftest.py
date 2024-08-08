import pytest
from django.contrib.auth.models import User


@pytest.fixture
def new_user_factory(db):
    def create_app_user(
            username: str,
            password: str = None,
            email: str = "test@com",
            is_superuser: bool = False
    ):
        user = User.ojects.create(
            username=username,
            password=password,
            email=email,
            is_superuser=is_superuser
        )
        return user
    return create_app_user


@pytest.fixture
def user_one(db, new_user_factory):
    return new_user_factory("Test", "Pass", "email")
