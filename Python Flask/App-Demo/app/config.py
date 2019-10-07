class Config:
	DEBUG = False
	KEY = 'Optimusmom@1492'

class ProductionConfig(Config):
	pass

class DevelopmentConfig(Config):
	DEBUG = True

class TestConfig(Config):
	pass