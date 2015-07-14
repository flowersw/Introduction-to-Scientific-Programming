#!/usr/bin/env python

#Will Flowers
#Assignment 4
#Question 4

#I will make use of the fill_between function in matplotlib.pyplot, and the stackplot function

#Import numpy and matplotlib.pyplot
import numpy as np 
import matplotlib.pyplot as plt

#set up x range, and y functions
x = np.arange(-6,13,.01)
y1 = np.sin(x)
y22 = x**2
y3 = 3*x + 2
y4 = 2*x - x
y5 = x
y6 =x
y7 =x
y8 = x/2

#Make a subplot of different plots, I have set fill_between to fill in the space between the function and the x
#-axis with color, by using y2 = 0, and None fills everywhere between the function and the x-axis
plt.subplot(3,1,1)
plt.fill_between(x,y1,y2 = 0, color='k', where = None)

plt.subplot(3,1,2)
plt.fill_between(x,y22,y2 = 0, color='r', where = None)

plt.subplot(3,1,3)
plt.fill_between(x,y3,y2 = 0, color = 'b', where = None)

plt.show()

#On a different plot, I have stacked several functions(y5-8)  This "compares them to one another.
#Just because one is on top of another, it doesn't mean it is actually bigger, or rises faster
#This is determined by the order that I have placed them into the plot.
#The thickness of the line is related to how fast it grows, and the magnitude of it, depicted by using
#Three of the same functions and one different
plt.stackplot(x,y5,y6,y7,y8, colors =('r','g','k','b'))
plt.show()




