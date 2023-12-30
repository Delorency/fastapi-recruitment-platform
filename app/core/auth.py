import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

from fastapi import Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.config import configs
from app.core.exceptions import AuthError, UnauthorizedError



pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")


def create_jwt_token(subject: dict, expire_in: timedelta, token_type: str) -> (str, str, str):
	expire_time = (datetime.utcnow() + timedelta(seconds=expire_in)).timestamp()

	payload = {**subject, 'exp': expire_time, 'type':token_type}
	encode = jwt.encode(payload, configs.SECRET_KEY, algorithm=configs.ALGORITHM)

	return encode, expire.strftime(configs.DATETIME_FORMAT), token_type


def decode_token(token: str) -> str:
	try:
		return jwt.decode(token, configs.SECRET_KEY, algorithms=[configs.ALGORITHM])
	except Exception as e:
		return {}


def get_password_hash(password: str) -> str:
	return pwd_context.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
	return pwd_context.verify(password, password_hash)



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


	def verify_jwt(self, token:dict):
		is_valid_token: bool = True

		if not token.get('type', '') == 'access':
			is_valid_token = False
		if 'exp' in token and token.get('exp') < datetime.utcnow():
			is_valid_token = False

		return is_valid_token

