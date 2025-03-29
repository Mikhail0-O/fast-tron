from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import User, Wallet


class CRUDWallet(CRUDBase):

    async def create(
            self,
            obj_in_data: dict,
            session: AsyncSession,
            user: Optional[User] = None
    ):
        if user is not None:
            obj_in_data['user_id'] = user.id
        db_obj = Wallet(**obj_in_data)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj


wallet_crud = CRUDWallet(Wallet)
