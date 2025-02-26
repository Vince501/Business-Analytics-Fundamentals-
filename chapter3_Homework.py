# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 12:20:02 2025

@author: Vincent Mutungi
"""

# 1) Dollar Store
itemsNo = eval(input("Enter number of items: ")) # Getting input; no of items bought
if itemsNo < 10:
    grossCost = itemsNo * 1 # Calculating Gross Cost
    print("Gross cost: ", format(grossCost, '.2f')) # Displaying Gross Cost
    discount = grossCost * 0 # Calculating discount; zero for items less than 10
    print("Discount: ", format(discount, '.2f')) # Displaying Discount Amount
    netCost = grossCost - discount # Calculating Net Cost
    print("Net cost: ", format(netCost, '.2f')) #Displaying Net Cost
    print('') # Adding a next space
    tax = netCost * 0.075 # Calculating Tax
    print("Tax: ", format(tax, '.2f')) # Displaying Tax Amount
    afterTax = netCost + tax # Calculating After Tax Cost
    print("After tax: ", format(afterTax, '.2f')) #Displaying After Tax Amount
else:
    grossCost = itemsNo * 1
    print("Gross cost: ", format(grossCost, '.2f'))
    discount = grossCost * 0.05
    print("Discount: ", format(discount, '.2f'))
    netCost = grossCost - discount
    print("Net cost: ", format(netCost, '.2f'))
    print('')
    tax = netCost * 0.075
    print("Tax: ", format(tax, '.2f'))
    afterTax = netCost + tax
    print("After tax: ", format(afterTax, '.2f'))
    

# 2) BMI—Target Weight
height_inches = eval(input('Enter your height in inches: ')) #getting input of height(inches)
weight_pounds = eval(input('Enter your weight in pounds: ')) #getting input of weight(pounds)
bmi = (weight_pounds / (height_inches ** 2)) * 703 # Calculate BMI

if bmi < 18.5:
    min_healthy_weight = (18.5 * (height_inches ** 2)) / 703 # Minimum required weight
    weight_gain = min_healthy_weight - weight_pounds # Calculating required weight to gain to reach healthy range
    print("Weight to gain for healthy BMI:", format(weight_gain, '.2f'), "pounds")
elif bmi > 24.9:
    max_healthy_weight = (24.9 * (height_inches ** 2)) / 703 # Maximum required weight
    weight_lose = weight_pounds - max_healthy_weight # Calculating required weight to lose to reach healthy range
    print("Weight to lose for healthy BMI:", format(weight_lose, '.2f'), "pounds")
else:
    print("You are within the healthy BMI range!")
        
    
# 5) Income Taxes
income = eval(input("Enter your income: ")) # Getting income input
if income < 9876:
    income_tax = income * 0.10 # Calculating Income Tax
    effective_tax = (income_tax / income) * 100 # Calculating Effective Tax
    print("Your Marginal Tax Rate is: 10 %") #Displaying Marginal Tax Rate
    print("Your Effective Tax Rate is: ", format(effective_tax, '.2f'), "%") #Displaying Effective Tax Rate
    print("Your Income Tax is: ", format(income_tax, '.2f')) #Displaying Income Tax Amount
elif income < 40126:
    income_tax = 986 + (income * 0.12)
    effective_tax = (income_tax / income) * 100
    print("Your Marginal Tax Rate is: 12 %")
    print("Your Effective Tax Rate is: ", format(effective_tax, '.2f'), "%")
    print("Your Income Tax is: ", format(income_tax, '.2f'))
elif income < 85526:
    income_tax = 4618 + (income * 0.22)
    effective_tax = (income_tax / income) * 100
    print("Your Marginal Tax Rate is: 22 %")
    print("Your Effective Tax Rate is: ", format(effective_tax, '.2f'), "%")
    print("Your Income Tax is: ", format(income_tax, '.2f'))
elif income < 163301:
    income_tax = 14606 + (income * 0.24)
    effective_tax = (income_tax / income) * 100
    print("Your Marginal Tax Rate is: 24 %")
    print("Your Effective Tax Rate is: ", format(effective_tax, '.2f'), "%")
    print("Your Income Tax is: ", format(income_tax, '.2f'))
elif income < 207351:
    income_tax = 33272 + (income * 0.32)
    effective_tax = (income_tax / income) * 100
    print("Your Marginal Tax Rate is: 32 %")
    print("Your Effective Tax Rate is: ", format(effective_tax, '.2f'), "%")
    print("Your Income Tax is: ", format(income_tax, '.2f'))
elif income < 518401:
    income_tax = 47368 + (income * 0.35)
    effective_tax = (income_tax / income) * 100
    print("Your Marginal Tax Rate is: 35 %")
    print("Your Effective Tax Rate is: ", format(effective_tax, '.2f'), "%")
    print("Your Income Tax is: ", format(income_tax, '.2f'))
else:
    income_tax = 156235 + (income * 0.37)
    effective_tax = (income_tax / income) * 100
    print("Your Marginal Tax Rate is: 37 %")
    print("Your Effective Tax Rate is: ", format(effective_tax, '.2f'), "%")
    print("Your Income Tax is: ", format(income_tax, '.2f'))





















