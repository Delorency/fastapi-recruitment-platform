from fastapi import FastAPI

from app.api.v1.endpoints.auth import router as auth_router



subapp = FastAPI()
subapp.include_router(auth_router)