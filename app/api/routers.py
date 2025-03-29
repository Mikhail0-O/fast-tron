from fastapi import APIRouter

from app.api.endpoints import user_router, wallet_router

main_router = APIRouter()

main_router.include_router(user_router)
main_router.include_router(
    wallet_router, prefix='/api/v1/wallet', tags=['Wallet']
)
