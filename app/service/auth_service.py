from pydantic import BaseModel

from app.core.config import configs
from app.core.auth import create_jwt_token
from app.core.exceptions import BadRequestError, ServerSideError

from app.repository.user_repository import UserRepository

from app.model.user_model import User

from app.schema.user_schema import User
from app.schema.token_schema import TokenBody, Payload

from .base_service import BaseService



class AuthService(BaseService):

	def __init__(self, repository: UserRepository):
		super().__init__(repository)


	def singup(self, schema: BaseModel):
		user = self.create(schema)
		delattr(user, 'password')
		return user


	def access(self, schema: BaseModel):
		user_data = schema.dict()
		
		user: User = self.get_obj_by_credentials(schema)

		try:
			body = Payload(**user.dict()).dict()
			access_token, exp, refresh_token = (
				*create_jwt_token(body, configs.ACCESS_TOKEN_EXPIRE_SECONDS, 'access'),
				create_jwt_token(body, configs.REFRESH_TOKEN_EXPIRE_SECONDS, 'refresh')[0]
			)

			user_info = User(**user.dict()).dict()
		except:
			raise ServerSideError(details='Token generation error')

		return {
				'access_token':access_token, 
				'refresh_token':refresh_token, 
				'exp':exp, 
				'user_info':user_info
			}


	def refresh(self, schema: BaseModel):
		pass