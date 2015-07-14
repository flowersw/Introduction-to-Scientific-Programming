#!/usr/bin/env python

#In class exercise 7/5/13

#with open('randominfo.csv','r') as f:
#    readlist = f.readlines()
#    print readlist

#def parse_csv(randominfo):
#    data = {}
#    with open(randominfo, 'r') as f:
#    # read the first line
#    line = f.readline()
#    print line
#    line = line.strip('\n')
#    #parse the line into the list: header
#    header = line.split(',')
#    print header
#    
#    #read the other lines
#    while True:
#        line = f.readline()
#        if not line: # the end of file
#            break
#        line = line.strip('\n')
#        content - line.split(',')
#        print content
#        # insert content into the dictionary
#        data[int(content[0])] = {}
#        for i in range(len(content)): #i = 0, len(content)
#            data[int(content[0])][header[i]] = content[i] #inner dictionary
#        
#        print data[int(content[0])]
#    
#    return data
#
#print parse_csv("list.csv")
#
##import random
##import os
##def function1():
##    os.mkdir('file_testing')
##    #create a folder
##    
##        
##    
##    #create files
##    for i in range(1,101):
##        #create the file, write a random number in it
##        with open('file_testing\%d.txt' %i,'w')as f:
##            f.write(str(random.randint(1,100)))
##            
##function1()
##
##    
##def function2():
##    #list the folder
##    L = # the list of files
##    for i in L:
##        flag = False
##        with open('file_testing/%is' %i, 'r') as f:
##            if int(f.read()) % 2 == 0#would have been a string
##            #we'll delete the file
##            flag = True
##        if flag == True:
##            os.remove('file_testing/%s' %i)
##        #if the content is an even number, delete
##        
##funtion2()
##
##    
##

#recursion
#ex.1 test if a string is palindrom

def isPalindrom(s):
    if len(s) == 0 or len(s) ==1:
        return True
    
    else:
        if s[0]==s[-1] and isPalindrom(s[1:-1]):
        return True
        else:
            return False
print isPalindrome("123232")






    
