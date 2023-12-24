from .base_service import BaseService
from app.repository.user_repository import UserRepository



class AuthService(BaseService):

	def __init__(self, repository: UserRepository):
		super().__init__(repository)

	def access(self):
		return 'Test'

	def refresh(self):
		pass