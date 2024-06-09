from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Column, Field, DateTime

from app.core.config import configs




class Base(SQLModel, table=False):
	id: Optional[int] = Field(default=None, primary_key=True)
	created_at: datetime = Field(sa_column=Column(DateTime(timezone=True),
		default=datetime.utcnow()))
	updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True),
		default=datetime.utcnow(), onupdate=datetime.utcnow()))