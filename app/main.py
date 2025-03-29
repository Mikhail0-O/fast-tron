from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routers import main_router
from app.core.config import settings
from app.core.init_db import create_first_superuser


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_first_superuser()
    yield
app = FastAPI(lifespan=lifespan, title=settings.app_title)
app.include_router(main_router)
