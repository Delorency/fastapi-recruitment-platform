from fastapi import Depends, Request

from app.core.auth import JWTBearer

from app.model.user_model import User



class BaseService:
	def __init__(self, repository):
		self._repo = repository

	def get_obj(self, id):
		return self._repo._get_by_id(id)

	def create(self, schema):
		return self._repo._create(schema)

	def patch(self, id, schema):
		return self._repo._update_patch(id, schema)