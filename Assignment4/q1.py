#!/usr/bin/env python

#Assignment 4
#Will Flowers
#Question 1
import numpy as np
import array

with open ('Assignment4\question1.csv', 'r')as f:  #open csv file to read numbers from
    a = f.readline()            #read the first line
    j1 = a.strip(',\n')         #strip out commas and newline characters
    print j1                    #print first line
    j = j1.split(',')            #split the string into a list seperated by commas
    
    nh = np.array(j)            #make the list into an array
    nd = np.int_(nh)            #make the values integers
    
    c = f.readline()            #read second line of file
    g = c.strip(',\n')            #strip commas and newline characters
    h = g.split(',')            #split into a list separated by commas
    
    v = np.array(h)            #make into an array
    fg = np.int_(v)            #make the array an array of integers
    stringlist2 = ''            #make a string and for loop to put all integers into string and print for correct format

    for i in fg:
        stringlist2 += str(i) + ','
    stringlist2 = stringlist2.strip(',')    
        
    print stringlist2
    
    c1 = np.zeros(2)            #make an array of two zeros
    d = np.hstack((v,c1))       #put the second line and this new array together
    d1 = np.int_(d)            #make them integers
    
    
    
    a1 = d1 + nd            #perform addition and multiplication on the two arrays
    b1 = d1 * nd
    

    stringlist3 = ''            #use for loop to put results into a string a print

    for i in a1:
        stringlist3 += str(int(i)) + ','
    stringlist3 = stringlist3.strip(',')    
        
    print stringlist3
            
    stringlist4 = ''            #use for loop to put results into a string a print

    for i in b1:
        stringlist4 += str(i) + ','
    stringlist4 = stringlist4.strip(',')    
        
    print stringlist4
    

    
        

        
    
    
    
    
