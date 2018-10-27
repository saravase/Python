login={'username':'optimus','email':'optimus@gmail.com','password':'Optimus323'}
print(login['username'])
#insert
login['username']="prime"
print(login)
login[0]="primz"#this create new key 0 and value primz
print(login)
del login['email']
print(login)
Student={'optimus':[23,"male"],"prime":[43,"male"]
         }
print(Student)
print(Student['prime'][1])#print sex
