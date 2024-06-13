from pydantic import BaseModel
from typing import Callable, Union
from contextlib import AbstractContextManager

from sqlalchemy import desc
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.core.exceptions import NotFoundError, BadRequestError, DuplicatedError



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

	def _get_list(self, schema):
		with self._session() as session:
			objs = session.query(self._model)

		return objs.order_by(desc(self._model.updated_at)).limit(
			schema.page_size).offset((schema.page-1)*schema.page_size)

	def _get_by_fields(self,fields:dict[Union[str,int], Union[str,int]]=dict()):
		with self._session() as session:
			objs = session.query(self._model)
			for k,v in fields.items():
				if self._model.__fields__.get(k) is None:
					continue
				objs.filter(self._model.__fields__.get(k)==v)

			return objs

	def _create(self, schema:BaseModel):
		with self._session() as session:
			query = self._model(**schema.dict())
			try:
				session.add(query)
				session.commit()
				session.refresh(query)
			except IntegrityError as e:
				raise DuplicatedError(detail=str(e.orig))
			return query

	def _full_update(self, id:int, schema:BaseModel):
		with self._session() as session:
			session.query(self._model).filter(self._model.id==id).update(schema.dict())
			session.commit()

		return self._get_by_id(id)

	def _partial_update(self, id:int, schema:BaseModel):
		with self._session() as session:
			session.query(self._model).filter(self._model.id==id).update(schema.dict(exclude_none=True))
			session.commit()

		return self._get_by_id(id)

	def _delete(self, id:int):
		with self._session() as session:
			obj = session.query(self._model).filter(self._model.id==id).first()

			if not obj:
				raise NotFoundError(f'{self._model.__name__}: Not found with id = {id}')

			session.delete(obj)
			session.commit()