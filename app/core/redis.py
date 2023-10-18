import redis




class Redis:
	def __init__(self, **kwargs:dict[str,str]) -> None:
		self.redis_engine = redis.Redis(
			host=kwargs.get('REDIS_HOST'), 
			port=kwargs.get('REDIS_PORT'), 
			db=kwargs.get('REDIS_DB'), 
			username=kwargs.get('REDIS_USER'), 
			password=kwargs.get('REDIS_PASS')
		)