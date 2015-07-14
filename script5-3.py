#!/usr/bin/env python

number_list=range (-1,-10,-2);


number_list[-1]=float(number_list[-1])
number_list=number_list[3:]+number_list[2:3]+number_list[:2]+[0]

print number_list


s='I have a dream'
l=s.split()
l.reverse()
string2=''.join(1)
string2=string2.title()




print string2

import random

N=random.randint(1,500)

if N>250:
    print 'N>250'
    if N % 2 == 1:
        print 'N is odd'
    else:
        print'N is even'
        
elif N<250:
    print 'N>250'
    if N % 3 == 0:
        print 'N can be divided by 3'
    else:
        print 'N cannot be divided by three'
else:
    print 'N==250'

    
print N


var = raw_input("say something here:")
if var.isalpha():
    if var. is lower():
        print'it is lower case'
    else:
        var = var.lower()
elif var. isdigit():
    a = int(var)
    print a%3
else:
    print "it is something else"
    
    