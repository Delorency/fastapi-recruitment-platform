from pydantic import BaseModel



class User(BaseModel):
	id:int
	username:str
	email:str
	name:str
	is_company:bool
	is_active:bool
	is_superuser:bool