from fastapi import APIRouter, Depends
from fastapi_pagination import Page, add_pagination, paginate
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import validate_address
from app.core.constants import (HEADERS, URL_GET_ACCOUNT,
                                URL_GET_ACCOUNT_RESOURCE)
from app.core.db import get_async_session
from app.core.tron_client import get_balance, get_energy_and_bandwidth
from app.core.user import current_superuser
from app.crud.wallet import wallet_crud
from app.models.user import User
from app.schemas.wallet import WalletDB

router = APIRouter()


@router.post('/{address}',
             response_model=WalletDB,
             response_model_exclude_none=True,)
async def create_new_wallet(
        address: str,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_superuser)
) -> WalletDB:
    """Создать запись. Только для суперюзеров."""

    await validate_address(address)
    balance = await get_balance(
        URL_GET_ACCOUNT, address, HEADERS
    )
    energy, bandwidth = await get_energy_and_bandwidth(
        URL_GET_ACCOUNT_RESOURCE, address, HEADERS
    )
    data = {
        'balance': balance,
        'energy': energy,
        'bandwidth': bandwidth,
    }
    result = await wallet_crud.create(data, session, user)
    return result


@router.get('/',
            response_model=Page[WalletDB],
            response_model_exclude_none=True,
            dependencies=[Depends(current_superuser)],)
async def get_all_meeting_rooms(
    session: AsyncSession = Depends(get_async_session),
):
    """Получить список всех записей. Только для суперюзеров."""

    result = await wallet_crud.get_multi(session)
    return paginate(result)
add_pagination(router)
