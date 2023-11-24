from typing import List
from uuid import uuid4, UUID

from sqlalchemy import ForeignKey, MetaData, Float
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import mapped_column, as_declarative, Mapped

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID

metadata = MetaData()


@as_declarative(metadata=metadata)
class AbstractModel:
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)


class User(SQLAlchemyBaseUserTableUUID, AbstractModel):
    username: Mapped[str] = mapped_column(nullable=False, unique=True)


class Team(AbstractModel):
    __tablename__ = 'team'
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    template_id: Mapped[int] = mapped_column(ForeignKey('template.id'), nullable=False, default=0)
    owner: Mapped[UUID] = mapped_column(ForeignKey('user.id'), nullable=False)

    obs_host: Mapped[str] = mapped_column(nullable=False, default='127.0.0.1')
    obs_port: Mapped[int] = mapped_column(nullable=False, default=4455)
    obs_password: Mapped[str] = mapped_column(nullable=False, default='')


class Photo(AbstractModel):
    __tablename__ = 'photo'
    name: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[str] = mapped_column(nullable=False)
    embeding: Mapped[List[float]] = mapped_column(ARRAY(Float), nullable=False)
    team_id: Mapped[int] = mapped_column(ForeignKey('team.id'), nullable=False)
    url: Mapped[str] = mapped_column(unique=True, nullable=True)


class Template(AbstractModel):
    __tablename__ = 'template'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)


class OBSScene(AbstractModel):
    __tablename__ = 'obs_scene'
    team_id: Mapped[UUID] = mapped_column(ForeignKey('team.id'), nullable=False)
    scene: Mapped[str] = mapped_column(nullable=False)
    source: Mapped[str] = mapped_column(nullable=False)
