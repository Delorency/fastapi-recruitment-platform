import redis



class Redis:
	def __init__(self, REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_USER, REDIS_PASS) -> None:
		self.redis_engine = redis.Redis(
			host='localhost',
			port='6379',
			db=1,
			username='delorency',
			password='delorency',
			charset="utf-8",
			decode_responses=True
		)