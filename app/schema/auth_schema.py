from datetime import datetime

from pydantic import BaseModel

from .user_schema import User



class SingUpRequest(BaseModel):
	username:str
	email:str
	name:str
	password:str


class SingInRequest(BaseModel):
	email:str|None
	username:str|None
	password:str


class SignInResponse(BaseModel):
	access_token: str
	refresh_token: str
	exp: float
	user_info: User


class TokenBody(BaseModel):
	type:str
	exp: float
	body:User


class Payload(BaseModel):
	id: int
	is_active:bool
	is_superuser:bool