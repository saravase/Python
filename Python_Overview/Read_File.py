read1=open('read.txt','r').read()
print(read1)

#read2=open('login.xlsx','r').read()
#print(read2)#not work

output=open('output.txt','w')
data='''my mom is my only world
she is my only friend
'''
output.write(data)
output.close()

