#!/usr/bin/env python

#in class exercise 7-15-13

#Step 1: Create an Array using arange(), reshape(), zeros(), ones(),
#vstack(), hstack()
#[[ 1. 2. 3. 4. 0. 0. 0. 0.]
#[ 5. 6. 7. 8. 1. 1. 1. 1.]
#[-8. -7. -6. -5. -4. -3. -2. -1.]
#[ 1. 2. 3. 4. 5. 6. 7. 8.]]
#Step 2: print every other elements in row 0 and 2:
#1.0, 3.0, 0.0, 0.0
#-8.0, -6.0, -4.0, -2.0



import numpy as np

a = np.arange(1,5)
print a
b = np.arange(5,9)
c = np.ones(4)
d = np.zeros(4)
e = np.arange(-8,0,1)
print e
f = np.arange(1,9)
print f
h = np.hstack((a,d))
j = np.hstack((b,c))
print h,j