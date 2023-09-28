
from sqlmodel import SQLModel, create_engine


def get_engine():
    return create_engine("sqlite:///database.db")


def create_all():
    SQLModel.metadata.create_all(get_engine())
    