#!/usr/bin/env python

#Will Flowers
#Assignment 4
#Question 3

import numpy as np
from scipy import linalg

#part 1
#make arrays A, and B , using array and reshape
A = np.array([6,2,5,7,4,1,2,6,9]).reshape(3,3)


B = np.array([1,5,3,6,5,4,9,8,2]).reshape(3,3)

#take inverse of A and B

D = linalg.inv(A)

E = linalg.inv(B)

#Take dot product of inverses of A and B
C = np.dot(E,D)
print C


#take dot product of original A and B
G = np.dot(A,B)
#take inverse of that
J = linalg.inv(G)
print J
#The two results are the same


#part 2
print np.transpose(G)    #take transpose of dot product of A and B

U = np.transpose(B)
JU = np.transpose(A)
JUU = np.dot(U,JU)  #Take dot product of transpose of A and B
print JUU #print result
#They are the same


#part 3
print linalg.det(G)  #Take determinant of dot of A and B
print linalg.det(A)*linalg.det(B) #print dot of determinant of A and B
#they are the same