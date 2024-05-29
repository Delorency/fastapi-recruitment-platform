from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session

from app.model.user_model import User
from app.repository.base_repository import BaseRepository



class UserRepository(BaseRepository):
    def __init__(self, session: Callable[..., AbstractContextManager[Session]], utils=None):
        super().__init__(User, session, utils)