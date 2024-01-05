from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject

from app.core.container import Container

from app.schema.auth_schema import SingUpRequest, AccessRequest, AccessResponse
from app.schema.user_schema import User



router = APIRouter(prefix="/auth")


@router.post('/sing-up', response_model=User)
@inject
async def test(schema:SingUpRequest, service=Depends(Provide(Container.auth_service))):
    return service.singup(schema)


@router.post('/access', response_model=AccessResponse)
@inject
async def test(schema: AccessRequest, service=Depends(Provide(Container.auth_service))):
    return service.access(schema)