from http import HTTPStatus

from fastapi import HTTPException

from app.core.constants import HEADERS, URL_VALIDATE_ADDRESS
from app.core.tron_client import tron_client


async def validate_address(address: str):
    result = await tron_client(URL_VALIDATE_ADDRESS, address, HEADERS)
    if not result.get('result'):
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Указанный адрес кошелька  не прошел валидацию!',
        )
