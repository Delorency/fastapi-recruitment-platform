import jwt
from datetime import datetime, timedelta

from fastapi import Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.config import configs
from app.core.exceptions import AuthError, UnauthorizedError



def create_jwt_token(subject: dict, expire_in: timedelta, token_type: str) -> (str, str):
	expire_time = (datetime.utcnow() + timedelta(seconds=expire_in)).timestamp()

	payload = {'body': subject, 'exp': expire_time, 'type':token_type}
	encode = jwt.encode(payload, configs.SECRET_KEY, algorithm=configs.ALGORITHM)

	return encode, expire_time


def decode_token(token: str) -> str:
	try:
		return jwt.decode(token, configs.SECRET_KEY, algorithms=[configs.ALGORITHM])
	except:
		raise AuthError('Invalid token')


class JWTBearer(HTTPBearer):
	def __init__(self, auto_error: bool = True):
		super(JWTBearer, self).__init__(auto_error=auto_error)

	async def __call__(self, request: Request):
		credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)

		if credentials:

			if not credentials.scheme == 'Bearer':
				raise AuthError('Schema not resolved') 

			token = decode_token(credentials.credentials)
			
			if not self.verify_jwt(token):
				raise AuthError('Invalid token or token has expired')

		else:
			raise AuthError('Invalid authorization code')


	@classmethod
	def verify_jwt(cls, token:dict, token_type:str = 'access'):
		is_valid_token: bool = True

		if not token.get('type', '') == token_type:
			is_valid_token = False
		if 'exp' in token and token.get('exp') < datetime.utcnow().timestamp():
			is_valid_token = False

		return is_valid_token

