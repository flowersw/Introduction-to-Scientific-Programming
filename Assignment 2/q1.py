#!/usr/bin/env python
#Will Flowers
#Question 1

import random #import random module to use
import math # import math module

list1 = [random.normalvariate(82,15) for i in range (50)] #use the normal variate math function to create a list of 50 numbers with mean 82, and standard deviation 15.

for i in range(len(list1)): #must look at each component of list
    
    list1[i]=int(list1[i]) #convert each component into an integer by looking at the value itself instead of just the place holder value.
    
    if list1[i] >= 100: #if that value is greater than 100, replace it with 100
        list1[i]=100
    elif list1[i] <= 0:#if that value is less than 0, replace it with 0
        list1[i]=0
print list1

for i in range(len(list1)): #must look at each component of list
    
    list1[i]=int(list1[i]) #convert each component into an integer by looking at the value itself instead of just the place holder value.
    
    if 90<= list1[i] <= 100 :#deciding if each component is an a,b,c or d
        list1[i]="a"
    if 80<= list1[i] <= 89:
        list1[i]="b"
    if 70<= list1[i] <=79:
        list1[i]="c"
    if 60<= list1[i]<= 69:
        list1[i]="d"

print list1 # print the list of letters

A = list1.count('a')#define new variables to use to print letter grades and count the letter's by their grade
B = list1.count('b')
C = list1.count('c')
D = list1.count('d')

print "This is how many a's there are: "#print number of each grade
print A
print "This is how many b's there are: "
print B
print "This is how many c's there are: "
print C
print "This is how many d's there are: "
print D


