from app.core.auth import decode_token

from app.model.user_model import User



class BaseService:

	def __init__(self, repository):
		self._repo = repository

	def get_obj(self, id):
		return self._repo._get_by_id(id)

	def get_obj_by_credentials(self, schema):
		return self._repo._get_by_credentials(schema)

	def create(self, schema):
		return self._repo._create(schema)

	def patch(self, id, schema):
		return self._repo._update_patch(id, schema)