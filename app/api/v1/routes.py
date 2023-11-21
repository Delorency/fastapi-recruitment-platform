from fastapi import APIRouter

from app.api.v1.endpoints.auth import router as auth_router



routers = APIRouter()
routers.include_router(auth_router)