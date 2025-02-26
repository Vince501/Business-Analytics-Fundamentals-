# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 12:45:05 2025

@author: Vincent Mutungi
"""

# Program 4-1, pg 46

# Initialization

i = 1 # Starting value
n = 5 # Ending value

# Uisng while, generate table
while i <= n:
    #calculate and display i^2 and i^3
    print(i, i**2, i**3, sep = '\t')
    #Increamenting i
    #i = i + 1
    #i += 1
    i += 2
print("End of Program!")

## for loops
# Using a list

list1 = [1,3,4,7]

for um in list1: # um is a Local Variable
    print(um, um**2, " and I am cute :)")
print("End of Program!")
##
s2 = "Vincent"
for value in s2:
    print(value)
print("End of Program!")


## Loop to find whether a number is prime or not

n = eval(input("Enter a Positive Integer: "))
for i in range(2,n):
    if n%i == 0:
        print("Not a Prime Number!")
        break
    else:
        print(n, " is not divisible by ", i)























