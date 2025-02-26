# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 12:44:22 2025

@author: Vincent Mutungi
"""

colors = ['blue', 'yellow', 'black', 'purple']
squares = [1, 4, 9, 16, 25, 36]

colors[-1] # purple
len(colors)
len(squares)
min(colors)
max(colors)
sum(squares)
concant = colors + squares
concant

squares.append(49) #adds at the end of the list
colors.count('black')

colors.append('black')
colors.count('black')

squares.index(36) 
colors.index('black')
colors.index('black') # finds the index of the first occurrence

colors.pop() #removes last item in the list
colors.remove('black') #revomes from list

colors.sort() #ascending order
colors.reverse() #descending order

#Group assignment IN CLASS

list_heights = []
while True:
    height_inches = input('Enter height in inches or just press Enter to end: ')
    
    if height_inches == '':
        break  # Stop if input is blank
    
    height_inches = eval(height_inches)    
    list_heights.append(height_inches) # Appends the list

    
        
if len(list_heights) > 0:
    list_heights.sort() # Sorts the list to find median
    
    # Calculating average
    total = 0
    for h in list_heights:
        total += h
        avg_height = total / len(list_heights)

    # Calculating range
    height_range = list_heights[-1] - list_heights[0]  # Since the list is sorted already

    # Calculating median
    mid = len(list_heights) // 2
    if len(list_heights) % 2 == 0:
        median_height = (list_heights[mid - 1] + list_heights[mid]) / 2
    else:
        median_height = list_heights[mid]

    # Calculating standard deviation
    sum_squares = 0
    for h in list_heights:
        sum_squares += (h - avg_height) ** 2
    std_dev = (sum_squares / (len(list_heights) - 1)) ** 0.5 if len(list_heights) > 1 else 0

    # Display results
    print("\nHeight Statistics:")
    print("\nAverage Height: {:.2f} inches".format(avg_height))
    print("\nRange: {:.2f} inches".format(height_range))
    print("\nMedian: {:.2f} inches".format(median_height))
    print("\nStandard Deviation: {:.2f} inches".format(std_dev))
else:
    print("No heights entered. Exiting program...")

