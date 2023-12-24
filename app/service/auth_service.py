from .base_service import BaseService
from app.repository.user_repository import UserRepository



class AuthService(BaseService):

	def __init__(self, user_repository: UserRepository):
		self.repository = user_repository
		super().__init__(self.repository)

	def sing_up(self):
		pass

	def sing_in(self):
		pass
