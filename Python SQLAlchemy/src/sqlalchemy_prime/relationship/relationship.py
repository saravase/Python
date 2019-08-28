import sqlalchemy as db
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

session = sessionmaker()
engine = db.create_engine('mysql+mysqlconnector://root@localhost:3306/sqlalchemy_mysql')
con = engine.connect()
session.configure(bind = engine)
my_session = session()
Base = declarative_base()

class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, Sequence('user_id_seq'),primary_key = True)
	name = Column(String(100))
	fullname = Column(String(100))
	nickname = Column(String(100))
	
	def __repr__(self):
		return "< fullname : '%s' nickname : '%s'>"%(self.fullname, self.nickname)

Base.metadata.create_all(engine)

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Address(Base):
	__tablename__ = 'addresses'
	id = Column(Integer, Sequence('add_id_seq'), primary_key = True)
	email_address = Column(String(100) , nullable = False)
	user_id = Column(Integer, ForeignKey('users.id'))
	user = relationship("User", back_populates = 'addresses')

	def __repr__(self):
		return "<email_address : '%s'>"%(self.email_address)

User.addresses = relationship("Address", order_by = Address.id , back_populates = "user")

Base.metadata.create_all(engine)


