from app.repository.user_repository import UserRepository

from app.schema.auth_schema import SingUp

from .base_service import BaseService



class AuthService(BaseService):

	def __init__(self, repository: UserRepository):
		super().__init__(repository)

	def singup(self, schema: SingUp):
		user = self._repo._create(schema)
		delattr(user, 'password')
		return user

	def access(self):
		return 'Test'

	def refresh(self):
		pass