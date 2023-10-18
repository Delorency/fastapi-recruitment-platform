from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core.config import configs

from app.core.container import Container



class AppCreator:
	def __init__(self):
		# App
		self.app = FastAPI(
			title=configs.PROJECT_NAME,
			openapi_url=f"{configs.API}/openapi.json",
			version="0.0.1",
		)

		# Container
		self.container = Container()

		# Database
		self.database = self.container.database()
		# self.database.create_database()

		# Middleware
		if configs.BACKEND_CORS_ORIGINS:
			self.app.add_middleware(
				CORSMiddleware,
				allow_origins=[str(origin) for origin in configs.BACKEND_CORS_ORIGINS],
				allow_credentials=True,
				allow_methods=["*"],
				allow_headers=["*"],
			)

		# Add routes


app_creator = AppCreator()
app = app_creator.app
database = app_creator.database
container = app_creator.container