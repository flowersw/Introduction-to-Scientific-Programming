#!/usr/bin/env python

#Will Flowers
#Assignment 4
#question2


import numpy as np                      #import numpy, matplotlib.pyplot, and math modules
import matplotlib.pyplot as plt
import math

x = np.arange(1,12)                      #set range x and function's y respectively
y1 = 1/x
y2 = x**2
y3 = 3*x + 2

#set up seperate plots to plot y1,y2, and y3 against x
plt.plot(x,y1, color='b' , linestyle='--', marker='d' , linewidth='6', label='1/x-asumptote to zero')
plt.plot(x,y2, color='r' , linestyle='-', marker='h' , linewidth='2', label='x**2-exponential increase')
plt.plot(x,y3, color='k' , linestyle=':', marker='2' , linewidth='2', label='3x+2-linear increase')

plt.legend(loc = 1) #set legend location
plt.axis([0,30,0,75]) #set x and y axes ranges for window

#set title, x axis label, and y-axis label
plt.title("Question 2", fontsize=24, color='g')
plt.xlabel("Days", fontsize=18)
plt.ylabel("Money Made", fontsize=18, color='y')

plt.show() #print first graph



#set up second graph, this will be a subplot, but show on a different page than the first
x1 = np.arange(0,30) #set x range

# For each function, I will present a pie graph that compares the amount of "money" made from each function over 12 "days"
#I will sum each function up over 12 days below, put into lists, and plot a pie graph of the data
sumy1 = []
for i in range(1,13):
    sumy1.append(int(i**2))
tu = math.fsum(sumy1)

sumy2 = []
for op in range(1,13):
    sumy2.append(int(3*i + 2))
ru = math.fsum(sumy2)

sumy3 = []
for i in range(1,13):
    sumy3.append(float(1/i))
pu = math.fsum(sumy3)

qu = [tu,ru,pu]

#set up pie graph
labels = ['y1', 'y2','y3']
plt.subplot(1,1,1)  #this is technically a subplot, even though only one graph will show on this page
#set up text to represent the functions of different areas in pie graph(could have done this with labels, but wanted to implement the text function)
plt.text(0,1.1, "x**2", fontsize=20, color="b")
plt.text(0,-1.25, "3*x+2", fontsize=20, color="g")
plt.text(1.25,0, "1/x", fontsize=20, color="k")
plt.title("Comparison of amount of money made", fontsize=24, color='w') #set title to pie graph
plt.pie(qu, labels=labels)  #call pie graph function
plt.show()  #print out
