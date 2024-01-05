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
				raise NotFoundError(f'{self._model.__name__}: Not found with id = {id}')

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
				raise NotFoundError(f'{self._model.__name__}: Not found with id = {id}')

			session.delete(obj)
			session.commit()