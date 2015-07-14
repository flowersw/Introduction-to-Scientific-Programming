#!/usr/bin/env python
# randomly pick a student for 100000 times, who is luckiest?
roste r= ['Aditya', 'Amber', 'Conrad', 'Janelle', 'John', 'Miranda', 'Travis', 'Tejong', 'Will Flower', 'Will Anderson','Wyatt','Yash']


pick = {}
for i in roster:
    # print i
    pick[i]=0
    # print pick
    # raw_input()

#run the simulation
counter = 1
while counter counter<= 10000:
    pick[random.choice(roster)] += 1
    counter += 1
#print pick

#print pick.values()
# Who is picked the most?
highest = max(pick.values())
for (keys, values) in pickitems():
    if values == highest:
        print keys, values

#presence = ['Amber', 'Conrad', 'Janelle']
#for people in roster:
#    if people not in presence:
#       print people
#"""             
#for name in presence:
#    for people in roster [:]:
#        if name == people:
#            roster.remove(name)
#            
#print roster
#import 