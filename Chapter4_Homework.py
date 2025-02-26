# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 21:04:15 2025

@author: Vincent Mutungi
"""
# =============================================================================
# HW 3.1) Assume a, b, and c have been defined as shown:
# 
# a, b, c = 7, 8, 9
# 
# Within your Python script, write if statements that print 'OK' if:
# 
# (a) a is less than b.
# 
# (b) c is less than b.
# 
# (c) The sum of a and b is equal to c.
# 
# (d) The sum of the squares a and b is equal to c squared.
# =============================================================================
# Sol 1
# a, b, c = 7, 8, 9
# if a<b: # Check if a is less than b
#     print("OK")
# elif c<b: # Check if c is less than b
#     print("OK")
# elif a+b == c: # Check if the sum of a and b is equal to c
#     print("OK")
# elif (a**2 + b**2) == c**2: # Check if the sum of the squares of a and b is equal to c squared
#     print("OK")
    
# Sol 2
a, b, c = 7, 8, 9
# Check if a is less than b
if a < b:
    print("OK")
# Check if c is less than b
if c < b:
    print("OK")
# Check if the sum of a and b is equal to c
if a + b == c:
    print("OK")
# Check if the sum of the squares of a and b is equal to c squared
if a**2 + b**2 == c**2:
    print("OK")

# =============================================================================
# HW 3.2) Repeat the previous problem with the additional requirement that 'NOT OK' is printed
# 
# if the condition is false.
# =============================================================================
a, b, c = 7, 8, 9
# Check if a is less than b
if a < b:
    print("OK")
else:
    print("NOT OK")
# Check if c is less than b
if c < b:
    print("OK")
else:
    print("NOT OK")
# Check if the sum of a and b is equal to c
if a + b == c:
    print("OK")
else:
    print("NOT OK")
# Check if the sum of the squares of a and b is equal to c squared
if a**2 + b**2 == c**2:
    print("OK")
else:
    print("NOT OK")
        
# =============================================================================
# HW 3.3) Write a for loop that iterates over a list of numbers of a list named lst3 and prints the odd numbers
# 
# in the list.
# 
# For example, if lst3 is [2, 3, 4, 5, 6, 7, 8, 9], then the numbers 3, 5, 7, and 9 should be printed.
# =============================================================================
lst3 = [2, 3, 4, 5, 6, 7, 8, 9]
# Iterate over the list and print odd numbers
print("The odd numbers are;")
for x in lst3:
    if x % 2 != 0:  # Check if the number is odd; not divisible by 2
        print(x)

# =============================================================================
# HW 3.4) Write a for loop that iterates over a list of numbers named lst34 and prints the numbers in the
# 
# list whose square is divisible by 9.
# 
# For example, if lst34 is [2, 3, 4, 5, 6, 7, 8, 9] then the numbers 3, 6 and 9 should be printed.
# =============================================================================
lst34 = [2, 3, 4, 5, 6, 7, 8, 9]
# Iterate over the list and print squares divisible by 9
print("Numbers whose square is divisible by 9 are;")
for x in lst34:
    if x**2 % 9 == 0: # Check if the square of the number is divisible by 9
        print(x)
    else:
        print("None whose square is divisible by 9 are included")
 

# =============================================================================
# HW 3.6) Implement a program that requests a positive integer n from the user and prints the
# 
# first five multiples of n (n*0, n*1, n*2, n*3, and n*4).
# 
# For example:
# 
# Enter n: 9
# 
# 0
# 
# 9
# 
# 18
# 
# 27
# 
# 36
# =============================================================================
# Getting a positive integer from user
n = int(input("Enter a positive integer: "))
# Print the first five multiples of n, including n * 0 we use range 5
for i in range(5):
    print(n * i)


# =============================================================================
# HW 3.7) Implement a program that requests a positive integer n and prints on the screen all the
# 
# Positive integer divisors of n. Note: 0 is not a divisor of any integer, and n divides itself.
# 
# For example:
# 
# Enter n: 49
# 
# 1
# 
# 7
# 
# 49
# =============================================================================
# Getting a positive integer from user
n = int(input("Enter a positive integer: "))
print("Positive divisors of", n, ":") 
for i in range(1, n + 1):  # Loops from 1 to n
    if n % i == 0:  # Check if i is a divisor of n
        print(i) # Print all positive divisors of n
 

# =============================================================================
# HW 3.8) Implement a program that requests four numbers (integer or floating-point) from the
# 
# user. Your program should compute the sum of the first three numbers and compare the
# 
# sum to the fourth number. If they are equal, your program should print 'Equal' on the
# 
# screen.
# 
# >>> 
# 
# Enter first number: 5.5
# 
# Enter second number: 3
# 
# Enter third number: 4
# 
# Enter last number: 12.5
# 
# Equal
# =============================================================================
# Getting four numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input("Enter last number: "))
# Computing the sum of the first three numbers
sum_first_three = num1 + num2 + num3
# Comparing with the fourth number
if sum_first_three == num4:
    print("Equal")
else:
    print("Not Equal")


