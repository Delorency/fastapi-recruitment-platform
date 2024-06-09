from typing import Optional

from sqlmodel import Field, Relationship

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

	profile: Optional['Profile'] = Relationship(
		back_populates='user',
		sa_relationship_kwargs={'uselist': False}
	)

	def __str__(self):
		return f'id: {self.id}, username: {self.username}, email: {self.email}'