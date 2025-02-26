# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 13:55:20 2025

@author: Vincent Mutungi
"""

#Question 1; Vehicle Routing
# a)
distance_Miles = eval(input('Enter the distance in miles: ')) #prompting for distance input
speed_MilePerHour = eval(input('Enter the speed in miles per hour: ')) #prompting for speed

timeTaken_Hours = distance_Miles/speed_MilePerHour #time taken calculation; division operator
print('\n The route will take', timeTaken_Hours, 'hours') #displaying results


# b)
timeTaken_Minutes = timeTaken_Hours * 60 #converting hours to minutes; multiply by 60 
print('\n The route will take', round(timeTaken_Minutes, 1), 'minutes')  #printing while rounding to one decimal


# c)
#For route type LOCAL it will take 1.0 hours that is 60.0 minutes
#For route type PARKWAY it will take  0.875 hours that is 52.5 minutes
#For route type HIGHWAY it will take  0.875 hours that is 52.5 minutes
#For route type HIGHWAY it will take  0.872 hours that is 52.4 minutes
# THEREFORE the fastest route is HIGHWAY


#Question 3; Weighted Average Forecast
pessimistic_forecast = eval(input('Enter pessimistic forecast: '))#getting input of pessimistic
middle_forecast = eval(input('Enter middle forecast.....: '))#getting input of middle
optimistic_forecast = eval(input('Enter optimistic forecast.: '))#getting input of optimistic
weighted_averageForecast = 0.25 * pessimistic_forecast + 0.5 * middle_forecast + 0.25 * optimistic_forecast#calculating weighted average forecast
print('\nWeighted average forecast = ', round(weighted_averageForecast, 0))


#Question 4; BMI-Healthy Range
height_person = eval(input('Enter your height in inches: '))#getting input of height in inches
healthy_weightLow = 18.5 * height_person ** 2 / 703
healthy_weightHigh = 24.9 * height_person ** 2 / 703
print('\nFor a height of ', height_person, 'the healthy weight range is between ', round(healthy_weightLow, 0), ' and ', round(healthy_weightHigh, 0), ' pounds.')


#Question 5; BMI-Metric
height_inches = eval(input('Enter your height in inches: '))#getting input of height(inches)
weight_pounds = eval(input('Enter your weight in pounds: '))#getting input of weight(pounds)
height_meters = height_inches * 0.0254#converting inches to meters
weight_kgs = weight_pounds * 0.453592#converting pounds to Kilograms
BMI = weight_kgs / height_meters ** 2# calculation of BMI 
print('\n Your BMI is: ', round(BMI, 2))#BMI result rounded off to 2 decimals












