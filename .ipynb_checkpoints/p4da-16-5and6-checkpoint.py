#!/usr/bin/env python
# coding: utf-8

# Python for Data & Analytics<br>
# Chapter 16, sections 5 and 6
# 
# *** requires datafiles: ORNG.csv, USIX.csv

# In[1]:


import pandas as pd
stockSymbol = 'ORNG'
stock = pd.read_csv(stockSymbol +'.csv', index_col=0)
stock.head()


# In[2]:


stock.tail(1)


# In[3]:


stock = stock[['AdjustedClose']]
stock.rename(columns={'AdjustedClose':stockSymbol}, inplace=True)
stock.head()


# In[4]:


stock[stockSymbol + '_Return'] = stock.pct_change()
stock.head()


# In[5]:


indexSymbol = 'USIX'
index = pd.read_csv(indexSymbol +'.csv', index_col=0)
index = index[['AdjustedClose']]
index.rename(columns={'AdjustedClose':indexSymbol}, inplace=True)
index[indexSymbol +'_Return'] = index.pct_change()
index.head()


# In[6]:


df = index.join(stock)
df.head()


# In[7]:


df[[stockSymbol,indexSymbol]].plot()


# In[8]:


import matplotlib.pyplot as plt
df[[stockSymbol, indexSymbol]].plot(secondary_y=indexSymbol, figsize=(9,7))
plt.title(stockSymbol+' vs '+indexSymbol)
plt.ylabel('Adj Closing Price')
plt.show()


# In[9]:


df[stockSymbol+'_Return'].plot(kind='hist', bins=30)


# In[10]:


df[stockSymbol+'_Return'].plot(kind='kde')


# In[11]:


df[[stockSymbol+'_Return',indexSymbol+'_Return']].plot(kind='box')


# In[12]:


df.plot(kind='scatter', x=indexSymbol+'_Return', y=stockSymbol+'_Return')


# Code from: Python for Data & Analytics, (c) 2023 Rose River Software, LLC
