# -*- coding: utf-8 -*-
import math

x=input("请输入x:")
y=math.sin(x)*math.sin(x)+math.cos(x)
if x==0:
    print "f(x)的值为pi"
elif x>0:
    z=(y+1)**3-3*y
    print "f(x)的值为%0.2f" %(z)
else:
    z=4*y-1
    print "f(x)的值为%0.2f" %(z)
