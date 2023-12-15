from abc import abstractmethod
from typing import List
from uuid import uuid4, UUID
from pydantic import BaseModel

from sqlalchemy import ForeignKey, MetaData, Float
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import mapped_column, as_declarative, Mapped

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from src.schemas.obs_scene import SceneRead
from src.schemas.photo import PhotoRead
from src.schemas.template import TemplateRead

from src.schemas.user import UserRead

metadata = MetaData()

@as_declarative(metadata=metadata)
class AbstractModel:
    """
    Базовый класс всех таблиц. Класс задаёт поле id в формате UUID.

    Attributes
    ----------
    id : UUID
        Id таблицы в формате UUID.

    Methods
    -------
    to_read_model():
        Преобразует модель базы данных в pydantic схему.
    """

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)

    @abstractmethod
    def to_read_model(self) -> BaseModel:
        '''
        Преобразует модель базы данных в pydantic схему.

        Returns:
            BaseModel: Базовый класс схемы pydantic.
        '''
        ...


class User(SQLAlchemyBaseUserTableUUID, AbstractModel):
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    template_id: Mapped[int] = mapped_column(ForeignKey('template.id'), nullable=False, default=0)

    obs_host: Mapped[str] = mapped_column(nullable=False, default='127.0.0.1')
    obs_port: Mapped[int] = mapped_column(nullable=False, default=4455)
    obs_password: Mapped[str] = mapped_column(nullable=False, default='')

    def to_read_model(self) -> UserRead:
        '''
        Преобразует модель пользователя из базы данных в pydantic схему.

        Returns:
            UserRead: Cхема pydantic для чтения пользователя.
        '''
        return UserRead(
            id=self.id,
            email=self.email,
            username=self.username,
            template_id=self.template_id,
            obs_host=self.obs_host,
            obs_port=self.obs_port,
            obs_password=self.obs_password
        )


class Photo(AbstractModel):
    __tablename__ = 'photo'
    name: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[str] = mapped_column(nullable=False)
    embeding: Mapped[List[float]] = mapped_column(ARRAY(Float), nullable=False)
    team_id: Mapped[UUID] = mapped_column(ForeignKey('user.id'), nullable=False)
    url: Mapped[str] = mapped_column(unique=True, nullable=True)

    def to_read_model(self) -> PhotoRead:
        '''
        Преобразует модель фотографии из базы данных в pydantic схему.

        Returns:
            PhotoRead: Cхема pydantic для чтения фотографии.
        '''
        return PhotoRead(
            id=self.id,
            name=self.name,
            role=self.role,
            embeding=self.embeding,
            team_id=self.team_id,
            url=self.url
        )


class Template(AbstractModel):
    __tablename__ = 'template'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)

    def to_read_model(self) -> TemplateRead:
        '''
        Преобразует модель титра из базы данных в pydantic схему.

        Returns:
            TemplateRead: Cхема pydantic для чтения титра.
        '''
        return TemplateRead(
            id=self.id,
            name=self.name
        )


class OBSScene(AbstractModel):
    __tablename__ = 'obs_scene'
    team_id: Mapped[UUID] = mapped_column(ForeignKey('user.id'), nullable=False)
    scene: Mapped[str] = mapped_column(nullable=False)
    source: Mapped[str] = mapped_column(nullable=False)

    def to_read_model(self) -> SceneRead:
        '''
        Преобразует модель OBS сцены из базы данных в pydantic схему.

        Returns:
            SceneRead: Cхема pydantic для чтения OBS сцены.
        '''
        return SceneRead(
            id=self.id,
            team_id=self.team_id,
            scene=self.scene,
            source=self.source
        )
