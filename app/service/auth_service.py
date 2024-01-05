from pydantic import BaseModel

from app.repository.user_repository import UserRepository

from .base_service import BaseService



class AuthService(BaseService):

	def __init__(self, repository: UserRepository):
		super().__init__(repository)

	def singup(self, schema: BaseModel):
		user = self.create(schema)
		delattr(user, 'password')
		return user

	def access(self):
		return 'Test'

	def refresh(self):
		pass