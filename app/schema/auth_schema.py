from datetime import datetime

from pydantic import BaseModel

from .user_schema import User



class SingUpRequest(BaseModel):
	username:str
	email:str
	name:str
	password:str


class AccessRequest(BaseModel):
	email:str|None
	username:str|None
	password:str


class AccessResponse(BaseModel):
	access_token: str
	refresh_token: str
	exp: float
	user_info: User