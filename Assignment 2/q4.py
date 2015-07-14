#!/usr/bin/env python
#Will Flowers
#Question 4
#mean, variance and standard deviation

import random
import math
user = raw_input("Enter how many numbers: ") #user enters how many numbers and the lambda with which to calculate the mean variance and standard deviation.
lmbda = raw_input("Enter the lambda value with which to calculate mean, variance and standard deviation: ")

num = int(user) #convert the number to an integer
figure = float(lmbda) #convert lamnda to floating point if user wants to use decimals

List1 = [random.expovariate(figure) for i in range(num)] #perform an exponential distribution for however many numbers the user entered.

mean= sum(List1)
mean = mean/num#calculate mean bu summing the elements of list1, and dividing by the number of integers user entered
print mean

squared = 0
for i in List1:
    squared += i**2#get a sum of the squares in list one

variance = (squared/num)-(squared/num**2) #calculate variance
print variance

standard_deviation = math.sqrt(variance) #calculate standard deviation by taking square root of variance found above
print standard_deviation

