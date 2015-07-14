#!/usr/bin/env python

# in class 7-17-13

#linalg, and numerical integration

from scipy import linalg
import numpy as np
"""
#a = np.array([1,3,5,2,5,1,2,3,8]).reshape(3,3)
#c = np.array([10,8,3])
#print a
#b = linalg.inv(a)
#print b
#
#print np.int_(np.dot(a,b))
#
##(x,y,z) = b * c, this is one way to solve this system
#print np.dot(b,c)
#
##another way is to use linalg.solve
#print linalg.solve(a,c)
#
##determinants

#b = linalg.det(a)
#print b

#exercises
i = np.diag(np.ones((3)))
a = linalg.det(i)
print a

b = np.array([1,2,3,5,4,3,5,74,2]).reshape(3,3)
c = linalg.det(np.transpose(b))
print c
d = linalg.det(b)
print d

f = linalg.det(linalg.inv(b))
print f
g = 1 / linalg.det(b)
print g

h = 4*b
k = linalg.det(h)
print k
l = 4**3*linalg.det(b)
print l
"""

from scipy import integrate
import numpy as np

def func():
    return np.exp(x)

print integrate.quad((func),0,1)
