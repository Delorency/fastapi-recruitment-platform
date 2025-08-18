import jwt
from datetime import datetime, timedelta

from fastapi import Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.config import configs
from app.core.exceptions import AuthError, UnauthorizedError



def create_jwt_token(subject: dict, expire_in: timedelta, token_type: str) -> list[str, str]:
	expire_time = (datetime.now(datetime.UTC) + timedelta(seconds=expire_in)).timestamp()

	payload = {'body': subject, 'exp': expire_time, 'type':token_type}
	encode = jwt.encode(payload, configs.jwtcfg.secret_key, algorithm=configs.jwtcfg.alg)

	return encode, expire_time


def decode_token(token: str) -> str:
	try:
		return jwt.decode(token, configs.jwtcfg.secret_key, algorithms=[configs.jwtcfg.alg])
	except:
		raise AuthError('Invalid token')


class JWTBearer(HTTPBearer):
	def __init__(self, is_company:bool|None=None, auto_error:bool=True):
		super(JWTBearer, self).__init__(auto_error=auto_error)
		self.is_company=is_company

	async def __call__(self, request: Request):
		credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
		if credentials:
			if not credentials.scheme == 'Bearer':
				raise AuthError('Schema not resolved') 
			
			token = decode_token(credentials.credentials)

			if not self.verify_jwt(token):
				raise AuthError('Invalid token or token has expired')

			if self.is_company and token['body'].get('is_company') is False:
				raise AuthError('Not company token') 

			return token

		else:
			raise AuthError('Invalid authorization code')


	@classmethod
	def verify_jwt(cls, token:dict, token_type:str='access'):
		is_valid_token: bool = True

		if any((
			token.get('type', '') != token_type,
			'exp' in token and token.get('exp') <= datetime.now(datetime.UTC).timestamp()
		)):
			is_valid_token = False

		return is_valid_token

