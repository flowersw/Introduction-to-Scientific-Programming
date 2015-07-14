#!/usr/bin/env python

#Assignment 3
#Will Flowers
#question 2
#go through list once, compare it with current maximum value, then update as you go
x=[1,3,5,3,66,7,2] #sample list of integers


def min_max(x): #defining a new function min_max(x)
    max1 = min1 = x[0] #set variables max1 and min1 to the first value on the list 'x'
    for i in x: #if there is a number in the list higher or lower than the first, it will be assigned to min1 or max1
        if i > max1:
            max1 = i
        elif i < min1:
            min1 = i
    
    return min1,max1 #return min1 and max1 values
     
print min_max(x) #use the function, then print it

