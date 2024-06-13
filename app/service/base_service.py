from typing import Union

from fastapi import Depends, Request

from app.core.auth import JWTBearer
from app.model.user_model import User



class BaseService:
	def __init__(self, repository):
		self._repo = repository

	def get_obj(self, id:int):
		return self._repo._get_by_id(id)

	def get_by_fields(self,
		page_size:int,
		page:int,
		fields:dict[Union[str,int], Union[str,int]]=dict()
		):
		return self._repo._get_by_fields(fields=fields, page_size=page_size, page=page)

	def create(self, schema):
		return self._repo._create(schema)

	def full_update(self, id, schema):
		return self._repo._full_update(id, schema)

	def partial_update(self, id, schema):
		return self._repo._partial_update(id, schema)