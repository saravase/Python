"""import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Sequence
Base = declarative_base()
session = sessionmaker()
engine = db.create_engine('mysql+mysqlconnector://root@localhost:3306/sqlalchemy_mysql')
con = engine.connect()
session.configure(bind = engine)
my_session = session()

class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, Sequence('user_id_seq'),primary_key = True)
	name = Column(String(100))
	firstname = Column(String(100))
	lastname = Column(String(100))

	def __repr__(self):
		return "<User (name ='%s' firstname ='%s' lastname ='%s' )>"%(self.name, self,firstname,self.lastname)

Base.metadata.create_all(engine)"""


from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Sequence
import sqlalchemy as db

session = sessionmaker()
engine = db.create_engine('mysql+mysqlconnector://root@localhost:3306/sqlalchemy_mysql')
con = engine.connect()
session.configure(bind = engine)
my_session = session()

# Create Table

Base = declarative_base()
class Poster(Base):
	__tablename__ = 'poster'
	id = Column(Integer, Sequence('poster_seq_id'), primary_key = True)
	name = Column(String(100))
	description = Column(String(200))

	def __repr__(self):
		return "{ name : '%s' , description : '%s' }"%(self.name, self.description)

Base.metadata.create_all(engine)




































