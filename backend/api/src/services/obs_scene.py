from typing import List
import uuid
from src.schemas.main_schemas import IdRead
from src.schemas.obs_scene import SceneCreate, SceneRead
from src.utils.unit_of_work import IUnitOfWork


class SceneService:
    """
    Класс сервиса для реализации логики работы с OBS сценами.

    Methods
    -------
    create_scene():
        Метод создания сущности OBS сцены в БД.
    get_scenes_by_team_id():
        Метод получения OBS сцен из БД, которые принадлежат одной команде.
    delete_scene_by_id():
        Метод удаления OBS сценя из БД по id.
    delete_scenes_by_team_id():
        Метод удаления всех OBS сцен, принадлежавших команде.
    """
    async def create_scene(self, uow: IUnitOfWork, scene: SceneCreate) -> uuid.UUID:
        '''
        Создаёт сущьность OBS сцены в базе данных.

        Parameters:
            uow (IUnitOfWork): Базовый класс работы с БД сессией.
            scene (SceneCreate): Объект pydentic схемы для создания OBS сцены.

        Returns:
            scene_id (UUID): Id созданной OBS сцены.
        '''
        scene_dict = scene.model_dump(exclude_none=True)
        async with uow:
            scene_id = await uow.scene.create_entity(scene_dict)
            await uow.commit()
            return scene_id
    
    async def get_scenes_by_team_id(self, uow: IUnitOfWork, team_id: uuid.UUID) -> List[SceneRead]:
        '''
        Получает OBS сцены, которые принадлежат команде.

        Parameters:
            uow (IUnitOfWork): Базовый класс работы с БД сессией.
            team_id (UUID): Id команды.

        Returns:
            scenes (List[SceneRead]): Список схем OBS сцен.
        '''
        async with uow:
            scenes = await uow.scene.read_all_entities(team_id=team_id)
            return scenes
    
    async def delete_scene_by_id(self, uow: IUnitOfWork, id: uuid.UUID) -> uuid.UUID:
        '''
        Удаляет OBS сцену по id.

        Parameters:
            uow (IUnitOfWork): Базовый класс работы с БД сессией.
            id (UUID): Id OBS сцены.

        Returns:
            scene_id (UUID): Id удалённой OBS сцены.
        '''
        async with uow:
            scene_ids = await uow.scene.delete_entities(id=id)
            await uow.commit()
            return scene_ids[0]
    
    async def delete_scenes_by_team_id(self, uow: IUnitOfWork, team_id: uuid.UUID) -> List[IdRead]:
        '''
        Удаляет все OBS сцены, которые принадлежат команде.

        Parameters:
            uow (IUnitOfWork): Базовый класс работы с БД сессией.
            team_id (UUID): Id команды.

        Returns:
            res (List[IdRead]): Список схем Id.
        '''
        async with uow:
            scene_ids = await uow.scene.delete_entities(team_id=team_id)
            res = [{"id": scene_id} for scene_id in scene_ids]
            await uow.commit()
            return res
