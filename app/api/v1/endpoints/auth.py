from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject

from app.core.container import Container



router = APIRouter(prefix="/auth")


@router.get('/access')
@inject
def test(service=Depends(Provide(Container.auth_service))):
    return service.access()