from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker,
                                    create_async_engine)

from app.core.constants import DATABASE_URL_FRO_TEST

engine = create_async_engine(DATABASE_URL_FRO_TEST)
AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession)


async def get_async_session():
    async with AsyncSessionLocal() as async_session:
        yield async_session
