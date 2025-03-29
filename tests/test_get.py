import pytest
from httpx import AsyncClient

from app.core.constants import DATA_FOR_TESTS, URL_APP_DEV, URL_LOGIN


@pytest.mark.asyncio
async def test_get():
    async with AsyncClient(base_url=URL_APP_DEV) as client:
        response = await client.post(
            URL_LOGIN,
            data=DATA_FOR_TESTS,
        )
        assert response.status_code == 200, (
            f'Ошибка при входе: {response.json()}')
        token = response.json().get('access_token')
        assert token, 'Токен не был получен'
        headers = {'Authorization': f'Bearer {token}'}
        response = await client.get(
            '/api/v1/wallet/?page=1&size=50',
            headers=headers,
        )
        assert response.status_code == 200, (
            f'Ошибка при создании операции: {response.json()}')
        data = response.json()
        assert 'items' in data, 'Поле "items" отсутствует'
        assert 'total' in data, 'Поле "total" отсутствует'
        assert 'page' in data, 'Поле "page" отсутствует'
        assert 'size' in data, 'Поле "size" отсутствует'
        assert 'pages' in data, 'Поле "pages" отсутствует'
        assert isinstance(data['items'], list), 'Поле "items" должно быть list'
        assert isinstance(data['total'], int), 'Поле "total" должно быть int'
        assert isinstance(data['page'], int), 'Поле "page" должно быть int'
        assert isinstance(data['size'], int), 'Поле "size" должно быть int'
        assert isinstance(data['pages'], int), 'Поле "pages" должно быть int'
