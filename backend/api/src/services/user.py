import uuid
from src.schemas.user import UserUpdate
from src.utils.unit_of_work import IUnitOfWork


class UsersService:
    """
    Класс сервиса для реализации логики работы с пользователями.

    Methods
    -------
    get_team_id_by_tg_id():
        Метод получения id команды, к которой принадлежит пользователь, по его телеграмм id.
    create_or_update_user_by_tg_id():
        Метод обновления или создания пользователя, когда он заходит в команду.
    """
    async def get_team_id_by_tg_id(self, uow: IUnitOfWork, tg_id: int) -> uuid.UUID:
        '''
        Получает фотографии, которые принадлежат команде.

        Parameters:
            uow (IUnitOfWork): Базовый класс работы с БД сессией.
            tg_id (int): Телеграмм id пользователя.

        Returns:
            team_id (UUID): Id команды.
        '''
        async with uow:
            user = await uow.user.read_one_entity(tg_id=tg_id)
            return user.team_id

    async def create_or_update_user_by_tg_id(self, uow: IUnitOfWork, update_user_data: UserUpdate) -> uuid.UUID:
        '''
        Обновлеет или созданёт пользователя, когда он заходит в команду.

        Parameters:
            uow (IUnitOfWork): Базовый класс работы с БД сессией.
            update_user_data (UserUpdate): Pydentic схема пользователя.

        Returns:
            user_id (UUID): Id созданного или обнавлённого пользователя.
        '''
        user_dict = update_user_data.model_dump(exclude_none=True)
        async with uow:
            try:
                user = await uow.user.read_one_entity(tg_id=update_user_data.tg_id)
                #TODO Реализовать логику с is_owner
                user_id = await uow.user.update_entity(user.id, user_dict)
            except:
                user_id = await uow.user.create_entity(user_dict)
            await uow.commit()
        return user_id
