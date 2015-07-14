#!/usr/bin/env python

#Assignment 3, Will Flowers
#Question 1



import os           #import os module
os.mkdir('question1')               #make a directory called question1


with open('list.csv','r')as f:      #open already created file "list.csv
    s = f.read()
    l = s.split(',')        #read it and split it to make it into a list
    print l              #print the result
    k = len(l)        #set new variable k to the length of the newly made list
for i in range(k):   #for the length of the string iterations
    with open('question1/%s.txt' % l[i], 'w') as m: #make that many new files with the names of the files the words from the list as indicated by %s and % l[i]
        m.write(('%s') %len(l[i])) #write the number of letters of the file name has in each file, by len(l[i])


    
    
## his example in class:
#import os
## with open('list.csv', 'r') as f:
    #    for line in f:
    #            line = line.strip('\n')
    #            name_list += line.split(',')
    #print name_list
    #
    #os.mkdir('question1')
    
#for i in name_list:
#    with open('question1\%s.txt' % i, 'w')as f:
#        f.write(str(len(i)))
#    
    
#
#
#
#
#
#
#
#
#
#
#



