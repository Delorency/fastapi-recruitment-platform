from typing import Callable
from contextlib import AbstractContextManager

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.core.exceptions import DuplicatedError



class BaseRepository:
	def __init__(self, model, session: Callable[...,AbstractContextManager[Session]]) -> None:
		self._model = model
		self._session = session


	def _get_by_id(self, id, session):
		obj = session.query(self._model).filter_by(id=id).first()
		if obj:
			return obj
		raise NotFoundError(detail=f'Not found with id = {id}')


	def _create(self, schema):
		with self._session() as session:
			query = self._model(**schema.dict())
			try:
				session.add(query)
				session.commit()
				session.refresh()
			except IntegrityError as e:
				raise DuplicatedError(detail=str(e.orig))
			return query
	

	def _update(self, id:int, schema:dict):
		with self._session() as session:
			obj = self._get_by_id(id, session)
			obj.update(schema.dict(exclude_none=True))
			session.commit()

		return self._get_by_id(id, session)


	def _delete(self, id):
		with self._session() as session:
			obj = self._get_by_id(id, session)
			session.delete(obj)
			session.commit()