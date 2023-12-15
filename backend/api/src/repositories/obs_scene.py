from src.models import OBSScene
from src.utils.repository import SQLAlchemyRepository


class OBSSceneRepository(SQLAlchemyRepository):
    """
    Класс репозитория для работы с таблицей OBS сцен.

    Attributes
    ----------
    model : OBSScene
        Модель таблицы OBS сцены, с которой будет работать репозиторий.

    Methods
    -------
    create_entity():
        Метод создания сущности OBS сцены в БД.
    read_one_entity():
        Метод получения одной сущности OBS сцены из БД.
    read_all_entities():
        Метод получения нескольких OBS сцен из БД.
    update_entity():
        Метод обновления OBS сцен в БД.
    delete_entities():
        Метод удаления OBS сцен из БД.
    """
    model = OBSScene
