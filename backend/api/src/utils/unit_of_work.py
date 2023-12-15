from abc import ABC, abstractmethod
from typing import Type

from src.database import async_session_maker

from src.repositories.user import UserRepository
from src.repositories.photo import PhotoRepository
from src.repositories.obs_scene import OBSSceneRepository
from src.repositories.template import TemplateRepository


class IUnitOfWork(ABC):
    """
    Базовый класс контекстного менеджера для реализации паттерна Unit of Work.

    Attributes
    ----------
    user : UserRepository
        Репозиторий для действий с таблицой Пользователь.
    photo : PhotoRepository
        Репозиторий для действий с таблицой Фотография.
    scene : OBSSceneRepository
        Репозиторий для действий с таблицой OBS сцена.
    template : TemplateRepository
        Репозиторий для действий с таблицой Титр.

    Methods
    -------
    __aenter__():
        Точка входа в контекстный менеджер.
    __aexit__():
        Точка выхода из контекстного менеджера.
    commit():
        Метод для записи изменений в базу данных.
    rollback():
        Метод отката транзакции в базу данных.
    """

    user: Type[UserRepository]
    photo: Type[PhotoRepository]
    scene: Type[OBSSceneRepository]
    template: Type[TemplateRepository]
    
    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    async def __aenter__(self):
        ...

    @abstractmethod
    async def __aexit__(self, *args):
        ...

    @abstractmethod
    async def commit(self):
        ...

    @abstractmethod
    async def rollback(self):
        ...


class UnitOfWork(IUnitOfWork):
    """
    Базовый класс контекстного менеджера для реализации паттерна Unit of Work.

    Attributes
    ----------
    user : UserRepository
        Репозиторий для действий с таблицой Пользователь.
    photo : PhotoRepository
        Репозиторий для действий с таблицой Фотография.
    scene : OBSSceneRepository
        Репозиторий для действий с таблицой OBS сцена.
    template : TemplateRepository
        Репозиторий для действий с таблицой Титр.

    Methods
    -------
    __aenter__():
        Точка входа в контекстный менеджер.
    __aexit__():
        Точка выхода из контекстного менеджера.
    commit():
        Метод для записи изменений в базу данных.
    rollback():
        Метод отката транзакции в базу данных.
    """

    def __init__(self):
        '''
        Объявляет фабрику для сессий с БД.
        '''
        self.session_factory = async_session_maker

    async def __aenter__(self):
        '''
        Точка входа в контекстный менеджер и инициализация полей репозиториев.
        '''
        self.session = self.session_factory()

        self.user = UserRepository(self.session)
        self.photo = PhotoRepository(self.session)
        self.scene = OBSSceneRepository(self.session)
        self.template = TemplateRepository(self.session)

    async def __aexit__(self, *args):
        '''
        Точка выхода из контекстного менеджера. В данном методе происходит откат транзакции 
        (при аварийном выходе из контекстного менеджера) и закрытие сесии.
        '''
        await self.rollback()
        await self.session.close()

    async def commit(self):
        '''
        Запись всех изменений в БД.
        '''
        await self.session.commit()

    async def rollback(self):
        '''
        Откат транзакции.
        '''
        await self.session.rollback()
