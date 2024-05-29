from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from sqladmin import Admin

from app.core.container import Container
from app.core.config import configs

from app.api.v1.subapp import subapp as api_v1



class AppIniContainer:

	def __init__(self):

		# App
		self.app = FastAPI(
			title=configs.PROJECT_NAME,
			openapi_url=f'{configs.API}/openapi.json',
			version='0.0.1'
		)

		# Middleware
		if configs.BACKEND_CORS_ORIGINS:
			self.app.add_middleware(
				CORSMiddleware,
				allow_origins=[str(origin) for origin in configs.BACKEND_CORS_ORIGINS],
				allow_credentials=True,
				allow_methods=["*"],
				allow_headers=["*"],
			)
		
		# Container
		self.container = Container()

		# Database
		self.database = self.container.database()

		# Redis
		self.redis = self.container.redis()

		# Mount subapps
		self.app.mount(configs.API_V1_PREFIX, api_v1)

		# Admin
		self.admin = Admin(self.app, self.database._engine)



container_ini = AppIniContainer()

app = container_ini.app
database = container_ini.database
redis = container_ini.redis
container = container_ini.container
admin = container_ini.admin