from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.core.exceptions import NotFoundError, BadRequestError, DuplicatedError
from app.core.hash import check_password_hash

from app.model.user_model import User

from app.repository.base_repository import BaseRepository



class AuthRepository(BaseRepository):
    def __init__(self, session: Callable[..., AbstractContextManager[Session]]):
        super().__init__(User, session)


    def _get_by_credentials(self, schema):
        with self._session() as session: 
            if schema.email:
                obj = session.query(self._model).filter(self._model.email==schema.email).first()
            elif schema.username:
                obj = session.query(self._model).filter(self._model.username==schema.username).first()
            else:
                raise BadRequestError('Email field and username field is empty')

            if not obj:
                raise NotFoundError(f'{self._model.__name__}: Invalid email or username or password')

            if not obj.is_active:
                raise NotFoundError(f'{self._model.__name__}: Not active user')

            if not check_password_hash(schema.password, obj.password):
                raise NotFoundError(f'{self._model.__name__}: Invalid password')

            return obj


    def _create(self, schema):
        with self._session() as session:
            query = self._model(**schema.dict())

            try:
                session.add(query)
                session.commit()
                session.refresh(query)
            except IntegrityError as e:
                raise DuplicatedError(detail=str(e.orig))
            return query