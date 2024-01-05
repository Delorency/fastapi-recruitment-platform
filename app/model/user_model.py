from sqlalchemy_utils import EncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import AesEngine
from sqlmodel import SQLModel, Column, DateTime, Integer, String, Field, func

from app.core.config import configs

from .base_model import Base



class User(Base, table=True):
	username:str = Field(sa_column=Column(String(100), unique=True))
	email:str = Field(sa_column=Column(String(100), unique=True))
	name:str = Field(sa_column=Column(String(100)))
	password:str = Field(sa_column=Column(EncryptedType(
							String,
							configs.SECRET_KEY,
							AesEngine,
							'pkcs5'
							))
						)



	is_active:bool = True
	is_superuser:bool = False

	def __repr__(self):
		return f'id: {self.id}'