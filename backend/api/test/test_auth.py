from sqlalchemy import insert, select
from src.models import Template
from conftest import client, async_session_maker

def test_gg():
    assert 1 == 1

async def test_add_template():
    async with async_session_maker() as session:
        session.add(Template(id=0, name="TITLE"))
        await session.commit()

        query = select(Template)
        result = await session.execute(query)
        print(result.all())
        assert result.all() == [(0, 'TITLE')], "Шаблон не добавилась"


# def test_register():
#     response = client.post("/auth/register", json={
#         "email": "string",
#         "password": "string",
#         "is_active": True,
#         "is_superuser": False,
#         "is_verified": False,
#         "username": "string",
#         "template_id": 1,
#         "obs_host": '127.0.0.1',
#         "obs_port": 4455,
#         "obs_password": 'string'
#     })

#     assert response.status_code == 201