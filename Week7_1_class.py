# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 12:32:24 2025

@author: Vincent Mutungi
"""

# Functions 
# Finding the best value of Pizza
# Only original crust pizza
# Step 1: Find the surface area of the pizza 
def pizzaArea(size):
    if size == 's':
        radius = 5
    elif size == 'm':
        radius = 6
    elif size == 'l':
        radius = 7
    else:
        radius = 8
     # calculate area   
    area = 3.14159*radius**2
    return area
#Step 2: New function to calculate prize per square inch, ppsi
def ppsi(cost, size):
    a = pizzaArea(size)
    value = cost/a
    return value

def pizzaCalc():
    s = input('Enter the size of the pizza (s, m, l, or xl): ')
    p = eval(input('Enter the cost of the pizza: '))
    print('$', round(ppsi(p, s), 2))

pizzaCalc()


