import os
cdir=os.getcwd()
print(cdir)
os.mkdir("optimus")

from time import sleep as s
s(3)
os.rename('optimus','prime')
s(3)
os.rmdir('prime')
