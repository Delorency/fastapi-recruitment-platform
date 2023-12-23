import redis



class Redis:
	def __init__(self, REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_USER, REDIS_PASS) -> None:
		self.redis_engine = redis.Redis(
			host=REDIS_HOST,
			port=REDIS_PORT,
			db=REDIS_DB,
			username=REDIS_USER,
			password=REDIS_PASS,
			charset="utf-8",
			decode_responses=True
		)