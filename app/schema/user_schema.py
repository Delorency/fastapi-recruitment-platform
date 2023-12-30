from pydantic import BaseModel



class User(BaseModel):
	username:str
	email:str
	name:str
	is_active:bool
	is_superuser:bool