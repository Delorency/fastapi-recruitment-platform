from sqlmodel import SQLModel, Column, DateTime, Integer, String, Field, func

from .base_model import Base



class User(Base, table=True):
	username:str = Field(sa_column=Column(String(100), unique=True, nullable=False))
	email:str = Field(sa_column=Column(String(100), unique=True))
	password:str = Field(sa_column=Column(String))
	name:str = Field(sa_column=Column(String(100)))


	def __repr__(self):
		return f'id: {self.id}'