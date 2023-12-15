from typing import List
import uuid
from src.schemas.photo import PhotoCreate, PhotoRead
from src.utils.unit_of_work import IUnitOfWork


class PhotoService:
    """
    Класс сервиса для реализации логики работы с фотографиями.

    Methods
    -------
    create_photo():
        Метод создания сущности фотографии в БД.
    get_photos_by_team_id():
        Метод получения фотографий из БД, которые принадлежат одной команде.
    delete_photo_by_id():
        Метод удаления OBS сценя из БД по id.
    """

    async def create_photo(self, uow: IUnitOfWork, photo: PhotoCreate) -> uuid.UUID:
        '''
        Создаёт сущьность фотографии в базе данных.

        Parameters:
            uow (IUnitOfWork): Базовый класс работы с БД сессией.
            photo (SceneCreate): Объект pydentic схемы для создания фотографии.

        Returns:
            photo_id (UUID): Id созданной фотографии.
        '''
        photo_dict = photo.model_dump(exclude_none=True)
        async with uow:
            photo_info = await uow.photo.create_entity(photo_dict)
            await uow.commit()
            return photo_info
    
    async def get_photos_by_team_id(self, uow: IUnitOfWork, team_id: uuid.UUID) -> List[PhotoRead]:
        '''
        Получает фотографии, которые принадлежат команде.

        Parameters:
            uow (IUnitOfWork): Базовый класс работы с БД сессией.
            team_id (UUID): Id команды.

        Returns:
            photos (List[PhotoRead]): Список схем фотографий.
        '''
        async with uow:
            photos = await uow.photo.read_all_entities(team_id=team_id)
            return photos
    
    async def delete_photo_by_id(self, uow: IUnitOfWork, id: uuid.UUID) -> uuid.UUID:
        '''
        Удаляет фотографию по id.

        Parameters:
            uow (IUnitOfWork): Базовый класс работы с БД сессией.
            id (UUID): Id фотографии.

        Returns:
            photo_ids (UUID): Id удалённой фотографии.
        '''
        async with uow:
            photo_ids = await uow.photo.delete_entities(id=id)
            await uow.commit()
            return photo_ids[0]
