# -*- coding: utf-8 -*-
import math

alphabet=list(map(chr, range(ord('A'), ord('Z')+1 )))

n=int(input("请输入n:"))
k=0

for j in range(n,0,-1):
    for i in range (1,j+1):
        print alphabet[k], 
        k+=1
        if k==26:
            k=0
    print 


