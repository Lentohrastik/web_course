from src.models import Template
from src.utils.repository import SQLAlchemyRepository


class TemplateRepository(SQLAlchemyRepository):
    """
    Класс репозитория для работы с таблицей шаблонов титров.

    Attributes
    ----------
    model : Template
        Модель таблицы шаблонов титров, с которой будет работать репозиторий.

    Methods
    -------
    create_entity():
        Метод создания сущности титра в БД.
    read_one_entity():
        Метод получения одной сущности титра из БД.
    read_all_entities():
        Метод получения нескольких титров из БД.
    update_entity():
        Метод обновления титров в БД.
    delete_entities():
        Метод удаления титров из БД.
    """
    model = Template
