# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 09:50:14 2025

@author: Vinny
"""

# =============================================================================
# Name: Mutungi, Vincent
# Course: Business Analytic Fundamentals, DSCI 505
# =============================================================================

# =============================================================================
# Question 2.1
# Write a program that prompts for the price of an item, prompts for the number of that item purchased, 
# then calculates and displays the pre-tax cost, the total sales tax (assume a 7.5% tax rate), 
# and the after-tax cost (pre-tax cost plus total sales tax).  
# All calculated values should be rounded to the nearest 2 decimals.
# 
# Example run:
# Enter price per item: 2.50
# Enter number of items: 3
# Pre-tax cost= 7.5
# Tax paid= 0.56
# After-tax cost= 8.06
# =============================================================================

# Prompting the user to enter the price per item and convert it to a float number
price_per_item = float(input("Enter price per item: "))
# Prompting the user to enter the number of items purchased and convert it to an integer
no_items = int(input("Enter number of items: "))

# Calculating the pre-tax cost by multiplying price per item by the number of items
pre_tax_cost = round(price_per_item * no_items, 2) # Rounding the result to 2 decimal places
# Calculating the total sales tax by multiplying the pre-tax cost by the tax rate (7.5%)
sales_tax = round(pre_tax_cost * 0.075, 2) # Rounding the result to 2 decimal places
# Calculating the after-tax cost by adding the pre-tax cost and the total sales tax
after_tax_cost = round(pre_tax_cost + sales_tax, 2) # Rounding the result to 2 decimal places

print("Pre-tax cost =", pre_tax_cost) # Displaying the pre-tax cost
print("Tax paid =", sales_tax) # Displaying the total sales tax paid
print("After-tax cost =", after_tax_cost) # Displaying the final after-tax cost

# =============================================================================
# Question 3.3
# A company offers quantity discounts for a certain product.  If less than 5 items are purchased, 
# the cost per item is $10.  If 5 - 10 items are purchased, the cost per item is $9.  
# If more than 10 items are purchased, the cost per item is $8.
# Write a program that prompts for the number of items purchased, then calculates and displays the total cost.  
# Your program should display an error message if the number of items entered is negative.
# 
# Example run:
# Enter number of items: 5
# Total cost: $ 45
# =============================================================================

# Prompting the user to enter the number of items and convert input to an integer
no_items = int(input("Enter number of items: "))
# Checking if the entered number of items is negative
if no_items < 0:
    print("Error: Number of items cannot be negative.") # Displaying an error message if the input is negative
else:
    # Determining the price per item based on quantity purchased
    if no_items < 5:
        price_per_item = 10  # Price per item is $10 if less than 5 items are purchased
    elif no_items <= 10:
        price_per_item = 9   # Price per item is $9 if between 5 and 10 items (inclusive) are purchased
    else:
        price_per_item = 8   # Price per item is $8 if more than 10 items are purchased

    # Calculating the total cost by multiplying the number of items by the price per item
    total_cost = no_items * price_per_item
    # Displaying the total cost with a dollar sign
    print("Total cost: $", total_cost)


# =============================================================================
# Question 4.3
# A parking garage charges $5 plus $2.50 for each hour parked.  Further, the minimum fee is $10.
# Write a program to print a table of hours and fees, from 1 to 6 hours, in increments of ½ hours.  
# Use either a while or for statement.
# 
# Example output:
# Hours Fee
# 1.0  $10.00
# 1.5  $10.00
# 2.0  $10.00
# 2.5  $11.25
# 3.0  $12.50
# 3.5  $13.75
# 4.0  $15.00
# 4.5  $16.25
# 5.0  $17.50
# 5.5  $18.75
# 6.0  $20.00
# =============================================================================

# Initializing the hours variable to start from 1.0
hours = 1.0 
print("Hours  Fee") # Printing table header 
# Loop while hours is less than or equal to 6.0
while hours <= 6.0:
    # Calculating the total fee using the formula: base fee + (extra hours * rate per hour)
    fee = 5 + (hours * 2.5)  
    # Ensuring the minimum fee is $10
    if fee < 10:
        fee = 10 
    print(f"{hours:.1f}  ${fee:.2f}") # Print the hours and fee, formatted to 2 decimal places for proper alignment
    # Incrementing hours by 0.5 to move to the next half-hour slot
    hours += 0.5  

# =============================================================================
# Question 5.2
# Write a function named calcCost, that takes two required input parameters, count and price.  
# The function should also have one named parameter named discount.  The signature of the function should be:
#    def calcCost(count, price, discount=.1)
# The function should return:
#    count * price if the count is less than 5, or
#    count * price * (1-discount) if the count is 5 or more
#    
# Below the function, write test statements to determine and display the cost for 10 items priced at $15, using a discount of 20%.
# Sample output:
# Cost = $ 120.0
# =============================================================================

# Defining the function with count, price, and an optional discount parameter (default is 10%)
def calcCost(count, price, discount=0.1):
    # If count is less than 5, no discount is applied
    if count < 5:
        return count * price
    else:
        # If count is 5 or more, apply the discount
        return count * price * (1 - discount)

# Testing the function with 10 items, price $15, and a discount of 20% (0.2)
cost = calcCost(10, 15, discount=0.2)
# Displaying the calculated cost
print("Cost = $", cost)

# =============================================================================
# Question 6.2
# Assume the following are sales for each day of the week:
#  Monday: $50
#  Tuesday: $75
#  Wednesday: $150
#  Thursday: $125
#  Friday: $100
# Write a program that determines the day with the most sales.  Use two lists in your program 
# (one for the sales, one for the days of the week).
# 
# Sample output:
# Max sales = $ 150
# Max sales day = Wednesday
# =============================================================================

# Listing of days of the week in a list called days
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# Listing of corresponding sales for each day in a list called sales
sales = [50, 75, 150, 125, 100]

# Finding the maximum sales value using max function
max_sales = max(sales)
# Finding the index of the maximum sales value in the sales list
max_sales_index = sales.index(max_sales)
# Getting the corresponding day using the same index from the days list
max_sales_day = days[max_sales_index]

# Displaying the results
print("Max sales = $", max_sales)
print("Max sales day =", max_sales_day)





















