import sqlalchemy as db

class Connection:
	def __init__(self):
		pass

	def connect(self):
		self.engine = db.create_engine('mysql+mysqlconnector://root:@localhost:3306/sqlalchemy_mysql')
		self.connection = self.engine.connect()
		return self.engine