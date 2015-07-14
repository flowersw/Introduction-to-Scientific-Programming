#!/usr/bin/env python
#Will Flowers
#Question 3
#Fibonacci Sequence

a=0 #set variables a,b and n to their respective values.  a and b are the starting values of the fibbonacci sequence
b=1
n = 10000
while a < n: #use a while loop to find the fibonacci sequence of numbers up to 10000
    print a
    a = b #a becomes b
    b = a + b #b becomes a + b, thus, the sequence is continued.
        

