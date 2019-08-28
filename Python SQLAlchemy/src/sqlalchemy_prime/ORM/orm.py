from sqlalchemy import Table, MetaData, Column, Integer, String
from sqlalchemy.orm import mapper

metadata = MetaData()

todo = Table('Todo', metadata, 
	Column('id', Integer, primary_key = True),
	Column('name', String(100)),
	Column('description', String(100))
	)

class Todo(object):
	def __init__(self,name,description):
		self.name = name
		self.description = description

todo_mapper = mapper(Todo, todo)