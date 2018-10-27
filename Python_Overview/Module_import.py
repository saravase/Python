'''import statistics
a=[1,1,2,3,1,2,12,3,1,2]
x=statistics.mean(a)
print(x)'''

'''
import statistics as s
a=[1,1,2,3,1,2,12,3,1,2]
x=s.mean(a)
print(x)'''

'''from statistics import mean
a=[1,1,2,3,1,2,12,3,1,2]
x=mean(a)
print(x)'''


'''from statistics import mean as m
a=[1,1,2,3,1,2,12,3,1,2]
x=m(a)
print(x)'''


'''from statistics import mean as m,median as md
a=[1,1,2,3,1,2,12,3,1,2]
x=m(a)
y=md(a)
print(x,y)'''

from statistics import *
a=[1,1,2,3,1,2,12,3,1,2]
x=mean(a)
y=median(a)
print(x,y)
