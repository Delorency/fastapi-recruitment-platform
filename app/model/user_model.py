from sqlmodel import Field

from .base_model import Base



class User(Base, table=True):
	username:str = Field(max_length=100, unique=True)
	email:str = Field(max_length=100, unique=True)
	name:str = Field(max_length=100)
	password:str = Field()

	photo:str|None = Field()

	is_active:bool = True
	is_superuser:bool = False
	is_company:bool = False