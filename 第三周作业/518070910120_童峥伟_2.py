# -*- coding: utf-8 -*-
a = 1
b = 1
c = a + b
while c <= 100:
    a = b
    b = c
    c = a + b
print("Fibonacci数列中第一个大于100的数是%d。" % (c))
