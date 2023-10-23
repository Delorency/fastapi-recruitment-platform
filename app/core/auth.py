import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



def create_jwt_token(subject: dict, expire_in: timedelta, token_type: str) -> (str, str, str):
	expire_time = datetime.utcnow() + timedelta(seconds=expire_in)
	payload = {**subject, 'exp': expire_time}
	encode = jwt.encode(payload, secret=configs.SECRET_KEY, algorithms=configs.ALGORITHMS)
	return encode, expire.strftime(configs.DATETIME_FORMAT), token_type


def decode_token(token: str) -> dict:
	return jwt.decode(token, configs.SECRET_KEY, algorithms=configs.ALGORITHMS)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
	return pwd_context.verify(password, password_hash)