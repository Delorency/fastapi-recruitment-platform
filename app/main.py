from app.core.container import Container



class ContainerIni:

	def __init__(self):
		
		# Container
		self.container = Container()

		# Database
		self.database = self.container.database()

		# Redis
		self.redis = self.container.redis()



container_ini = ContainerIni()

database = container_ini.database
redis = container_ini.redis
container = container_ini.container