from typing import Callable
from contextlib import AbstractContextManager

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.core.exceptions import NotFoundError, BadRequestError



class BaseRepository:
	def __init__(self, model, session: Callable[...,AbstractContextManager[Session]]) -> None:
		self._model = model
		self._session = session


	def _get_by_id(self, id:int):
		with self._session() as session:
			obj = session.query(self._model).filter(self._model.id==id).first()

			if not obj:
				raise NotFoundError(detail=f'{self._model.__name__}: Not found with id = {id}')

			return obj


	def _get_by_credentials(self, schema):
		with self._session() as session:
			email, username, password = tuple(schema.dict().values())
			if email:
				obj = session.query(self._model).filter(self._model.email==email, self._model.password==password).first()
			elif username:
				obj = session.query(self._model).filter(self._model.username==username, self._model.password==password).first()
			else:
				raise BadRequestError('Email field and username field is empty')

			if not obj:
				raise NotFoundError(detail=f'{self._model.__name__}: Invalid email or username or password')

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
	

	def _update_patch(self, id:int, schema):
		with self._session() as session:
			session.query(self.model).filter(self._model.id==id).update(schema.dict(exclude_none=True))
			session.commit()

		return self._get_by_id(id)


	def _update_put(self, id:int, schema):
		with self._session() as session:
			session.query(self.model).filter(self._model.id==id).update(schema.dict())
			session.commit()

		return self._get_by_id(id)


	def _delete(self, id:int):
		with self._session() as session:
			obj = session.query(self._model).filter(self._model.id==id)

			if not obj:
				raise NotFoundError(detail=f'{self._model.__name__}: Not found with id = {id}')

			session.delete(obj)
			session.commit()