from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from sqladmin import Admin

from app.core.container import Container
from app.core.config import configs

from app.api.v1.subapp import subapp as api_v1

from app.core.lifespan import lifespan



class AppIniContainer:

	def __init__(self):

		# App
		self.app = FastAPI(
			title=configs.projectcfg.project_name,
			openapi_url=f'{configs.projectcfg.api}/openapi.json',
			version='0.0.1'
		)
		lifespan()

		# Middleware
		if configs.apicfg.backend_cors_origins:
			self.app.add_middleware(
				CORSMiddleware,
				allow_origins=[str(origin) for origin in configs.apicfg.backend_cors_origins],
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
		self.app.mount(configs.projectcfg.api_v1_prefix, api_v1)

		# Mount static directories
		self.app.mount("/static", StaticFiles(directory=f'{configs.projectcfg.project_path}/{configs.projectcfg.static_dir}'), name="static") 

		# Admin
		self.admin = Admin(self.app, self.database._engine)



container_ini = AppIniContainer()

app = container_ini.app
database = container_ini.database
redis = container_ini.redis
container = container_ini.container
admin = container_ini.admin