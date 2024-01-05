from pydantic import BaseModel

from app.core.config import configs
from app.core.auth import create_jwt_token, JWTBearer, decode_token
from app.core.exceptions import BadRequestError, ServerSideError

from app.repository.auth_repository import AuthRepository

from app.model.user_model import User

from app.schema.user_schema import User
from app.schema.token_schema import TokenBody, Payload, TokenRefreshHandler

from .base_service import BaseService



class AuthService(BaseService):

	def __init__(self, repository: AuthRepository):
		super().__init__(repository)

	def get_by_credentials(self, schema):
		return self._repo._get_by_credentials(schema)

	def get_by_id_password(self, schema):
		return self._repo._get_by_id_password(schema)

	def singup(self, schema: BaseModel):
		user = self.create(schema)
		delattr(user, 'password')
		return user


	def access(self, schema: BaseModel):
		user: User = self.get_by_credentials(schema)
		try:
			body = Payload(**user.dict()).dict()
			access_token, exp, refresh_token = (
				*create_jwt_token(body, configs.ACCESS_TOKEN_EXPIRE_SECONDS, 'access'),
				create_jwt_token(body, configs.REFRESH_TOKEN_EXPIRE_SECONDS, 'refresh')[0]
			)

			user_info = User(**user.dict()).dict()
		except:
			raise ServerSideError('Token generation error')

		return {
				'access_token':access_token, 
				'refresh_token':refresh_token, 
				'exp':exp, 
				'user_info':user_info
			}


	def refresh(self, schema: BaseModel):
		token_decode = decode_token( schema.dict().get('refresh_token'))
		
		if not JWTBearer.verify_jwt(token_decode, 'refresh'):
			raise BadRequestError('Invalid token type or token has expired')

		try:
			token_handler = TokenRefreshHandler(**token_decode.get('body'),
				password=schema.dict().get('password'))
		except:
			raise BadRequestError('Invalid token body')

		user: User = self.get_by_id_password(token_handler)
		
		try:

			body = Payload(**user.dict()).dict()

			access_token, exp = create_jwt_token(body, 
				configs.ACCESS_TOKEN_EXPIRE_SECONDS, 'access')

			user_info = User(**user.dict()).dict()
		except:
			raise BadRequestError('Invalid token body')

		return {
				'access_token':access_token, 
				'exp':exp, 
				'user_info':user_info
			}