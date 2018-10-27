#local variable
x=9
def sim():
    print(x)
    glob=x
    glob+=90
    print(glob+8)
sim()

#global variable
y=9
def hi():
    global y
    print(y)
    y+=90
    print(y)
hi()
print(x,y)
