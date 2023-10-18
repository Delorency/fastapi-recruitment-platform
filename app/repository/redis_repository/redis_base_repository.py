from redis import Redis



class RedisBaseRepository:
	def __init__(self, connection:Redis):
		self.s = connection