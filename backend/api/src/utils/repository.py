from abc import ABC, abstractmethod
from typing import List, Union
import uuid
from pydantic import BaseModel

from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractRepository(ABC):
    """
    Базовый класс репозитория для работы с БД.

    Methods
    -------
    create_entity():
        Метод создания сущности в БД.
    read_one_entity():
        Метод получения одной сущности из БД.
    read_all_entities():
        Метод получения нескольких сущностей из БД.
    update_entity():
        Метод обновления сущностей в БД.
    delete_entities():
        Метод удаления сущностей из БД.
    """

    @abstractmethod
    async def create_entity(self):
        ...
    
    @abstractmethod
    async def read_one_entity():
        ...
    
    @abstractmethod
    async def read_all_entities():
        ...

    @abstractmethod
    async def update_entity():
        ...
    
    @abstractmethod
    async def delete_entities():
        ...


class SQLAlchemyRepository(AbstractRepository):
    """
    Базовый класс репозитория для работы с БД.

    Attributes
    ----------
    model : AbstractModel
        Модель базы данных, с которой будет работать репозиторий.

    Methods
    -------
    create_entity():
        Метод создания сущности в БД.
    read_one_entity():
        Метод получения одной сущности из БД.
    read_all_entities():
        Метод получения нескольких сущностей из БД.
    update_entity():
        Метод обновления сущностей в БД.
    delete_entities():
        Метод удаления сущностей из БД.
    """
    model = None

    def __init__(self, session: AsyncSession):
        '''
        Объявляет асинхронную сессию.

        Parameters:
            session (AsyncSession): Асинхронная сессия с БД.
    '''
        self.session = session

    async def create_entity(self, data: dict) -> Union[uuid.UUID, int]:
        '''
        Создаёт сущьность в базе данных.

        Parameters:
            data (dict): Словарь с данными о сущности.

        Returns:
            id (Union[UUID, int]): Id созданной сущности.
        '''
        stmt = insert(self.model).values(**data).returning(self.model.id)
        res = await self.session.execute(stmt)
        return res.scalar_one()

    async def update_entity(self, id: Union[uuid.UUID, int], data: dict) -> Union[uuid.UUID, int]:
        '''
        Обновляет сущность в базе данных по id.

        Parameters:
            id (Union[uuid.UUID, int]): id сущности, которую надо обновить.
            data (dict): Словарь с данными о сущности, которые надо обновить.

        Returns:
            id (Union[UUID, int]): Id обновлённой сущности.
        '''
        stmt = update(self.model).values(**data).filter_by(id=id).returning(self.model.id)
        res = await self.session.execute(stmt)
        return res.scalar_one()
    
    async def read_one_entity(self, **filter_by) -> BaseModel:
        '''
        Получает одну сущность по условию.

        Parameters:
            filter_by (dict): Словарь с данными о сущности, по которым будет производиться поиск.

        Returns:
            BaseModel: Объект pydentic схемы.
        '''
        stmt = select(self.model).filter_by(**filter_by)
        res = await self.session.execute(stmt)
        return res.scalar_one().to_read_model()


    async def read_all_entities(self, **filter_by) -> List[BaseModel]:
        '''
        Получает все сущности, удовлетворяющие условию.

        Parameters:
            filter_by (dict): Словарь с данными о сущностях, по которым будет производиться поиск.

        Returns:
            res (List[BaseModel]): Список pydantic схем.
        '''
        stmt = select(self.model).filter_by(**filter_by)
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]
        return res
    
    async def delete_entities(self, **filter_by) -> Union[List[uuid.UUID], List[int]]:
        '''
        Удаляет все сущности, удовлетворяющие условию.

        Parameters:
            filter_by (dict): Словарь с данными о сущностях, по которым будет производиться поиск.

        Returns:
            ids (Union[List[UUID], List[int]]): Список id удалённых сущностей.
        '''
        stmt = delete(self.model).filter_by(**filter_by).returning(self.model.id)
        res = await self.session.execute(stmt)
        ids = [row[0] for row in res.all()]
        return ids
