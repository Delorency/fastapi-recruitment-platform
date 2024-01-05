from fastapi import Depends
from dependency_injector.wiring import Provide, inject

from app.core.container import Container

from app.model.user_model import User

from app.schema.token_schema import TokenBody, Payload

from .auth import create_jwt_token, decode_token, JWTBearer



@inject
def get_current_user(
	token:str = Depends(JWTBearer()), 
	service = Depends(Provide(Container.user_service))
	) -> User:
	try:
		token_decode = TokenBody(**decode_token(token))
		payload = Payload(**token_decode.body)
	except:
		raise AuthError(details='Not valid credentials')

	user: User = service.get_obj(payload.get('id'))

	return user
