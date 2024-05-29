from sqlmodel import SQLModel, Column, String, Text, Field

from .base_model import Base



class User(Base, table=True):
	username:str = Field(sa_column=Column(String(100), unique=True))
	email:str = Field(sa_column=Column(String(100), unique=True))
	name:str = Field(sa_column=Column(String(100)))
	password:str = Field(sa_column=Column(Text))

	is_active:bool = True
	is_superuser:bool = False
	is_company:bool = False