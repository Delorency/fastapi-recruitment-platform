from typing import Callable
from contexlib import AbstractContextManager

from sqlalchemy.orm import Session
from sqlalchemy.ext import IntegrityError

from app.core.exception import DuplicatedError



class BaseRepository:
	def __init__(self, model, _session: AbstractContextManager[..., Session]) -> None:
		self._model = model
		self._session = _session


	def _get_by_id(self, id, session):
		obj = session.query(self._model).filter_by(id=id).first()
		if obj:
			return obj
		raise NotFoundError(detail=f'Not found with id = {id}')


	def _create(self, schema:dict):
		with self._session as session:
			query = self._model.query(**schema.dict())
			try:
				session.add(query)
				session.commit()
			except IntegrityError as e:
				raise DuplicatedError(detail=str(e.orig))
			return query
	

	def _update(self, id:int, schema:dict):
		with self._session as session:
			obj = self._get_by_id(id, session)
			obj.update(schema.dict(exclude_none=True))
			session.commit()

		return self._get_by_id(id, session)


	def _delete(self, id):
		with self._session as session:
			obj = self._get_by_id(id, session)
			session.delete(obj)
			session.commit()