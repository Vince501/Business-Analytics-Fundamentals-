# -*- coding: utf-8 -*-
"""
@author: Chad.Birger
"""

import pandas as pd
df_hotel = pd.read_csv('Class files\Hotel_Ratings.csv')
####
def orderRankings(value):
    if value == 'Terrible':
        val = '1 - Terrible'
    elif value == 'Poor':
        val = '2 - Poor'
    elif value == 'Average':
        val = '3 - Average'
    elif value == 'Very Good':
        val = '4 - Very Good'
    else:
        val = '5 - Excellent'
    return val

df_hotel['Ranking'] = df_hotel['Rating'].apply(orderRankings)
####

df_hotel_pivot = df_hotel.pivot_table(values= 'Customer', index = "Ranking", aggfunc='count')

df_hotel_pivot['Customer'].plot(kind='bar')
df_hotel_pivot['Customer'].plot(kind='pie')

import seaborn as sns
sns.countplot(data=df_hotel, x='Ranking')
