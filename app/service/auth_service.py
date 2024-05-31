from pydantic import BaseModel

from app.core.config import configs
from app.core.auth import create_jwt_token, JWTBearer, decode_token
from app.core.exceptions import BadRequestError, ServerSideError
from app.core.hash import generate_password_hash

from app.repository.auth_repository import AuthRepository

from app.schema.token_schema import Payload

from app.model.user_model import User

from .base_service import BaseService



class AuthService(BaseService):

	def __init__(self, repository: AuthRepository):
		super().__init__(repository)

	def get_by_credentials(self, schema):
		return self._repo._get_by_credentials(schema)


	def singup(self, schema: BaseModel):
		schema.password = generate_password_hash(schema.password)
		obj = self.create(schema)
		delattr(obj, 'password')
		return obj


	def access(self, schema: BaseModel):
		obj:User = self.get_by_credentials(schema)
		try:
			body = Payload(**obj.dict()).dict()
			access_token, exp, refresh_token = (
				*create_jwt_token(body, configs.ACCESS_TOKEN_EXPIRE_SECONDS, 'access'),
				create_jwt_token(body, configs.REFRESH_TOKEN_EXPIRE_SECONDS, 'refresh')[0]
			)
		except:
			raise ServerSideError('Token generation error')

		return {		
				'access_token':access_token, 
				'refresh_token':refresh_token, 
				'exp':exp
			}


	def refresh(self, schema: BaseModel, user):
		token_decode = decode_token(schema.refresh_token)
		
		if not JWTBearer.verify_jwt(token_decode, 'refresh'):
			raise BadRequestError('Invalid token type or token has expired')

		if not token_decode['body'].get('id') == user.id:
			raise BadRequestError('Incorrect refresh token')

		try:
			body = Payload(**user.dict()).dict()

			access_token, exp = create_jwt_token(body, 
				configs.ACCESS_TOKEN_EXPIRE_SECONDS, 'access')
		except:
			raise BadRequestError('Invalid token body')

		return {
				'access_token':access_token, 
				'exp':exp, 
				'refresh_token':schema.refresh_token
			}