from pydantic import BaseModel

from app.schema.user_schema import User



class Payload(BaseModel):
	id: int
	is_active:bool
	is_company:bool = False