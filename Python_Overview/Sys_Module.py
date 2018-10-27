import sys
sys.stderr.write('optimus this is error')
sys.stderr.flush()
sys.stdout.write("This is not a error")
print(sys.argv)
if len(sys.argv)>1:
    print(sys.argv[1])
else:
    print(sys.argv)
def show(arg):
    print(arg)
show(sys.argv[1])
    
