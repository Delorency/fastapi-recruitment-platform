from typing import Union

from fastapi import Depends, Request

from app.core.auth import JWTBearer
from app.model.user_model import User



class BaseService:
	def __init__(self, repository):
		self._repo = repository

	def get_obj(self, id:int):
		return self._repo._get_by_id(id)

	def get_by_fields(self, fields:dict[Union[str,int], Union[str,int]]):
		return self._repo._get_by_fields(fields)

	def create(self, schema):
		return self._repo._create(schema)

	def patch(self, id, schema):
		return self._repo._update_patch(id, schema)

	def put(self, id, schema):
		return self._repo._update_put(id, schema)