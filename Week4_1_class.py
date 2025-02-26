# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 12:58:36 2025

@author: Vince
"""

#number
num = eval(input('Enter a number:'))
if num>0:
    print(num, 'is a positive number!')
elif num<0:
    print(num, 'is a negative munber!')
else:
    print(num, 'is neither positive nor negative')
    

#bmi
bmi = eval(input('Enter your  BMI: '))
if bmi < 18.5:
    print("Your BMI is BELOW the 'healthy' range!")
elif bmi <= 24.9:
    print("Your Your BMI is in the 'healthy' range")
else:
    print("Your BMI is OVER the 'healthy' range!")
                
    
    
# Nested (Sequential) Decisions
# =============================================================================
#  Calculate the ending balance of a 1-year certificate of deposit
#  Consider new vs existing customers, and 2 rates for existing customers
# =============================================================================
# Prompt for type of customer
customer = input('Enter n if customer is new, or e for existing: ')
# Prompt for the initial investment
invest = float(input('Please enter investment amount: '))
if customer == 'e':# Determine the interest rate, depending on the size of the investment
    if invest >= 1000:
        interestRate = 3.25
    else:
            interestRate = 3.0
else:
    interestRate = 3.5
    # Calculate the ending balance
endBalance = invest * (1 + interestRate/100)
# Display the result
print('Interest rate=', interestRate, '%')
print('Ending balance= $', endBalance)
