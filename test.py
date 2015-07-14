#!/usr/bin/env python

import numpy as np
#
#a = np.linspace(0,1,10,False)
#print a
#
#b = np.array([0, 0.1, 0.2, 0.3, 0.4])
#print b
#
#c = np.arange(0,1,.1)
#print c
#
#def f(i, j):
#    return i+0.1*j
#e = np.fromfunction(f,(1,10)[0])
#    
#def f(i):
#    return 0.1*i
#f = np.fromfunction(f, (10,))
#print f
#
#L = [float(i)/10 for i in range(0, 10)]
#g = np.array(L)
#print G

#J = [1,2,3,4]
#H = [5,6,7,8]
#
#a = np.array(J)
#b = np.array(H)
#print J + H
#print a + b, a * b
#print a**b

#In-class excercise

def matrix_prod(A,B):
    print B.mean()
    np.dot(A**2, B-B.mean())
    
a = np.array([[1,2], [3,4]])
b = np.ones(2,2)
print matrix_prod(a,b)
