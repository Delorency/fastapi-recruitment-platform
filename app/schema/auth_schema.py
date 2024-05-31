from datetime import datetime
from pydantic import BaseModel

from .user_schema import User



class SingUpRequest(BaseModel):
	username:str
	email:str
	name:str
	password:str
	is_company:bool = False

class SingUpResponse(BaseModel):
	id:int
	username:str
	email:str
	name:str
	is_active:bool
	is_company:bool = False


class AccessRequest(BaseModel):
	email:str|None
	username:str|None
	password:str


class AccessResponse(BaseModel):
	access_token: str
	exp: float
	refresh_token: str


class RefreshRequest(BaseModel):
	refresh_token: str

class RefreshResponse(BaseModel):
	access_token: str
	exp: float
	refresh_token: str