from typing import List
import uuid
from src.schemas.template import TemplateRead
from src.utils.unit_of_work import IUnitOfWork


class TemplateService:
    """
    Класс сервиса для реализации логики работы с шаблонами титров.

    Methods
    -------
    get_all_templates():
        Метод получения всех доступных шаблонов.
    get_template_by_team_id():
        Метод получения шаблона, по id команды, которая его использует.
    """
    async def get_all_templates(self, uow: IUnitOfWork) -> List[TemplateRead]:
        '''
        Получает все доступные шаблоны титров.

        Parameters:
            uow (IUnitOfWork): Базовый класс работы с БД сессией.

        Returns:
            templates (List[TemplateRead]): Список схем шаблонов.
        '''
        async with uow:
            templates = await uow.template.read_all_entities()
            return templates

    async def get_template_by_team_id(self, uow: IUnitOfWork, team_id: uuid.UUID) -> TemplateRead:
        '''
        Получает шаблон, по id команды, которая его использует.

        Parameters:
            uow (IUnitOfWork): Базовый класс работы с БД сессией.
            team_id (UUID): Id команды.

        Returns:
            template (TemplateRead): Схема шаблона титра.
        '''
        async with uow:
            team = await uow.team.read_one_entity(id=team_id)
            template_id = team.template_id
            template = await uow.template.read_one_entity(id=template_id)
            return template
