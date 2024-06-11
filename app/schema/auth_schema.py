import re

from datetime import datetime
from pydantic import BaseModel, validator, EmailStr

from app.core.exceptions import BadRequestError
from .user_schema import User



class SingUpRequest(BaseModel):
	username:str|None
	email:EmailStr
	name:str
	password:str
	is_company:bool = False

	@validator('username')
	@classmethod
	def validate_username(cls, value):
		if len(value) < 3:
			raise BadRequestError("The username must be at least 3 characters long")
		return value

	# @validator('email')
	# @classmethod
	# def validate_email(cls, value):
	# 	if not bool(re.fullmatch(r'[\w.-]+@[\w-]+\.[\w.]+', value)):
	# 		raise BadRequestError("Email is invalid")
	# 	return value 

	@validator('password')
	@classmethod
	def validate_password(cls, value):
		password_length = len(value)
		if password_length < 8 or password_length > 32:
			raise BadRequestError("The password must be between 8 and 32 characters long")
		return value

class SingUpResponse(BaseModel):
	id:int
	username:str
	email:str
	name:str
	is_active:bool
	is_company:bool = False


class AccessRequest(BaseModel):
	username:str|None
	email:str|None
	password:str

	@validator('username')
	@classmethod
	def validate_username(cls, value):
		if value and len(value) < 3:
			raise BadRequestError("The username must be at least 3 characters long")
		return value

	@validator('email')
	@classmethod
	def validate_email(cls, value):
		if value and not bool(re.fullmatch(r'[\w.-]+@[\w-]+\.[\w.]+', value)):
			raise BadRequestError("Email is invalid")
		return value 

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