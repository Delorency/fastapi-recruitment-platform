from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject

from app.core.secure import get_current_active_user
from app.core.container import Container

from app.schema.auth_schema import SingUpRequest, SingUpResponse, \
    AccessRequest, AccessResponse, RefreshRequest, RefreshResponse



router = APIRouter(prefix="/auth", tags=['Auth / Registration, Authentication, Authorization'])


@router.post('/sing-up', response_model=SingUpResponse, summary='Registration', status_code=201)
@inject
async def singup(
    schema:SingUpRequest,
    service=Depends(Provide[Container.auth_service])
    ):
    return service.singup(schema)


@router.post('/access', response_model=AccessResponse, summary='Get access-refresh tokens pair')
@inject
async def access(
    schema: AccessRequest,
    service=Depends(Provide[Container.auth_service])
    ):
    return service.access(schema)


@router.post('/refresh', response_model=AccessResponse, summary='Get new access token')
@inject
async def refresh(
    schema: RefreshRequest,
    user=Depends(get_current_active_user),
    service=Depends(Provide[Container.auth_service])
    ):
    return service.refresh(schema, user)