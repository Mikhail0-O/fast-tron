import pytest
from httpx import AsyncClient

from app.core.constants import (DATA_FOR_TESTS, URL_APP_DEV, URL_LOGIN,
                                VALID_ADDRESS)


@pytest.mark.asyncio
async def test_post_validate_address():
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
        response = await client.post(
            f'/api/v1/wallet/{VALID_ADDRESS}',
            headers=headers,
        )
        assert response.status_code == 200, (
            f'Ошибка при создании операции: {response.json()}')
        data = response.json()
        assert 'id' in data, 'Поле "id" отсутствует'
        assert 'balance' in data, 'Поле "balance" отсутствует'
        assert 'energy' in data, 'Поле "energy" отсутствует'
        assert 'bandwidth' in data, 'Поле "bandwidth" отсутствует'
        assert isinstance(data['id'], int), 'Поле "id" должно быть int'
        assert isinstance(data['balance'], int), (
            'Поле "balance" должно быть int')
        assert isinstance(data['energy'], int), (
            'Поле "energy" должно быть int')
        assert isinstance(data['bandwidth'], int), (
            'Поле "bandwidth" должно быть int')
