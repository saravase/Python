import  pandas as pd
import sqlalchemy as db

engine = db.create_engine('mysql+mysqlconnector://root@localhost:3306/sqlalchemy_mysql')
query = 'select * from post'
post_frame = pd.read_sql_query(query, engine)
