#!/usr/bin/env python

#in class 7-18-13
#OOP, and intro to simpy
"""
class book():
    def _init_(self, name, pages, price):
        self.name = name
        self.pages = pages
        self.price = price
    def get_name(self):
        return self.name
    def change_price(self, new_price):
        self.price = new_price
    
        
obj = book("a book", 100, 20)
print obj.name, obj.pages, obj.price

print obj.get_name()
opj.change_price(30)
print obj.price
"""
"""
class cars():
    def _init_(self, make, model, color):
        self.make = make
        self.model = model
        self.color= color
    def change_color(self, new_color):
        self.color = new_color
        
class suv(cars):
    def _init_(self, make, model, color, trim):
        self.trim = trim
        cars._init_(self, make, model, color)

a = cars("ford", "explorer", "pink")
print a.color
b = suv("toyota", "camry", "black", "2wd")
print b.color
b.change_color("white")
print b.color
"""
"""
from SimPy.Simulation import*
import random
class Customer(Process):
    def visit(self, t):
        print '%f' % now()
        yield hold, self, t
        print'%f' % now()
    
initialize()

obj = Customer(name = 'Yinqian')

activate(obj, obj.visit(random.randint(10,20)),
        at = random.randint(1,50))
simulate(until = 1000)
"""    

#Drunk man example
from SimPy.Simulation import*
import random

class drunk(Process):
    def _init_(self, name):
        self.location = 0
        Process._init_(self,name = name)
    def go(self):
        while True:
            # change his location
            direction = random.choice([-1,1])
            self.location += direction
            yield hold, self, 1
        
initialize()

simulation_time = 60*60
obj = drunk(name = 'drunk')
activate(obj, obj.go())
simulate(until = simulation_time)
print obj.location
    


