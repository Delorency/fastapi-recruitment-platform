from datetime import datetime

from pydantic import BaseModel

from .user_schema import User



class SingUp(BaseModel):
	username:str
	email:str
	name:str
	password:str


class SignInResponse(BaseModel):
    access_token: str
    refresh_token: str
    exp: datetime
    user_info: User