from util.connection import Connection 

con = Connection()
engine = con.connect()
result = engine.execute('select * from post')

# fetchone
# post_result = result.fetchone()

# fetchmany
# post_result = result.fetchmany(3)

# fetchall
post_result = result.fetchall() 
print(post_result)