from datetime import datetime

from typing import Optional

from sqlmodel import SQLModel, Column, DateTime, Field, func




class Base(SQLModel, table=False):
	id: Optional[int] = Field(default=None, primary_key=True)
	created_at: datetime = Field(sa_column=Column(DateTime(timezone=True),
		default=datetime.utcnow()))
	updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True),
		default=datetime.utcnow(), onupdate=datetime.utcnow()))