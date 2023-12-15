from src.models import Photo
from src.utils.repository import SQLAlchemyRepository


class PhotoRepository(SQLAlchemyRepository):
    """
    Класс репозитория для работы с таблицей фотографий.

    Attributes
    ----------
    model : Photo
        Модель таблицы фотографий, с которой будет работать репозиторий.

    Methods
    -------
    create_entity():
        Метод создания сущности фотографии в БД.
    read_one_entity():
        Метод получения одной сущности фотографии из БД.
    read_all_entities():
        Метод получения нескольких фотографий из БД.
    update_entity():
        Метод обновления фотографий в БД.
    delete_entities():
        Метод удаления фотографий из БД.
    """
    model = Photo
