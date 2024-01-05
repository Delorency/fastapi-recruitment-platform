from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session

from app.core.exceptions import NotFoundError, BadRequestError

from app.model.user_model import User
from app.repository.base_repository import BaseRepository



class AuthRepository(BaseRepository):
    def __init__(self, session: Callable[..., AbstractContextManager[Session]]):
        super().__init__(User, session)

    def _get_by_credentials(self, schema):
        with self._session() as session:
            email, username, password = tuple(schema.dict().values())
            if email:
                obj = session.query(self._model).filter(self._model.email==email,
                    self._model.password==password).first()
            elif username:
                obj = session.query(self._model).filter(self._model.username==username,
                    self._model.password==password).first()
            else:
                raise BadRequestError('Email field and username field is empty')

            if not obj:
                raise NotFoundError(f'{self._model.__name__}: Invalid email or username or password')

            return obj

    def _get_by_id_password(self, schema):
        with self._session() as session:
            id, password = tuple(schema.dict().values())
            obj = session.query(self._model).filter(self._model.id==id, self._model.password==password).first()

            if not obj:
                raise NotFoundError(f'{self._model.__name__}: Invalid password')

            return obj