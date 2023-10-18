from datetime import datetime

from typing import Optional

from sqlmodel import SQLModel, Column, DateTime, Field, func




class Base(SQLModel, table=False):
	id: Optional[int] = Field(default=None, primary_key=True)
	created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=func.now()))
	updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=func.now(), onupdate=func.now()))

	def __init__(self, *args, **kwargs):
		self.__tablename__ = self.title.lower().strip()
		return super().__init__(self, *args, **kwargs)