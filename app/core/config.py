import os

from pydantic import BaseSettings

from dotenv import load_dotenv



load_dotenv()


class Configs(BaseSettings):
	# base
	API: str = "/api"
	API_V1_PREFIX:str = f"{API}/v1"
	PROJECT_NAME:str = "recruitment-platform api"
	DB_ENGINE_DICT:dict[str,str] = {
		"postgresql": "postgresql",
		"mysql": "mysql+pymysql",
	}

	# date
	DATETIME_FORMAT:str = "%Y-%m-%dT%H:%M:%S"
	DATE_FORMAT:str = "%Y-%m-%d"

	# auth
	SECRET_KEY:str = os.getenv('SECRET_KEY', '')
	ACCESS_TOKEN_EXPIRE_SECONDS:int = 60 * 60 * 24 * 2
	REFRESH_TOKEN_EXPIRE_SECONDS:int = 60 * 60 * 24 * 30
	ALGORITHM:str = 'HS256'

	# CORS
	BACKEND_CORS_ORIGINS:list[str] = ["*"]

	# Database
	DB:str = os.getenv('DB')
	DB_ENGINE:str = DB_ENGINE_DICT.get(DB)
	DB_HOST:str = os.getenv('DB_HOST')
	DB_PORT:str = os.getenv('DB_PORT')
	DB_NAME:str = os.getenv('DB_NAME')
	DB_USER:str = os.getenv('DB_USER')
	DB_PASS:str = os.getenv('DB_PASS')

	DATABASE_URI_FORMAT:str = "{db_engine}://{user}:{password}@{host}:{port}/{name}"

	DATABASE_URI = DATABASE_URI_FORMAT.format(
		db_engine=DB_ENGINE,
		user=DB_USER,
		password=DB_PASS,
		host=DB_HOST,
		port=DB_PORT,
		name=DB_NAME,
	)

	# Redis
	redis_configs:dict[str, str] = {
		'REDIS_HOST': os.getenv('REDIS_HOST'),
		'REDIS_PORT': os.getenv('REDIS_PORT'),
		'REDIS_DB': os.getenv('REDIS_DB'),
		'REDIS_USER': os.getenv('REDIS_USER'),
		'REDIS_PASS': os.getenv('REDIS_PASS')
	}



configs = Configs()