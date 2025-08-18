import os

from pydantic import BaseSettings

from dotenv import load_dotenv



load_dotenv()

class ProjectConfig(BaseSettings):
	api: str = "/api"
	api_v1_prefix:str = f"{api}/v1"
	project_name:str = os.getenv('PROJECT_NAME', 'test project')

	project_path:str = os.getenv('PROJECT_PATH')
	static_dir = os.getenv('STATICDIR')

	datetime_format:str = "%Y-%m-%dT%H:%M:%S"
	date_format:str = "%Y-%m-%d"

	for cfg in [project_path, static_dir]:
		if cfg is None:
			raise Exception('Parsing project config error')


class ServerConfig(BaseSettings):
	host:str = os.getenv('HOST', 'localhost')
	port:str = os.getenv('PORT', '8080')


class DBConfig(BaseSettings):
	db_engine_dict:dict[str,str] = {
		"postgresql": "postgresql",
		"mysql": "mysql+pymysql",
	}
	db:str = os.getenv('DB_TYPE')
	db_engine:str = db_engine_dict.get(db)
	db_host:str = os.getenv('DB_HOST')
	db_port:str = os.getenv('DB_PORT')
	db_name:str = os.getenv('DB_NAME')
	db_user:str = os.getenv('DB_USER')
	db_pass:str = os.getenv('DB_PASS')

	database_uri_format:str = "{db_engine}://{user}:{password}@{host}:{port}/{name}"

	database_uri = database_uri_format.format(
		db_engine=db_engine,
		user=db_user,
		password=db_pass,
		host=db_host,
		port=db_port,
		name=db_name,
	)

	for cfg in [db, db_engine, db_host, db_port, db_name, db_user, db_pass]:
		if cfg is None:
			raise Exception('Parsing db config error')


class RedisConfig(BaseSettings):
	redis_host:str = os.getenv('REDIS_HOST')
	redis_port:str = os.getenv('REDIS_PORT')
	redis_db:str = os.getenv('REDIS_DB')
	redis_user:str = os.getenv('REDIS_USER')
	redis_pass:str = os.getenv('REDIS_PASS')

	for cfg in [redis_host, redis_port, redis_db, redis_user, redis_pass]:
		if cfg is None:
			raise Exception('Parsing redis config error')
		
	redis_configs:dict[str, str] = {
		'REDIS_HOST': redis_host,
		'REDIS_PORT': redis_port,
		'REDIS_DB': redis_db,
		'REDIS_USER': redis_user,
		'REDIS_PASS': redis_pass
	}


class JWTConfig(BaseSettings):
	secret_key:str = os.getenv('SECRET_KEY')
	access_token_expire_second:int = int(os.getenv('ACCESS_TOKEN_EXPIRE', 40000))
	refresh_token_expire_second:int = int(os.getenv('REFRESH_TOKEN_EXPIRE', 200000))
	alg:str = os.getenv('ALG')

	for cfg in [secret_key, alg]:
		if cfg is None:
			raise Exception('Parsing jwt config error')
		


class LoggerConfig(BaseSettings):
	logsdir:str = os.getenv('LOGSDIR')
	apilogfilename:str = os.getenv('APILOGFILENAME')
	dblogfilename:str = os.getenv('DBLOGFILENAME')

	for cfg in [logsdir, apilogfilename, dblogfilename]:
		if cfg is None:
			raise Exception('Parsing logger config error')
		

class APIConfig(BaseSettings):
	page_size:int = 20
	backend_cors_origins:list[str] = ["*"]


class Configs(BaseSettings):
	projectcfg = ProjectConfig()
	servercfg = ServerConfig()
	dbcfg = DBConfig()
	rediscfg = RedisConfig()
	jwtcfg = JWTConfig()
	logcfg = LoggerConfig()
	apicfg = APIConfig()


configs = Configs()