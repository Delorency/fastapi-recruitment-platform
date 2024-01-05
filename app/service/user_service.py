from app.repository.user_repository import UserRepository

from .base_service import BaseService



class UserService(BaseService):
	def __init__(self, repository: UserRepository):
		super().__init__(repository)