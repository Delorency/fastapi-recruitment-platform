from typing import Any, Callable
from contextlib import AbstractContextManager, contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker

from sqlmodel import SQLModel



class Database:
	def __init__(self, db_url: str) -> None:
		self._engine = create_engine(db_url, echo=True)
		self._session_factory = sessionmaker(
			bind=self._engine,
			autocommit=False,
			autoflush=False
		)
		self._session = scoped_session(self._session_factory)


	def create_database(self) -> None:
		SQLModel.metadata.create_all(self._engine)


	@contextmanager
	def session(self) -> Callable[..., AbstractContextManager[Session]]:
		session: Session = self._session()
		try:
			yield session
		except Exception:
			session.rollback()
			raise
		finally:
			session.close()