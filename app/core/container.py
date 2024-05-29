from dependency_injector import containers, providers

from .config import configs
from .database import Database
from .redis import Redis

from app.repository import *
from app.service import *



class Container(containers.DeclarativeContainer):
	wiring_config = containers.WiringConfiguration(
		modules=[
			'app.api.v1.endpoints.auth'
		]
	)

	# Databases
	database = providers.Singleton(Database, db_uri=configs.DATABASE_URI)
	redis = providers.Singleton(Redis, **configs.redis_configs)

	# Repositories
	utils_repository = providers.Factory(UtilsRepository, session=database.provided.session)
	user_repository = providers.Factory(UserRepository, utils=utils_repository, session=database.provided.session)
	auth_repository = providers.Factory(AuthRepository, utils=utils_repository, session=database.provided.session)

	# Services
	user_service = providers.Factory(UserService, repository=user_repository)
	auth_service = providers.Factory(AuthService, repository=auth_repository)