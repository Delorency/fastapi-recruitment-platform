from dependency_injector import containers, providers

from .config import configs
from .database import Database



class Container(containers.DeclarativeContainer):
	wiring_config = containers.WiringConfiguration(
		modules=[
			'app.api.v1.endpoints.auth',
		]
	)

	database = providers.Singleton(Database, db_url=configs.DATABASE_URI)