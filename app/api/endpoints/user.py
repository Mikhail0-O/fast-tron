from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import auth_backend, current_superuser, fastapi_users
from app.crud.user import user_crud
from app.schemas.user import UserCreate, UserRead, UserUpdate

router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth/jwt',
    tags=['auth'],
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/auth',
    tags=['auth'],
)


users_router = fastapi_users.get_users_router(UserRead, UserUpdate)

router.include_router(
    users_router,
    prefix='/users',
    tags=['users'],
)


@router.get('/users',
            response_model=list[UserRead],
            tags=['users'],
            dependencies=[Depends(current_superuser)],)
async def get_all_users(
    session: AsyncSession = Depends(get_async_session),
):
    """Получить списаок всех пользователей. Только для суперюзеров."""

    return await user_crud.get_multi(session)
