from fastapi import FastAPI

from app.api.v1.endpoints.auth import router as auth_router
from app.api.v1.endpoints.company.profile import router as company_router



subapp = FastAPI()
subapp.include_router(auth_router)
subapp.include_router(company_router)