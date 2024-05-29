from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session

from app.repository.base_repository import BaseRepository

from app.core.auth import decode_token

from app.model.user_model import User



class UtilsRepository(BaseRepository):
	def __init__(self, session: Callable[..., AbstractContextManager[Session]]):
		super().__init__(User, session)
		

	def get_current_user(obj:dict):
		return self._get_by_id(obj['body'].get('id'))