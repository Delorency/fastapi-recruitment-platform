from pydantic import BaseModel

from app.schema.user_schema import User



class TokenBody(BaseModel):
	type:str
	exp: float
	body:User


class Payload(BaseModel):
	id: int
	is_active:bool
	is_superuser:bool


class TokenRefreshHandler(BaseModel):
	id:int
	password:str