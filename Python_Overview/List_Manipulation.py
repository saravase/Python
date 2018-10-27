x=[0,1,10,100,1000,10000,10,101,10]
print(x)
x.insert(3,2000)#inserted in 3 position
print(x)
x.insert(8,9000)#inserted only last positon of the list
print(x)
x.remove(10)
print(x)
x.remove(x[3])
print(x)
print(x[-3])
print(x.index(1000))
print(x.count(10))#print num of occurence
x.sort()
print(x)
