# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 20:56:50 2025

@author: Vincent Mutungi
"""
# 5.7 Dollar Store
def calcCost(count):
    # Cost is $1 per item
    base_cost = count * 1.0
    # Apply 5% discount if 10 or more items
    if count >= 10:
        discounted_cost = base_cost * 0.95
    else:
        discounted_cost = base_cost
    return discounted_cost

def displayLine(label, amount):
    # Display label and amount with specific width and 2 decimal places
    print(f"{label:10}{amount:>8.2f}")

def display(cost, tax):
    # Calculate net cost (pre-tax), tax, and after-tax amounts
    net_cost = cost
    tax_amount = cost * 0.075  # 7.5% sales tax
    after_tax = net_cost + tax_amount

    # Display the results
    displayLine("Net Cost: ", net_cost)
    displayLine("Tax: ", tax_amount)
    displayLine("After tax: ", after_tax)

# Main program
# Error handling for invalid inputs (non-integers or negative numbers)
try:
    # Prompt user for number of items
    count = int(input("Enter number of items: "))
    if count < 0:
        print("Please enter a non-negative number of items.")
    else:
        # Calculate pre-tax cost
        cost = calcCost(count)
        # Display the results
        display(cost, 0.075)  # Pass tax rate as 7.5%
except ValueError:
    print("Please enter a valid integer.")


# 6.1 Min and Max
def minmax(alist):
    # Check if the list is empty
    if not alist:
        return None, None

    # Initialize min and max with the first element
    value_min = alist[0]
    value_max = alist[0]

    # Iterate through the list to find min and max
    for item in alist:
        if item < value_min:
            value_min = item
        if item > value_max:
            value_max = item

    return value_min, value_max

# Test the function on a list of numbers
lo, hi = minmax([1, 2, 3])
print(lo, hi)
# Test the function on a list of words
lo, hi = minmax(["what", "are", "the", "min", "and", "max"])
print(lo, hi)
# Test the function on an empty list
print(minmax([]))


# 6.3 Mean and Standard Deviation Excluding Outliers
def filterOutliers(alist, arange):
    # New list with values within the specified range of values...
    # within the range [arange[0], arange[1]] without modifying the original list.
    result = []
    for value in alist:
        if arange[0] <= value <= arange[1]:
            result.append(value)
    return result

def calcStats(alist):
    # Check if the list is empty
    if not alist:
        return None, None

    # Calculate mean
    n = len(alist)
    mean = sum(alist) / n

    # Calculate standard deviation
    sum_squared_diff = 0
    for value in alist:
        diff = value - mean
        sum_squared_diff += diff * diff

    variance = sum_squared_diff / n
    if variance < 0:  # Handle potential floating-point errors
        variance = 0
    sd = variance ** 0.5 if variance > 0 else 0 # square-root

    return mean, sd

# Test the functions
inliers = filterOutliers([9.9, 10.0, 9.7, 10.1], [9.85, 10.15])
print(inliers)
print(calcStats(inliers))
