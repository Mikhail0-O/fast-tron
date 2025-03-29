import pytest

from app.crud.wallet import wallet_crud
from tests.conftest import get_async_session


@pytest.mark.asyncio
async def test_create_wallet():
    wallet_data = {
        'balance': 1000,
        'energy': 500,
        'bandwidth': 200
    }

    async for session in get_async_session():
        wallet = await wallet_crud.create(wallet_data, session)
        assert wallet is not None, 'Объект не существует'
        assert wallet.balance == 1000, 'Неправильное значение'
        assert wallet.energy == 500, 'Неправильное значение'
        assert wallet.bandwidth == 200, 'Неправильное значение'
        break
