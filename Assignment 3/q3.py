#!/usr/bin/env python

#Assignment 3
#Will Flowers
#question 3

#part a
#matrix = []
#start with: with open('matrix.csv', 'r') as f:
    #for line in f:
    #line = line.strip('\n'
    #L = line.split(','))
    #print L
    #matrix.append(L)
#print matrix

#for L in matrix:
    #for jin in range(len(L)):
        #L[j] = int(L[j])
matrix = [] #create a list to put each line of the matrix we will be using
f = open('matrix.csv', 'r')#open the file
r = f.readline() #read the first line
b = r.strip('\n') #strip out the new line characters
n = b.split(',') #turn it into a string
matrix.append(n) #append that into the matrix list
r = f.readline() #same thing for the other three lines.....
b = r.strip('\n')
n = b.split(',')
matrix.append(n)
r = f.readline()
b = r.strip('\n')
n = b.split(',')
matrix.append(n)
r = f.readline()
b =r.strip('\n')
n = b.split(',')
matrix.append(n)
    
print matrix #print newly made "list of lists"

for c in matrix: #this turns it into a nicer looking matrix
    for d in c:
        print d,
    print
    
#part b

g = raw_input("enter a row number: ")    #get user input for row, column, and new value
e = raw_input("enter a column number: ")
l = raw_input("enter a new value to replace the old value: ")

matrix[int(g)][int(e)] = int(l) #replace those values in the matrix

print matrix #print new matrix

for c in matrix: #print 'nicer' new matrix
    for d in c:
        print d,
    print
f.close #close the file

#part c
#Making a copy of the old matrix file in a new file before writing over it with new data, from example in class
with open('matrix.csv', 'r') as f1, open('matrix2.csv','w') as f2:
    for line in f1:
        f2.write(line)

        
f = open('matrix.csv', 'w') #write back the matrix to the file
f.writelines(str(matrix)) #must be a string
f.close #close file

#could have done:
#with open('matrix.csv', 'w') as f:
    #for L in matrix:
        #for i in L:
            #f.write('%d,' % i),
        #f.write('%d\n'% L[-1])
        
#or
#s = ''
#with open('matrix.csv', 'w') as f:
    #for L in matrix:
        #for i in L:
            #s+=str(i) + ','
        #s = s.strip
        
    
#Extra notes:...
#p = matrix[1][4]
#print p


    
#use 2 for loops
#l=[[1, 2], [3, 4]]
#
#for i in l:
#    for j in i:
#        print j,
#    print
    

    
 