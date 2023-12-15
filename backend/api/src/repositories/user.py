from src.models import User
from src.utils.repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    """
    Класс репозитория для работы с таблицей пользователей.

    Attributes
    ----------
    model : User
        Модель таблицы пользователей, с которой будет работать репозиторий.

    Methods
    -------
    create_entity():
        Метод создания сущности пользователя в БД.
    read_one_entity():
        Метод получения одной сущности пользователя из БД.
    read_all_entities():
        Метод получения нескольких пользователей из БД.
    update_entity():
        Метод обновления пользователей в БД.
    delete_entities():
        Метод удаления пользователей из БД.
    """
    model = User
