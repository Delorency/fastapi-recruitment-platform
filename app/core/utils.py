from fastapi import Depends
from dependency_injector.wiring import Provide, inject

from .auth import JWTBearer, decode_token

from app.schema.user_schema import User
from app.schema.auth_schema import TokenBody, Payload



@inject
def get_current_user(token:str = Depends(JWTBearer()), 
	service = Depends(Provide(Container.user_service))) -> User:
	try:
		token_decode = TokenBody(**decode_token(token))
		payload = Payload(**token_decode.body)
	except:
		raise AuthError(details='Not valid credentials')

	user: User = service.get_obj(payload.get('id'))

	return user
