from dependency_injector import containers, providers

from .config import configs
from .database import Database
from .redis import Redis

from app.repository import *
from app.service import *



class Container(containers.DeclarativeContainer):
	wiring_config = containers.WiringConfiguration(
		modules=[
			'app.api.v1.endpoints.auth',
			'app.core.utils'
		]
	)

	# Databases
	database = providers.Singleton(Database, db_url=configs.DATABASE_URI)
	redis = providers.Singleton(Redis, **configs.redis_configs)

	# Repositories
	user_repository = providers.Factory(UserRepository, session=database.provided.session)

	# Services
	auth_service = providers.Factory(AuthService, repository=user_repository)
	user_service = providers.Factory(UserService, repository=user_repository)