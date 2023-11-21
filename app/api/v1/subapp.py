from fastapi import FastAPI

from .routes import routers

from app.core.config import configs



subapp = FastAPI()
subapp.include_router(routers)