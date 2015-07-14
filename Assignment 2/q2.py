#!/usr/bin/env python

#will flowers
#question 2
#palindrome and prime numbers

list1 = []# create an empty list with which to put prime numbers
for i in range(2, 10001): #make the list between 2 and 10000
    # is i a prime?
    prime = True #set the variable prime to true
    for j in range(2, i): # for numbers up to i, for each in in previous for statement
        if i % j == 0: # if this is true, i is divisible by something other than itself
            prime = False
            break #not included in list
    if prime:
        list1.append(i) #put these prime numbers into the list we created above



for k in range(len(list1)): #use a for loop to look at each element in the prime list of numbers
    list2=list(str(list1[k])) #must convert each component to a string, and back to a list in order to be able to reverse it.
    
    list3 = list2[:] #create a copy the new list
    list2.reverse() #reverse it
    
    if list3 == list2: #compare the two lists of prime and reverse primes
        print list3 #if they are the same, print it to obtain answer.
 




    
