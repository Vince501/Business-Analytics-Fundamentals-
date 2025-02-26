# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 13:01:05 2025

@author: Vincent Mutungi
"""

# Problem 2.2 Page 28
#Developed a written plan in class

#  A store charges $2.75 for every product it sells. There is also a sales tax of 6% on all purchases.

# a) Write a program that prompts the user for the number of items purchased, and calculates the before-tax cost, sales tax, and total cost. Example run:
# Number of items: 3
# Pretax cost: 8.25
# Sales tax:   0.495
# Total cost:  8.745

# b) Refine your program so sales tax is rounded to two decimal places. Example run:
# Number of items: 3
# Pretax cost: 8.25
# Sales tax:   0.49
# Total cost:  8.74

items = eval(input('Number of items: ')) #get input from user
subtotal = items * 2.75 #calculate pretax cost
tax = subtotal * 0.06 + 0.001 #calculate sale tax
tax_string = '$' + format(tax, '.2f')
total = subtotal + tax #calculate total cost; pretax cost + sales tax
total_string = '$' + format(total, '.2f')

#printing results
# print('Pretax cost: ', round(subtotal, 2))
# print('Sales tax: ', round(tax, 2))
# print('Total cost: ', round(total, 2), '\n \n')

print('Pretax cost:', subtotal, sep='\t')
print('Sales tax:', tax_string, sep='\t')
print('Total cost:', total_string, sep='\t')


# pandas example:
import pandas as pd
dfAQI = pd.read_csv('Class files/aqi.txt')

dfAQI1 = pd.read_csv('Class files/aqi_pipe.txt', index_col='color', comment='#', delimiter='|')


adict = {'column1': [1, 2, 3], 'column2': [4, 5, 6]}
df = pd.DataFrame(adict)



# define AQI levels as a DataFrame of colors, concerns and ranges
# using a dictionary of parallel lists
import pandas as pd

# define the dictionary of parallel lists
dictAQI = {
'color': ['Green', 'Yellow', 'Orange', 'Red', 'Purple', 'Maroon'],
'concern': ['Good', 'Moderate', 'Unhealthy for Sensitive Groups',
'Unhealthy', 'Very Unhealthy', 'Hazardous'],
'low': [0, 51, 101, 151, 201, 301],
'high':[50, 100, 150, 200, 300, 999]}

# create a DataFrame from the dictionary
dfAQI = pd.DataFrame(dictAQI)
# display the DataFrame
print(dfAQI)

# This statement can be used to read the above file:
import pandas as pd
df = pd.read_csv('Class files/aqi_pipe.txt',
index_col='color',
delimiter='|',
comment='#')
df

import pandas as pd
dfsp = pd.read_csv('CSV files/SP500_Constituents.csv')
# Alternatively, we can set the Symbol column to the index, using
dfsp = pd.read_csv('CSV files/SP500_Constituents.csv', index_col='Symbol')
# The DataFrame's head() method returns its first rows
dfsp.head()
# Optionally can indicate how many rows to return
dfsp.head(10)
# head() returns a DataFrame; can assign its result to a variable
dfsp5 = dfsp.head(5)
dfsp5
# Returning no of rows
len(dfsp)
# Returning no of rows and columns
dfsp.shape
# Returning types and counts of each column
dfsp.info()


import pandas as pd
dfAQI = pd.read_csv('Class files/aqi_pipe.txt',
index_col='color',
delimiter='|',
comment='#')
dfsp = pd.read_csv('CSV files/SP500_Constituents.csv', index_col='Symbol')
# To access a particular DataFrame column, use square brackets [ ]; similar to Python list and dictionary item access
dfAQI['concern']
#The result of column access is a pandas Series
type(dfAQI['concern'])
#Shorthand for column access:
dfAQI.concern
#Convert from Series to list using tolist() method
dfAQI['concern'].tolist()
#Get a subset of DataFrame's column with double brackets [[ ]]
dfAQI[['low', 'high']]
# Access by index name: .loc[ ]
dfAQI.loc['Yellow']
# Access by row number: .iloc[ ] 
dfAQI.iloc[0]


# interactive data lookup program - S&P 500 securities
import pandas as pd
dfsp = pd.read_csv('CSV files/SP500_Constituents.csv', index_col='Symbol')
symbol = input('Enter security symbol of interest: ')
while symbol != '':
    symbol = symbol.upper() #symbols are upper case in the data
    if symbol in dfsp.index:# check if symbol is in data
            row = dfsp.loc[symbol] # locate the data using loc[]
            print(row)
    else:
        print('Not found')
        
dfAQI.loc['Red']['concern']


#To sort a DataFrame, use the sort_values() method; False to get result in descending order
dfAQI.sort_values('low', ascending=False)
dfAQI.sort_values('low', ascending=False, inplace=True)
dfAQI


# A filter expression returns a subset of rows
dfAQI[dfAQI.high <= 100]
#filter expressions can have a compound condition
# =============================================================================
# compound operators:
# & and
# | or
# ~ not
# =============================================================================
level = 75
dfAQI[(dfAQI.low <= level) & (level <= dfAQI.high)]


# Similar to lists, DataFrames provide slicing to get part of the data
dfAQI.sort_values('low', ascending=True, inplace=True)
dfAQI[:3]


# for and iterrows() will loop over DataFrame rows
for color, row in dfAQI.iterrows():
    print(color+ ':', row.concern)


# isna() method can locate missing data with a filter expression
dfAQI[dfAQI.high.isna()]
# notna() method can be used to filter out data with missing values


# a list can be appended to a DataFrame: df['colname'] = list
dfAQI['number'] = [1, 2, 3, 4, 5, 6]
dfAQI

# Appending a row
import pandas as pd
newrow = \
    pd.DataFrame({'concern':['Worst'],'low':[1000],'high':[9999],'number':7},
                 index=['Brown'])
pd.concat([dfAQI, newrow])
dfAQI


# Deleting a column
dfAQI.drop('number', axis='columns', inplace=True)
dfAQI
# Deleting a row
dfAQI.drop('Maroon', inplace=True)
dfAQI

# Updating a cell's value
dfAQI.at['Orange', 'concern'] = 'Unhealthy For Some'
dfAQI











