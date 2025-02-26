# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 12:27:01 2025

@author: Vincent Mutungi
"""

import pandas as pd

df = pd.read_csv('Class files/SP500_Constituents.csv')
dfsp = pd.read_csv('Class files/SP500_Constituents.csv', index_col='Symbol')

dfsp5 = dfsp.head()
len(dfsp)
dfsp.shape
dfsp.info()

dfAQI = pd.read_csv('Class files/aqi.txt', index_col='color')
dfAQI['concern'] 
dfAQI.concern

dfAQI['concern'].tolist()
dfAQI[['low', 'high']]
dfAQI.index.tolist()
dfsp.Security

dfAQI.loc['Yellow']
dfAQI.iloc['0']	
dfAQI.loc['Red']['concern']
dfAQI['concern']['Red'] #df['colname']['rowname']

