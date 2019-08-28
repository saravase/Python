import matplotlib.pyplot as plt
import pandas as pd
import sqlalchemy as db
import numpy as np

engine = db.create_engine('mysql+mysqlconnector://root:@localhost:3306/sqlalchemy_mysql')
query = 'select * from post'
post_df = pd.read_sql_query(query, engine)
x = post_df[['name']]
y = post_df[['id']]
colors = np.random.rand(4500)
plt.scatter(x,y,c = colors)
plt.title('Name vs Id')
plt.xlable('Name')
plt.ylable('Id')
plt.show()