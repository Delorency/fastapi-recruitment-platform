from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Column, String, Text, Field, DateTime

from app.core.config import configs




class Base(SQLModel, table=False):
	id: Optional[int] = Field(default=None, primary_key=True)
	created_at: datetime = Field(sa_column=Column(DateTime(timezone=True),
		default=datetime.utcnow()))
	updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True),
		default=datetime.utcnow(), onupdate=datetime.utcnow()))


class User(Base, table=False):
	username:str = Field(sa_column=Column(String(100), unique=True))
	email:str = Field(sa_column=Column(String(100), unique=True))
	name:str = Field(sa_column=Column(String(100)))
	password:str = Field(sa_column=Column(Text))

	is_active:bool = True